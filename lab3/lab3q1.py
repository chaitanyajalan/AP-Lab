print("aman poddar 190953172")
def mult(lst):
    mul=1
    for i in range(len(lst)):
        mul*=lst[i]
    return mul
print("enter number of elements")
n=int(input())
print("enter the list of numbers")
l=[]
for i in range(n):
    ele=int(input())
    l.append(ele)
print(mult(l))
