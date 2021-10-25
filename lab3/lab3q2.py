print("aman poddar 190953172")
def converts(lst):
    s=set()
    for i in range(len(lst)):
        s.add(lst[i])
    return s

print("enter size")
n=int(input())
l=[]
print("enter elements in the array")
for i in range(n):
    ele=int(input())
    l.append(ele)
print(converts(l))
    
        
