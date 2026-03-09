import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

#inisialisasi 
df = pd.read_excel('Dataset_Dummy_MBG.xlsx')
print(df.head())

