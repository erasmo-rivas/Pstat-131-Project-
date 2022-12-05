import json
import pandas as pd
data_file = open("yelp_academic_dataset_business.json", errors = "ignore")
data = []
for line in data_file:
    data.append(json.loads(line))
business_df = pd.DataFrame(data)
data_file.close()





Restaurant  = []
for i in range(len(business_df.categories)):
    
    categoryStr = str(business_df.iloc[i].categories)
    categoryList = categoryStr.split(", ")
    
    k = 0
    for item in categoryList:
        if item.upper() == "RESTAURANTS" or item.upper() == "RESTAURANT":
            k += 1
    if k >= 1:
        Restaurant.append(1)
    elif k == 0:
        Restaurant.append(0)

business_df["isRestaurant"] = Restaurant 
business_df.drop(business_df.loc[business_df['isRestaurant']==0].index, inplace=True)
business_df.dropna(inplace = True)   # removes rows with NA values 



z = []
for i in range(len(business_df)):
    if len(business_df.iloc[i].attributes.keys()) < 7:
        z.append(0)
    else:
        z.append(1)
business_df["GeqSevAttr"] = z
business_df.drop(business_df.loc[business_df['GeqSevAttr']==0].index, inplace=True)   # we are only keeping data points with 7 or more attributes


attr = set()       
for i in range(len(business_df)):   # creates a set of the unique attribute names
    for item in business_df.iloc[i].attributes.keys():
        if item not in attr:
            attr.add(item.upper())
        else:
            continue


Attributes = {}     # cresates a dictionary {attribute name: value or 0}
for item in attr:
    Attributes[item] = []


for i in range(len(business_df)):
    keys = []  
    for item in business_df.iloc[i].keys():
        keys.append(item.upper())
        
    for j in attr:
        if j in keys:
            Attributes[j].append(business_df.iloc[i][j])  # this adds the attribute value 
        else:
            Attributes[j].append(0)  # may want to change this to NA or someother value
            



    
for item in Attributes.keys():
    business_df[item] = Attributes[item]

print(business_df.columns)

    

    

business_df.to_csv("yelpRestaurant.csv")
