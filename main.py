import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data.csv')
#print(df.head())
#print(df.columns)
#print(df.shape)
#print(df.info())

#Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
#print(df.columns.tolist())
df = df.drop_duplicates()


#Numeric columns cleaning
df['price'] = df['price'].astype(str).str.replace(',','').astype(float)
#print(df['price'])
df['area'] = df['area'].astype(str).str.replace(',','').astype(int)
#print(df['area'])
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)
#print(df['rate_per_sqft'])





#Categorical columns cleaning
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})

df["flat_type"] = df["flat_type"].str.strip().str.lower()

#print(df["flat_type"])


df= df.drop_duplicates()

#print(df)
#print(df.info())

#Question 1: Which is the costliest flat?
costliest_flat = df.loc[df['price'].idxmax()]

'''
Let's write this output as a sentence:
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                       6
society                             DLF Camellias
company_name                                  DLF
flat_type                               apartment
'''

#print(costliest_flat)

print(f"The costliest flat is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']}. It has an area of {costliest_flat['area']} sqft and a rate per sqft of {costliest_flat['rate_per_sqft']}. The flat is built by {costliest_flat['builder_name']} and has RERA approval status: {costliest_flat['rera_approval']}.")

#Question 2: Which locality has the highest average price?

highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f'The locality with the highest average price is {highest_avg_price_locality}.')

#Question 3: Which locality has the highest rate per square foot?

highest_avg_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f'The locality with the highest average rate per square foot is {highest_avg_rate_locality}.')


#Question 4: Ready-to-move vs Under-construction pricing

ready_to_move_avg_price = df[df['status'] == 'ready_to_move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under_construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more on average.")
elif ready_to_move_avg_price < under_construction_avg_price:
    print("Under-construction properties cost more on average.")
else:
    print("Both property types have the same average price.")  
    
#Question 5: Does RERA approval affect pricing?

rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print("RERA-approved properties cost more on average.")
elif rera_approved_avg_price < rera_not_approved_avg_price:
    print("Non-RERA-approved properties cost more on average.")
else:
    print("RERA-approved and non-RERA-approved properties have the same average price.")
    
#6. Deeper Insights
#sns.scatterplot(data = df, x = 'area', y = 'price')
#plt.show()

#Question 7: Which BHK configuration is most expensive?
most_expensive_BHK = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f'The most expensive BHK configuration is {most_expensive_BHK} BHK.')

#Question 8: Which property type is the costliest?
costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f'The costliest property type is {costliest_property_type}.')

#Question 9: Do certain builders price higher?
builder_avg_price = df.groupby('company_name')['price'].mean().sort_values(ascending=False)
print("Average price by builder:")
print(builder_avg_price)

#Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(data = df, x = 'area', y = 'rate_per_sqft')
plt.show() 