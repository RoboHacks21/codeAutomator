testStr = "AS6"

print(testStr)

newNum = int(testStr[-1]) - 1

newStr = testStr[:-1] + str(newNum)

print(newStr)

testStr = "G5"

print(testStr)

newNum = int(testStr[-1]) + 1

newStr = testStr[:-1] + str(newNum)

print(newStr)