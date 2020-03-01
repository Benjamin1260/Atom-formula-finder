xList = []
endList = []
endResult = 1
inputList = []

while True:
    answer = input("Enter your number or to stop, type 'stop'.\n: ")  # Ask answer to:
    if answer != "stop":
        inputList.append(answer)  # 1)add inputted number to inputList.
    else:
        break  # 2)stop the input question and continue.


def primeFactorFinder(number):  # To find the primefactors of input: number and return them in a list.
    aList = []
    pfList = []
    while True:
        divider = number
        while divider > 1:
            if (number / divider) % 1.0 == 0.0 and number % divider == 0:
                aList.append(divider)
                divider -= 1
                continue
            else:
                divider -= 1
                continue
        aList.sort()
        result = aList[0]
        aList = []
        pfList.append(int(result))
        # print(result)
        number /= result
        # print("{}\n".format(number))
        if number == 1:
            break
    return pfList


# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

def adder(aList):  # To add the found primefactors to a list which can be used later.
    while True:
        currentNumber = aList[0]
        count = aList.count(currentNumber)
        aList.remove(currentNumber)
        fCount = endList.count(currentNumber)
        print("{0}\n{1}\n{2}\n".format(currentNumber, count, fCount))
        if count > fCount:
            for i in range(count - fCount):
                endList.append(currentNumber)
        if len(aList) == 0:
            return endList


# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----


for i in inputList:
    pfList = primeFactorFinder(int(i))
    endList = adder(pfList)

for numbers in endList:
    endResult *= numbers

print(endResult)

input("press enter to continue")
