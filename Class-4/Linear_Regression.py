import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('Dhaka Rent - Dhaka Rent.csv')

area,rent= df['area'],df['rent']
rent_bar = rent.mean()
area_bar = area.mean()


area_bar_sq2 = (area**2).mean()
area_bar_sq = area_bar**2


rent_bar_area_bar =  (area * rent).mean()

m = ( (rent_bar_area_bar) - (area_bar * rent_bar))/(area_bar_sq2 - area_bar_sq)
c = rent_bar - (m*area_bar)

y = m*area + c
df['predicted'] = y


from matplotlib import pyplot as plt
plt.plot(area,df['predicted'])
plt.scatter(df['area'], df['rent'], color='blue')
plt.xlabel('Area')
plt.ylabel('Rent')
plt.title('Dhaka Rent Analysis')

plt.show()


print(df) 



