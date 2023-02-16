import pandas as pd
import matplotlib.pyplot as mp
import random

csv = pd.read_csv('2016-2019.csv')

csv2 = csv.sort_values(by=['zip_code'], ascending=False)

csv3 = csv2.groupby(['zip_code','item_description'])['bottles_sold'].sum()
bs= csv2.groupby('store_name')['bottles_sold'].sum()

store =bs.index

sam= 0

per=[]

for i in range(len(bs)):
    sam += bs[i]

for j in range(len(bs)):
    per.append((bs[j]/sam)*100)

perdf= pd.DataFrame(per, index= store, columns=['percentage (%)'])

zip=csv3.index.get_level_values('zip_code')


no_of_colors=len(zip)
colors1=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]

no_of_colors=len(per)
colors2=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]

print(perdf)
print(" ")
print(csv3.head(10))


mp.subplot(1,2,1)
mp.barh(store,per, color=colors2)
mp.xlabel("percentage (%)")
mp.yticks(rotation= 7)

mp.subplot(1,2,2)
mp.scatter(zip,csv3, color=colors1)
mp.xlabel("zip codes")
mp.ylabel("bottles sold")
mp.show()











