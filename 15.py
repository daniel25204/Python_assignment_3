# 15.7.1
def mult(x, y=6):
    if type(x) == int:
        return x * y
    raise TypeError("The first argument should be an Integer.")

print(mult(4,5))
print(mult(4))
print(mult(4, "G"))
print(mult("s",5))
print(mult("s"))



# 15.7.2
def greeting(name, greeting="Hello", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))



# 15.7.3
def sum(intx, intz=5):
    return intz + intx

print(sum(1,2))
print(sum(1))



# 15.7.4
def test(num, b=True, dict1={2:3, 4:5, 6:8}):
    if b:
        if num in dict1.keys():
            return dict1[num]
    return False

print(test(2))
print(test(1, b=False))



# 15.7.5
def checkingIfIn(fru, direction=True, d={'apple':2, 'pear':1, 'fruit':19, 'orange':5, 'banana':3, 'grapes':2, 'watemelon':7}):
    return direction if fru in d else not direction

print(checkingIfIn("apple"))
print(checkingIfIn("ae"))
print(checkingIfIn("apple", direction=False))
print(checkingIfIn("e", direction=False))




# 15.7.6
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('potatoes')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('potatoes', direction=False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans= checkingIfIn('banana')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('tomatoes', d = {'potatoes': 13, 'tomatoes': 8, 'corns': 5})

print(c_false, c_true, fruit_ans, param_check)


