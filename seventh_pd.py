import pandas as pds 

datafr = pds.read_csv('/home/kaustubh/Documents/Automobile_data.csv')

maximum = datafr['price'].max()
print(maximum)

lol = datafr[['company', 'price']][datafr['price'] == maximum]
print(lol)