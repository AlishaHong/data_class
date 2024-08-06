import numpy as np
import random
arr = np.array([1,10,5,3,4,8,6,2,9])


# 랜덤한 숫자 뽑기
nums = range(1,20)
random_num = random.sample(nums, 10)
random_num_2d = random.sample(nums, 16)
print(random_num)


arr = np.array(random_num)
print(np.sort(arr))
print(np.sort(arr)[::-1])

arr2d = np.array(random_num_2d).reshape(4,4)
print(arr2d)
print(np.sort(arr2d))


#argsort 

#정렬순서대로 인덱스 번호를 출력해준다. 
argsort1 = np.argsort(arr2d, axis= 0)
print(argsort1)


#넘파이 연산

a = np.array([[1,2,3],[2,3,4]])
b = np.array([[3,4],[5,6]])

# ValueError: operands could not be broadcast together with shapes (2,3) (2,
# 연산 브로드캐스팅

print(a*b)
print(np.dot1)
mpy.opt2 = py.dot(a,b)

#브로드캐스팅()
#행렬과 숫자간의 연산은 불가능함 
#그런데 숫자를 행렬로 바꿔주면 가능함 

#
