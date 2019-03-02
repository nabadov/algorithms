def getNumbersList(a):
    a = str(a)
    arr = []
    for i in a:
        arr.append(int(i))
    return arr
    
def getCopyCount(a, arr):
    c = 0
    for i in arr:
        if i == a:
            c += 1
    return c
    
def checkNumsEquality(a, b):
    aList = getNumbersList(a)
    bList = getNumbersList(b)
    f = True
    
    for ai in range(len(aList)):
        copyCount = getCopyCount(aList[ai], aList)
        c = 0
        for bi in range(len(bList)):
            if aList[ai] == bList[bi]:
                c += 1
        if c != copyCount:
            f = False
            break
    return f
    
for i in range(100000, 170000):
    f = True
    for k in range(1, 7):
        if(not checkNumsEquality(i, i * k)):
            f = False
            break
    if f:
        print(i)
