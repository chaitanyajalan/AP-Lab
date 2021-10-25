m,n=input("Enter m and n for mat 1\n").split()
m1,n1=input("Enter m and n for mat 2 \n").split()
m=int(m)    
n=int(n)
m1=int(m1)
n1=int(n1)
mat1=[]
mat2=[]
if(m==m1 and n==n1):
    print("Enter First Matrix")
    for i in range(0,m):
        row=input()
        frow=row.strip().split(" ")
        mat1.append(frow)
    print("Enter Second Matrix")
    for i in range(0,m1):
        row=input()
        frow=row.strip().split(" ")
        mat2.append(frow)
    print("Matrix 1:")
    for i in range(0,m):
        print (mat1[i])
    print("Matrix 2:")
    for i in range(0,m):
        print(mat2[i])
    print()
    dict1={}
    for i in range(0,m):
        for j in range(0,n):
            if int(mat1[i][j])!=0:
                if (i,j) in dict1:
                   dict1[(i,j)]+=int(mat1[i][j])
                else:
                    dict1[(i,j)]=int(mat1[i][j])
            if int(mat2[i][j])!=0:
                if (i,j) in dict1:
                   dict1[(i,j)]+=int(mat2[i][j])
                else:
                    dict1[(i,j)]=int(mat2[i][j])
                    
    print("Dict : \n:",dict1)

    for i in range(0,m):
        for j in range(0,n):
            if (i,j) in dict1:
                print(str(dict1[(i,j)]),end=" ")
            else:
                print("0", end=" ")
        print()

    
