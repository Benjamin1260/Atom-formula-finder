xList = []
fList = []
result = 1
inputList = []
while True:
    answer = input("Enter your number or to stop, type 'stop'.\n: ")
    if answer != "stop":
        inputList.append(answer)
    else:
        break


def finder(number):
    xList = []
    aList = []
    scd = []
    while True:
        divider = number
        while divider > 1:
            if (number / divider) % 1.0 == 0.0 and number % divider == 0:
                #print("({0} / {1}) % 1.0 == 0.0 and {0} % {1} == 0".format(number, divider))
                #print((number / divider) % 1.0 == 0.0 and number % divider == 0)
                print(divider)
                aList.append(divider)
                print(aList)
                divider -= 1
                continue
            else:
                divider -= 1
                continue
        aList.sort()
        result = aList[0]
        aList = []
        scd.append(int(result))
        print(result)
        number /= result
        print("{}\n".format(number))
        if number == 1:
            break
    return scd

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

def adder(aList):
    while True:
        number = aList[0]
        count = aList.count(number)
        aList.remove(number)
        fCount = fList.count(number)
        print("{0}\n{1}\n{2}\n".format(number, count, fCount))
        if count > fCount:
            for i in range(count - fCount):
                fList.append(number)
        if len(aList) == 0:
            return fList

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

for i in inputList:
    xList = finder(int(i))
    fList = adder(xList)

#xList = finder(x)
#yList = finder(y)
#fList = adder(xList)
#fList = adder(yList)

#print(fList)
for number in fList:
    result *= number

print(result)

input("press enter to continue")