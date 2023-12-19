from variables1 import stringValue, cutToRight
def cut(string, cutTo, allValue, cutArray=[], valueArray=[]):
    valueArray += [string]

    if not cutTo or not string:
        return allValue, cutArray, valueArray

    cut_value = cutTo.pop(0)

    if cut_value < 0 or cut_value >= len(string):
        return allValue, cutArray, valueArray

    cutted = string[:cut_value]
    string = string[cut_value:]

    cutArray += [cutted]
    if cutTo and cutTo[0] < len(string):
        allValue += len(string)
        return cut(string, cutTo, allValue, cutArray, valueArray)
    else:
        cutArray += [string]
        
        if cutTo and cutTo[0] > len(string):
            allValue += len(string)
            valueArray += [string]
            return allValue, cutArray, valueArray
        
        # valueArray += [string]
        return allValue, cutArray, valueArray


cutToLeft = list(reversed(cutToRight))
print('ToRight:',cutToRight,'\nToLeft:',cutToLeft)

valueRight, cutArrRight, valueArrRight = cut(stringValue, cutToRight, len(stringValue), [],[])
valueLeft, cutArrLeft, valueArrLeft = cut(stringValue, cutToLeft, len(stringValue), [],[])

print('\nTo Right-------')
print("Value:", valueRight)
print("All cuts:", cutArrRight)
print("All values:", valueArrRight)

print('To Left--------')
print("Value:", valueLeft)
print("All cuts:", cutArrLeft)
print("All values:", valueArrLeft)


if (valueRight>valueLeft):
    print("\nResult: To Left win")
else:
    print("\nResult: To Right win")