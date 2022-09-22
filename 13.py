# 13.8.1
olympics = ('Beijing','London','Rio','Tokyo')



# 13.8.2
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ...]
country=[]
for c in tuples_lst:
    country.append(c[1])



# 13.8.3
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp



# 13.8.4
def info(name,gender,age,bday_month,hometown):
    return (name,gender,age,bday_month,hometown)



# 13.8.5
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for country, medal in gold.items():
    num_medals.append(medal)