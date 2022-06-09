import pandas as pd
import numpy as np
import requests as rq
import selenium as sn
import yfinance as yf
import matplotlib.pyplot as plt

militar_companies_list = ['HON', 'RTX', 'LMT', 'ATRO', 'AJRD', 'NOC', 'TXT', 'HEI',]
data = yf.download(militar_companies_list, start = '2022-01-01', end = '2022-05-31')

