

import numpy as np

a = np.array([1,2,3], dtype=int)
print(a)

#파이썬의 리스트는 다양한 데이터 타입을 넣을 수 있지만
#넘파이의 배열에는 한가지 타입의 데이터만 넣을 수 있다.

b = np.array([1.,2,3,4])    #[1.,2.,3.,4.]
print(b)

# 1.을 정수로 바꾸면 데이터 손실이 일어나기 때문에 나머지 정수를 모두 실수로 변경한다.


#리스트로부터 생성

#1차원 리스트
myList = [1,2,3,4]

#2차원 리스트
myList2 = [[1,2,3,4],[5,6,7,8]]

arr1 = np.array(myList)
arr2 = np.array(myList2)
print(arr1)
print(arr2)

