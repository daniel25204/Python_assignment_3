# 11.12.1.1
medal_count = {
    "United States" : 70,
    "Great Britain" : 38,
    "China" : 45,
    "Russia" : 30,
    "Germany" : 17
}



# 11.12.1.2
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}    
swimmers["Phelps"] = 23



# 11.12.1.3
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"] = 3



# 11.12.1.4
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] = golds["Spain"] + 2



# 11.12.1.5
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = golds.keys()
print(countries)



# 11.12.1.6
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, ...}   
# NOTE : the above line is too long and already provided in the sample answer. all u need is the codes from below
belarus = medal_count.get("Belarus")
print(belarus)



# 11.12.1.7
total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, ...}
chile_golds = total_golds.get("Chile")
print(chile_golds)




# 11.12.1.8
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, ...}
fencing_value = US_medals.get("Fencing")
print(fencing_value)



