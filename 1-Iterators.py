myList = [1,2,3,4]

for i in myList:
    print(i, end=' ')

# same thing, i can use any char as lons as it is not a number
for _ in myList:
    print(_, end=' ')


# strings are iterable
myStr = 'Hello'

for i in myStr:
    print(i, end=' ')


# dictionaries are iterable
myDict = {'a': 1, 'b': 2, 'c': 3}

for k,v in myDict.items():
    print(k, v)
    
# cycles through keys only
for k in myDict: # .keys() is not needed
    print(k)
    
# cycles through values only
for v in myDict.values():
    print(v)
    
# for cycle in predetermined range

# 0..4
for i in range(5):
    print(i, end=' ')
    
# 2..4
for i in range(2,5):
    print(i, end=' ')

# 2..4, step 2
for i in range(2,5,2):
    print(i, end=' ')
