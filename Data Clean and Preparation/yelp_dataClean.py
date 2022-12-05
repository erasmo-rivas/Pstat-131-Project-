import pandas as pd
# WE ONLY KEPT DATA WITH MORE THAN 7 ATTRIBUTES 



yelp_df = pd.read_csv("yelpRestaurant.csv", low_memory = False)

music = []
for i in range(len(yelp_df)):
    if len(yelp_df.iloc[i].Music) > 3:
        music.append(True)
    else:
        music.append(False)


yelp_df["Music"] = music

del yelp_df["BusinessAcceptsCreditCards"]



Reservation = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].RestaurantsReservations
    if "ALSE" in item.upper() or "RUE" in item.upper():
        Reservation.append(item)
    else:
        Reservation.append(False)

yelp_df["RestaurantsReservations"] = Reservation






outdoor = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].OutdoorSeating
    if "ALSE" in item.upper() or "RUE" in item.upper():
        outdoor.append(item)
    else:
        outdoor.append(False)

yelp_df["OutdoorSeating"] = outdoor








happyHour = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].HappyHour
    if "ALSE" in item.upper() or "RUE" in item.upper():
        happyHour.append(item)
    else:
        happyHour.append(False)

yelp_df["HappyHour"] = happyHour






del yelp_df["Open24Hours"]

del yelp_df["Smoking"]  # a lot of missing data





    


driveThru = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].DriveThru
    if "ALSE" in item.upper() or "RUE" in item.upper():
        driveThru.append(item)
    else:
        driveThru.append(False)

yelp_df["DriveThru"] = driveThru


        






caters = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].Caters
    if "ALSE" in item.upper() or "RUE" in item.upper():
        caters.append(item)
    else:
        caters.append(False)

yelp_df["Caters"] = caters





del yelp_df["BYOBCorkage"]







delivery = []
for i in range(len(yelp_df)):
    bools = [True, False]
    item = yelp_df.iloc[i].RestaurantsDelivery
    if "ALSE" in item.upper() or "RUE" in item.upper():
        delivery.append(item)
    else:
        delivery.append(False)


yelp_df["RestaurantsDelivery"] = delivery





del yelp_df["RestaurantsAttire"]

del yelp_df["BestNights"]







alc = []
for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].Alcohol
    if "none" in item or "0" in item:
        alc.append(False)
    else:
        alc.append(True)




yelp_df["Alcohol"] = alc





del yelp_df["AcceptsInsurance"]

del yelp_df["DogsAllowed"]

del yelp_df["RestaurantsTakeOut"]







wifi = []

for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].WiFi
    if "free" in item:
        wifi.append(True)
    else:
        wifi.append(False)

yelp_df["WiFi"] = wifi






del yelp_df["DietaryRestrictions"]







groups = []

for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].RestaurantsGoodForGroups
    bools = [True, False]
    if "ALSE" in item.upper() or "RUE" in item.upper():
        groups.append(item)
    else:
        groups.append(False)








yelp_df["RestaurantsGoodForGroups"] = groups

kids = []
for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].GoodForKids
    bools = [True, False]
    if "ALSE" in item.upper() or "RUE" in item.upper():
        kids.append(item)
    else:
        kids.append(False)
        
yelp_df["GoodForKids"] = kids








del yelp_df["Corkage"]
del yelp_df["BYOB"]
del yelp_df["ByAppointmentOnly"]
del yelp_df["RestaurantsCounterService"]








wheelchair = []

for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].WheelchairAccessible
    bools = [True, False]
    if "ALSE" in item.upper() or "RUE" in item.upper():
        wheelchair.append(item)
    else:
        wheelchair.append(False)

yelp_df["WheelchairAccessible"] = wheelchair







del yelp_df["BusinessAcceptsBitcoin"]
del yelp_df["BikeParking"]







table = []
for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].RestaurantsTableService
    bools = [True, False]
    if "ALSE" in item.upper() or "RUE" in item.upper():
        table.append(item)
    else:
        table.append(False)

yelp_df["RestaurantsTableService"] = table








tv = []
for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].HasTV
    bools = [True, False]
    if "ALSE" in item.upper() or "RUE" in item.upper():
        tv.append(item)
    else:
        tv.append(False)




yelp_df["HasTV"] = tv










del yelp_df["AgesAllowed"]
del yelp_df["GoodForDancing"]
del yelp_df["CoatCheck"]
del yelp_df["HairSpecializesIn"]
del yelp_df["BusinessParking"]
del yelp_df["attributes"]
del yelp_df["NoiseLevel"]
del yelp_df["Ambience"]
del yelp_df["hours"]



D = {"dessert":[],"latenight":[],"lunch":[],"dinner":[],"brunch":[],"breakfast":[]}

for i in range(len(yelp_df)):
    item = yelp_df.iloc[i].GoodForMeal
    if len(item) < 10:
        for obj in D.keys():
            D[obj].append(False)
    else:
        item = yelp_df.iloc[i].GoodForMeal.strip("{}").split(",")
        for obj1 in item:
            if len(obj1.split(":")) > 1:
                
                meal = obj1.split(":")[0].strip(" '")
                meal = meal.strip("u'")
            
                boolean = obj1.split(":")[1].strip()
                if "ALSE" in boolean.upper() or "RUE" in boolean.upper():
                    D[meal].append(boolean)
                else:

                    D[meal].append(False)
                
            
                



yelp_df["GoodForDessert"] = D["dessert"]
yelp_df["GoodForLatenight"] = D["latenight"]
yelp_df["GoodForLunch"] = D["lunch"]
yelp_df["GoodForBrunch"] = D["brunch"]
yelp_df["GoodForBreakfast"] = D["breakfast"]

del yelp_df["GoodForMeal"]
del yelp_df["GeqSevAttr"]





yelp_df.to_csv("ProjectDataset.csv")






    
    








    



