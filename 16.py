# 16.9.1
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = ''.join(reversed(sorted([char for char in letters])))
print(sorted_letters)



# 16.9.2
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
print(animals_sorted)



# 16.9.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)
print(alphabetical)



# 16.9.7
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
rev = {}
for k,v in medals.items():
    rev[v] = k

top_three = []
for r in sorted(rev ,reverse=True)[:3]:
    top_three.append(rev[r])
print(top_three)



# 16.9.8
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
rev = {}
for k,v in groceries.items():
    rev[v] = k

most_needed = []
for i in sorted(rev, reverse=True):
    most_needed.append(rev[i])
print(most_needed)




# 16.9.9
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(num):
    return str(num)[-4:]
sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)



# 16.9.10
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=lambda num: str(num)[-4:])
print(sorted_ids)



# 16.9.11
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda w:w[1])
print(lambda_sort)