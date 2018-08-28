#Excise 1
import numpy as np
x = np.arange(10,50)
print("x = ", x)

def ndarray_reverse(inputArray):
    reverseArray = np.zeros(inputArray.size)
    print(inputArray.size)
    index = inputArray.size
    while index > 0:
        index -= 1
        reverseArray[inputArray.size - index -1] = inputArray[index]
    return reverseArray

print("Reserve x = ", ndarray_reverse(x))

rand_x = np.random.random(27).reshape(3,3,3)
print("rand_x = ", rand_x)

rand_x = np.random.rand(100).reshape(10,10)
print("minimum in rand_x = ", np.min(rand_x))
print("maximum in rand_x = ", np.max(rand_x))

ones_x = np.ones((3,3))
print("result = ", np.pad(ones_x,(1,1),'constant'))

rand_x = np.random.random(25).reshape(5,5)
base_x = np.full((5,5), np.max(rand_x))
print("normal_x = ", rand_x/base_x)

#Q7
test_x = np.arange(10)
print("test_x = ", test_x)
condiction = (test_x < 3 ) | (test_x >= 8)
print("condiction = ", condiction)

#Q8
test_x = np.array([3,4,6,10,24,89,45,43,46,99,100])
condiction_1 = test_x % 3 != 0
condiction_2 = test_x % 5 == 0
condiction_3 = (test_x % 3 == 0) & (test_x % 5 == 0)
print("In test_x not divisible by 3 :", condiction_1)
print("In test_x divisible by 5 :", condiction_2)
print("In test_x divisible by 3 and divisible by 5 :", condiction_3)

#Q9
rand_x = np.random.random(10)
print("original rand_x = ", rand_x)
rand_x[np.argmax(rand_x)] = 0
print("Replace maximum value with 0 = ",rand_x)

#10
test_x = np.arange(5)
print(np.repeat(test_x,5).reshape(5,5))


