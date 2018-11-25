import pandas as pd
import matplotlib.pyplot as plt

Startup_df=pd.read_csv("C:\\Users\HP\\Documents\\KaggleProjects\\IndianStartups\\startup_funding.csv")
Startup_df.info()

Startup_df['InvestmentType'].hist()