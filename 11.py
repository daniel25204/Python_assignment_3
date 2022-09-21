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



###############################################################################################



# 11.12.2.1
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for c in Junior.values():
    credits += c
print(credits)




# 11.12.2.2
str1 = "peter piper picked a pack of pickeled peppers"
freq = {}
for char in str1:
    if char not in freq.keys():
        freq[char] = 1
    else:
        freq[char] = freq[char] + 1

print(freq)





# 11.12.2.3
s1 = "hello"
counts = {}
for char in s1:
    if char not in counts.keys():
        counts[char] = 1
    else:
        counts[char] = counts[char] + 1

print(counts)



# 11.12.2.4
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
words = str1.split(' ')
for w in words:
    if w not in freq_words.keys():
        freq_words[w] = 1
    else:
        freq_words[w] = freq_words[w] + 1

print(freq_words)




# 11.12.2.5
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
words = sent.split(' ')
for w in words:
    if w not in wrd_d.keys():
        wrd_d[w] = 1
    else:
        wrd_d[w] = wrd_d[w] + 1

print(wrd_d)




# 11.12.2.6
sally = "sally sells sea shells by the sea shore"
characters = {}
words = sally.split(' ')
for w in words:
    if w not in characters.keys():
        characters[w] = 1
    else:
        characters[w] = characters[w] + 1

best_char = ''
largest_frequency = 0
for char, freq in characters.items():
    if freq > largest_frequency:
        largest_frequency = freq
        best_char = char
    
print(characters)
print(best_char)





# 11.12.2.7
sally = "sally sells sea shells by the sea shore"
characters = {}
words = sally.split(' ')
for w in words:
    if w not in characters.keys():
        characters[w] = 1
    else:
        characters[w] = characters[w] + 1

worst_char = ''
smallest_frequency = max(characters.values())
for char, freq in characters.items():
    if freq < smallest_frequency:
        smallest_frequency = freq
        worst_char = char
    
print(characters)
print(worst_char)




# 11.12.2.8
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}
words = [word.lower() for word in string1.split(' ')]
for w in words:
    if w not in letter_counts.keys():
        letter_counts[w] = 1
    else:
        letter_counts[w] = letter_counts[w] + 1

print(letter_counts)




# 11.12.2.9
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for char in p.lower():
    if char not in low_d.keys():
        low_d[char] = 1
    else:
        low_d[char] = low_d[char] + 1

print(low_d)

