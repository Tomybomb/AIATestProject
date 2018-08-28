#Part 1
print("輸入第一個數字：")
num1 = int(input())
print("輸入第二個數字：")
num2 = int(input())

print(num1, " + ", num2, " = ", num1 + num2)
print(num1, " - ", num2, " = ", num1 - num2)
print(num1, " * ", num2, " = ", num1 * num2)
print(num1, " / ", num2, " = ", num1 / num2)

#Part 2
a_list = [3, 7, 6, 2, 9, 4, 1]
print("The 2nd element = ", a_list[1])
print("The last element = ", a_list[-1])
print("The 3st ~ 5st elements =", a_list[2:5])

test_dict = {"s1":"John", "s2":"Tom", "s3":"Lisa"}
print("test_dict(s2) = ", test_dict["s2"])
test_dict["s4"] = "Mana"
print("Add s4 = ", test_dict)
test_dict.pop("s1")
print("remove John = ", test_dict)


#Part 3-1
passwordStr = "ThomasChiou1018"
print("請輸入密碼：")
testStr = input()
for x in range(len(passwordStr)):
    if len(passwordStr) != len(testStr) or passwordStr[x] != testStr[x]:
        print("密碼錯誤！~~~")
        break

    if x == len(passwordStr)- 1:
        print("密碼正確！")
        break
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for x in test_list:
    sum = sum + x
print("Sum = ", sum)

#Part 3-2
print("請輸入身高(cm)：")
height=int(input())
print("請輸入體重(kg)：")
weight=int(input())
height = height / 100
BMI = weight / (height**2)
if BMI < 18.5:
    print("你太輕了！")
elif BMI>=18.5 and BMI<24:
    print("你是標準身材")
elif BMI>=24 and BMI < 27:
    print("你有一點點重！")
else:
    print("你太重了！")

resultList = [str(x)+'-Fizz' if x%3==0 else str(x)+'-Buzz' if x%5==0 else str(x)+'-FizzBuzz' if x%15==0 else str(x)+'-' for x in range(1,50)]
print("ResultList = ", resultList)

#Part 4
test_list =[1, 2, 3, 4, 5]
def stepProd(souceList):
    prodResult = 1
    for x in test_list:
        prodResult *= x
    return prodResult
print("test_list =", test_list, ", Product = ", stepProd(test_list))

testStr = "ThomasChiou1018"
def reverseStr(sourceStr):
    index = -1
    returnStr = ""
    while index >= -1 * len(sourceStr):
        print(returnStr)
        returnStr += sourceStr[index]
        index -= 1

    return returnStr
print("Orignal String =", testStr, ", ReverseStr = ", reverseStr(testStr))

testSentense = "it is a test string."
tempWordList = testSentense.split(" ")
newResultStr = ""
for x in tempWordList:
    newResultStr += reverseStr(x) + " "

print("Orignal Sentense =", testSentense)
print("ReverseStr = ", newResultStr)


#Part 5
def generate_ArmNum():
    testStartNum = 100
    testStopNum = 300
    resultList = []
    while testStartNum < testStopNum:
        testNumStr = str(testStartNum)
        calcuResult = int(testNumStr[0])**3 + int(testNumStr[1])**3 +int(testNumStr[2])**3
        if calcuResult == testStartNum:
            resultList.append(testStartNum)
        testStartNum +=1
    yield print("100 ~ 300 :",resultList)

    testStartNum = 300
    testStopNum = 600
    resultList = []
    while testStartNum < testStopNum:
        testNumStr = str(testStartNum)
        calcuResult = int(testNumStr[0]) ** 3 + int(testNumStr[1]) ** 3 + int(testNumStr[2]) ** 3
        if calcuResult == testStartNum:
            resultList.append(testStartNum)
        testStartNum += 1
    yield print("300 ~ 600 :", resultList)

    testStartNum = 600
    testStopNum = 999
    resultList = []
    while testStartNum < testStopNum:
        testNumStr = str(testStartNum)
        calcuResult = int(testNumStr[0]) ** 3 + int(testNumStr[1]) ** 3 + int(testNumStr[2]) ** 3
        if calcuResult == testStartNum:
            resultList.append(testStartNum)
        testStartNum += 1
    yield print("600 ~ 999 :", resultList)

    return

for i in generate_ArmNum():
    continue

import os
os.path.abspath("20180310_Ex1.txt")
#os.path.split(os.path.abspath("20180310_Ex1.txt"))
objectFile = open(os.path.abspath("20180310_Ex1.txt"))
#objectFile.read(10240)
resultArticle = objectFile.readlines()
for x in resultArticle:
    print(x)

#Part 6
#Q1
"(abc*)"
#Q2
"(abc[0-9][a-z])"
#Q3
"(cat{2})"
#Q4
"(wa+[z]{3,5}+up)"
#Q5
"(a{2,4}+b{0,4}*c{1,2})"
#Q6
"(0+[0-9][0-9][0-9]+[-]+[0-9][0-9][0-9]+[-]+[0-9][0-9][0-9])"
#Q7
"([0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3})"


#Part 7
class DealwithString():
    def __init__(self, str1 =""):
        self.str1 = str1

    def set_string(self, tmpStr):
        self.str1 = tmpStr

    def print_string(self):
        print("Object Value String = ", self.str1.upper())

testString = DealwithString("ThomasBomb")
testString.print_string()
testString.set_string("newTomybomb")
testString.print_string()
