import pandas as pds 

datafr = pds.read_csv('/home/kaustubh/Documents/Automobile_data.csv')

g = datafr.groupby('company')

k = g['price'].max()
print(k)
    
    


