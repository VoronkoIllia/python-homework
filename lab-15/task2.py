import pandas as pd
import matplotlib.pyplot as plt
from os import path

plt.style.use('ggplot') 

plt.rcParams['figure.figsize'] = (15, 5) 

fixed_df = pd.read_csv(path.join(path.dirname(__file__), "data.csv"), 
                       sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
print(fixed_df[:3])
fixed_df.plot(figsize=(15, 10))
plt.show()
