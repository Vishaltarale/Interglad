from main_model import is_rectangle,Quicksort
import array,numpy as np

obj = is_rectangle(20,20)   #Triangle is rectangle
obj = is_rectangle(40,10)   #Triangle is not rectangle

list=[10,2,98,34,23,43,12]
obj = Quicksort(list)
print("\n Sorted list = ",obj)


#2D array
arr = np.array([[20,10,20,30,67,1],[30,20,40,59,45,67]])
new = np.empty(5)

for i in range(0,len(arr[0])): 
    for j in range(i+1,len(arr[1])):
        if arr[0,i] == arr[1,j]:
            print("common values in both array are : ",arr[0,i])
            
