######################################################################################  
#pandas dataframe
#dro wows that has nan/none values
#delete rows with non values
import numpy as np
import pandas as pd
technologies={
    'courses':['spark','pyspark','hadoop','python'],
    'fee':[20000,25000,16000,22000],
    'duration':[' ','40days',np.nan,None],
    'discount':[1000,2300,1500,1200]
    }
#np.nan is a invalid or missing value
#none is a no value/empty
inedxes=['r1','r2','r3','r4']  
df=pd.DataFrame(technologies,index=inedxes)
df
df2=df.dropna()#removes empty space
df2
#droping rows with Nan(np.na,None)
df_clean=df.dropna(subset=['duration'])
#dropping rows with empty strings
df_clean=df_clean[df_clean['duration']!=' ']        
df_clean        
