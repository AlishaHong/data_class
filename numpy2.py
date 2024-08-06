import numpy as np

#1. 슬라이싱
temp = range(10)
print(temp)

myList = list(temp)
arr0 = np.array(myList)
print(arr0.shape)

print(arr0[0])
print(arr0[-1])

# 2차원 배열
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])


# print(arr2d[0,2])



#1-2 범위색인

# print(arr0[1:])
# print(arr0[:5])
# print(arr0[:-1])    #[:]는 전체인데 마지막에 -1넣으면 마지막 원소는 포함하지 않는다.and




#2 fancy인덱싱
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])


# print(arr2d[[0,2],:])   #1234  9101112
# print(arr2d[:,2:])

arr = np.array([1,2,3,4,5,6,7,8,9])
# print(arr)


#3. boolean 인덱싱

# print(arr[arr>2])



#[실습]
myArray2d = [[3,1,2,4], 
             [5,6,3,4],
             [2,7,8,9]]
# 5보다 큰 값만 골라서 리스트에 담아보자
array = np.array(myArray2d)
result = array[(array > 5)]
print(f'5보다 큰 숫자 : {result}')




