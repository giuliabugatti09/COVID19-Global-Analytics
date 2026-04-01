import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from scipy import stats
import logging
import os

# Professional Logging Setup
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CovidAnalyzer:
    """
    A professional class for COVID-19 data analysis, 
    handling ETL, statistical validation, and visualization.
    """

    def __init__(self, data_url):
        self.data_url = data_url
        self.df_raw = None
        self.df_countries = None
        self.df_brazil = None

    def load_data(self):
        """Extract: Downloads and parses the global dataset."""
        try:
            logging.info("Starting Data Extraction...")
            self.df_raw = pd.read_csv(self.data_url, parse_dates=['date'])
            logging.info(f"Successfully loaded {len(self.df_raw)} records.")
        except Exception as e:
            logging.error(f"Failed to download data: {e}")
            raise

    def preprocess(self):
        """Transform: Cleans aggregates and engineers mortality metrics."""
        if self.df_raw is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        logging.info("Starting Data Transformation...")
        df = self.df_raw.copy()
        
        # Filter: Remove non-country aggregates (continent is NaN for aggregates)
        df = df[df['continent'].notna()].copy()
        
        # Handle Missing Values in core mortality columns
        df.dropna(subset=['total_deaths', 'total_cases'], inplace=True)
        
        # Feature Engineering: Mortality Rate
        df['mortality_rate'] = (df['total_deaths'] / df['total_cases']) * 100
        
        self.df_countries = df.reset_index(drop=True)
        
        # Isolate Brazil for time-series analysis
        self.df_brazil = self.df_countries[self.df_countries.location == 'Brazil'].copy()
        self.df_brazil['cases_7d_avg'] = self.df_brazil['new_cases'].rolling(window=7).mean()
        self.df_brazil['deaths_7d_avg'] = self.df_brazil['new_deaths'].rolling(window=7).mean()
        
        logging.info("Transformation complete. Country-level data ready.")

    def run_statistical_test(self, col1='aged_65_older', col2='total_deaths_per_million'):
        """Performs Pearson Correlation and T-test for significance."""
        data = self.df_countries[[col1, col2]].dropna()
        r, p_value = stats.pearsonr(data[col1], data[col2])
        
        n = len(data)
        df_degrees = n - 2
        t_calc = (r * np.sqrt(df_degrees)) / np.sqrt(1 - r**2)
        t_crit = stats.t.ppf(1 - 0.025, df_degrees)

        result = {
            "r": r,
            "p_value": p_value,
            "t_calc": t_calc,
            "t_crit": t_crit,
            "significant": abs(t_calc) > t_crit
        }
        
        logging.info(f"Statistical Test Complete. Significant: {result['significant']}")
        return result

    def save_plot_ranking(self, column, title, filename, palette="viridis"):
        """Generates and saves Top 5 ranking plots."""
        latest = self.df_countries.dropna(subset=[column]).sort_values('date').groupby('location').last()
        top_5 = latest.nlargest(5, column).reset_index()
        
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(data=top_5, x=column, y='location', hue='location', palette=palette, legend=False)
        
        # Formatting and Annotations
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        for p in ax.patches:
            width = p.get_width()
            ax.annotate(f'{width:,.1f}', (width, p.get_y() + p.get_height() / 2), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

        plt.title(f"{title} (Latest Available Data)")
        plt.tight_layout()
        
        # Create images folder if not exists
        os.makedirs('images', exist_ok=True)
        plt.savefig(f'images/{filename}')
        plt.close() # Clean memory
        logging.info(f"Plot saved: images/{filename}")

# Main execution block
if __name__ == "__main__":
    URL = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    
    analyzer = CovidAnalyzer(URL)
    analyzer.load_data()
    analyzer.preprocess()
    
    # Statistical Validation
    stats_res = analyzer.run_statistical_test()
    print(f"\nSignificance Report: {stats_res}\n")
    
    # Generate Plots for the README
    analyzer.save_plot_ranking('total_cases', 'Top 5: Total Cases', 'top_cases.png', 'magma')
    analyzer.save_plot_ranking('people_vaccinated_per_hundred', 'Top 5: Vax Coverage', 'top_vax.png', 'viridis')