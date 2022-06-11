import pandas as pd
import numpy as np
import requests as rq
import selenium as sn
import yfinance as yf
import matplotlib.pyplot as plt

usa_militar_companies = ['LMT', 'RTX', 'GD', 'NOC', 'HII']
europe_militar_companies = ['AIR.PA', 'BAESY', 'HO.PA', 'RHM.DE', 'LDO.MI']

data_usa    = yf.download(usa_militar_companies, start = '2022-01-01', end = '2022-05-31')
data_europe = yf.download(europe_militar_companies, start = '2022-01-01', end = '2022-05-31')

pd_usa = pd.DataFrame(data_usa)
pd_europe =pd.DataFrame(data_europe)

pd_usa.to_excel("C:/Users/Mauricio Ortiz/Downloads/usa_data.xlsx")
pd_europe.to_excel("C:/Users/Mauricio Ortiz/Downloads/europe_data.xlsx")