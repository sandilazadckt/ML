import pandas as pd
 

df = pd.read_csv("Book1.csv")


# Normalization 
x_new =  (df["price"] - df["price"].min())/(df["price"].max()-df["price"].min())
df["price_scale"] = x_new
print(df.head())


# Normalization 
x_new =  (df["price"] - df["price"].min())/(df["price"].max()-df["price"].min())
df["price_scale"] = x_new
print(df.head())


from matplotlib import pyplot as plt
plt.plot(df['price'],df['price_scale'])
plt.title('Dhaka Rent Analysis')

plt.show()