import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])
df = pd.DataFrame(np.arange(12).reshape((3,4)))
dates = pd.date_range('20190705',periods=8)
df1 = pd.DataFrame(np.random.randn(8,4),index=dates,columns=['a','b','c','d'])
print(df1)