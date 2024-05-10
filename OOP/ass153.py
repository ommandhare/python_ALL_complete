"""
Write a program for doing generic sort.
Read employee file and sort employess using (age, height, weight, salary)
** application of function pointer

"""

from typing import  TypeVar
from employee import Employee as e

T = TypeVar('T')
def genSort(lst:list[T],**kwargs)->list[T]|str:
    if 'key' not in kwargs:
        return "Error sort(iterable,key)"
    keyFun = kwargs['key']
    size = len(lst)
    for i in range(size-1):
        for j in range(size):
            if keyFun(lst[i])< keyFun(lst[j]):
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst

def dataExtract(path):
    empList = []
    with open(path) as f:
        next(f)
        for line in f:
            id,name,age,ht,sal,mId=line.strip().split(',')
            id = int(id)
            age = int(age)
            ht  = float(ht)
            sal = int(sal)
            mId = int(mId)
            emp =e(id,name,age,ht,sal,mId)
            empList.append(emp)
    return empList




path = r'C:\Users\om\PycharmProjects\python_All\OOP\empManager.txt'
data =dataExtract(path)
print("SALARY")
print(genSort(data,key= lambda obj:obj.salary))
print("HEIGHT")
print(genSort(data,key= lambda obj:obj.height))
print("AGE")
print(genSort(data,key= lambda obj:obj.age))