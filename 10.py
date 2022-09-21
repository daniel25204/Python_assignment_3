# 10.15.4
file = "travel_plans.txt"
with open(file, 'r') as f:
    num = len(f.read())
print(num)



# 10.15.5
file = "emotion_words.txt"
words = []
with open(file, 'r') as f:
    for line in f:
        words_in_line = line.rstrip().split(' ')
        words += words_in_line

num_words = len(words)
print(num_words)



# 10.15.6
file = "school_prompt.txt"
num_lines = 0
with open(file, 'r') as f:
    for line in f:
        num_lines += 1

print(num_lines)



# 10.15.7
file = "school_prompt.txt"
with open(file, 'r') as f:
    beginning_chars = f.read(30)

print(beginning_chars)



# 10.15.8
file = "school_prompt.txt"
three = []
with open(file, 'r') as f:
    for line in f:
        words = line.rstrip().split(' ')
        three.append(words[2])
print(three)



# 10.15.9
file = "emotion_words.txt"
emotions = []
with open(file, 'r') as f:
    for line in f:
        words = line.rstrip().split(' ')
        emotions.append(words[0])
print(emotions)



# 10.15.10
file = "travel_plans.txt"
with open(file, 'r') as f:
    first_chars = f.read(33)

print(first_chars)



# 10.15.11
file = "school_prompt.txt"
p_words = []
with open(file, 'r') as f:
    for line in f:
        words = line.rstrip().split(" ")
        for word in words:
            if 'p' in word:
                p_words.append(word)
print(p_words)



