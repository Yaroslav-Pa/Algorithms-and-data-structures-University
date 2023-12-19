def cut(string, cutTo, all_value, cutArray=[], valueArray=[]):

    valueArray += [string]

    if not cutTo or not string:
        return all_value, cutArray, valueArray

    cut_value = cutTo.pop(0)
    
    if cut_value < 0 or cut_value >= len(string):
        return all_value, cutArray, valueArray

    cutted = string[:cut_value]
    # print("cutted: " + cutted)

    string = string[cut_value:]
    # print("left: `" + string + "`")

    cutArray += [cutted]
    all_value += len(string)
    if cutTo and cutTo[0] < len(string):
        # all_value += len(string)
        return cut(string, cutTo, all_value, cutArray, valueArray)
    else:
        cutArray += [string]
        if cutTo and cutTo[0] > len(string):
            # all_value += len(string)
            valueArray += [string]
            return all_value, cutArray, valueArray
        valueArray += [string]
        # all_value += len(string)
        return all_value, cutArray, valueArray

string_value = "abcdefghij"
cutTo_value = [3, 5]
all_value_result, cuts, allVal = cut(string_value, cutTo_value, len(string_value))
print("Result:", all_value_result)
print("All cuts:", cuts)
print("All values:", allVal)