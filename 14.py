# 14.8.1
def sublist(l):
    if l != None:
        if l == []:
            return []
        ind = 0
        num = l[0]
        sl = []
        while num != 5:
            sl.append(l[ind])
            ind += 1
            num = l[ind]
        return sl
    return None

print(sublist([2,3,6,4,5,11,3]))
print(sublist([5]))
print(sublist([]))
print(sublist([5, 4,24,1]))
print(sublist(None))




# 14.8.2
def check_nums(l):
    if l != None:
        if l == []:
            return []
        ind = 0
        num = l[0]
        sl = []
        while num != 7:
            sl.append(l[ind])
            ind += 1
            num = l[ind]
        return sl
    return None

print(check_nums([2,3,6,4,7,11,3]))
print(check_nums([7]))
print(check_nums([]))
print(check_nums([7, 4,24,1]))
print(check_nums(None))



# 14.8.3
def sublist(l):
    ind = 0
    sl = []
    while ind < len(l):
        if l[ind] == "STOP":
            break
        sl.append(l[ind])
        ind += 1
    return sl

print(sublist(['y','t',4,'STOP', 5]))



# 14.8.4
def stop_at_z(l):
    ind = 0
    sl = []
    while ind < len(l):
        if l[ind] == "z":
            break
        sl.append(l[ind])
        ind += 1
    return sl

print(stop_at_z(['x','g',4,'z', 5]))




# 14.8.5
sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
print(sum1)

sum2 = 0
idx = 0
while idx < len(lst):
    sum2 += lst[idx]
    idx += 1
print(sum2)



# 14.8.6
def beginning(l):
    ind = 0
    sl = []
    while ind < len(l):
        if l[ind] == "bye":
            break
        if len(sl) < 10:
            sl.append(l[ind])
        ind += 1
    return sl

print(beginning(['y','t',4,5,6,1,1111, "4", 6,"FF", 0, 2, "rerq2r", 'bye', 5]))
print(beginning(['y','t', 0, 2, "rerq2r", 'bye', 5]))


