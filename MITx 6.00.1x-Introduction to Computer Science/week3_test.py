def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    new_tuple = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            new_tuple += (aTup[i],)
    print(new_tuple)


oddTuples(('I', 'am', 'a', 'test', 'tuple'))

listA = [1, 4, 3, 0]
print(listA.sort())

listB = ['x', 'z', 't', 'q']
print(listB.sort())
print(listB.pop())
print(listB.remove("x"))
print(listB)
print(listB.reverse())
print(listB)


cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)

print('cList has object id =', id(cList), 'and contains', cList)
print('cList has object id =', id(dList), 'and contains', dList)

print("'cList == dList' yields the result", cList==dList)
print("'cList is dList' yields the result", cList is dList)


aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList

print('aList has object id =', id(aList), 'and contains', aList)
print('cList has object id =', id(bList), 'and contains', bList)

print("'cList == dList' yields the result", aList==bList)
print("'cList is dList' yields the result", aList is bList)

# https://learning.edx.org/course/course-v1:MITx+6.00.1x+2T2018/block-v1:MITx+6.00.1x+2T2018+type@sequential+block@01df98c1e74a459b8fb20d2d785622cd/block-v1:MITx+6.00.1x+2T2018+type@vertical+block@da207dc7bdd341f6a45710cb97b4ab4c
testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def absoulute(a):
    return abs(a)


applyToEach(testList, absoulute)

print(testList)

# Exercise 2

# Your Code Here
def plusOne(a):
    return a+1


applyToEach(testList, plusOne)

# Exercise 3
# Your Code Here
def square(a):
    return (a**2)


applyToEach(testList, square)


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey']}

animals['d'].append('dog')
animals['d'].append('dingo')
print(animals)

def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    """
    # Your Code Here
    counter = 0
    for value in aDict.values():
        counter += len(value)
    return counter


print(how_many(animals))


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    # Your Code Here
    max_key = None
    max_len = 0
    for key in aDict:
        current_len = len(aDict[key])
        if current_len > max_len:
            max_len = current_len
            max_key = key
    return max_key

print(biggest(animals))

