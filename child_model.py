from main_model import is_rectangle,Quicksort,numpy
import array,numpy as np

obj = is_rectangle(20,20)   #Triangle is rectangle
obj = is_rectangle(40,10)   #Triangle is not rectangle

list=[10,2,98,34,23,43,12]
obj = Quicksort(list)
print("\n Sorted list = ",obj)


list1=[10,29,34,54,32,89]
list2=[30,10,23,34,90,29]
obj = numpy(list1,list2)

