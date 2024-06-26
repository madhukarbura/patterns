"""n=int(input("enter the size: "))
for i in range(1,n+1):
    print("*"*i)
*
**
***
    """
"""n=int(input("enter the size"))
for i in range(1,n+1):
    for j in range(1,i):
        
        print(j%2,end="")
    print()
1
10
101
1010    
    """
"""n=int(input("enter the size:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
    *
   **
  ***
 ****
*****
"""
"""n=int(input("enter the size:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i,end="")
    print("*"*(i-1))
    
    *
   ***
  *****
 *******
*********
"""
"""n=int(input("enter the size:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i,end="")
    print("*"*(i-1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i,end="")
    print("*"*(i-1))
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *"""
"""n=int(input("enter the size: "))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    j=1
    while(j<=i):
        print(j,end='')
        j+=1
    for k in range(i-1,0,-1):
        print(k,end='')
    print()
    1
   121
  12321
 1234321
123454321 """
"""
n=int(input("enter the size: "))
m=(n//2)+1
for i in range(1,m+1):
    for j in range(i):
        print(m-j,end="")
    print()
for i in range(m,0,-1):
    for j in range(i-1):
        print(m-j,end="")
    print()"""
"""
n=7
m=(n//2)+1
for i in range(0,m):
    for j in range(i):
        print(i+1,end="")
    print()"""
"""n=int(input("enter the size:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print("*",end=" ")
    print()
   * 
  * * 
 * * * 
* * * * """
"""n=int(input("enter the size:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print("*",end=" ")
        
    print()
    
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * """
"""n=int(input("enter the size:"))
for i in range(n,0,-1):
    print("*"*i,end="")
    print(" "*(n-i),end="")
    print(" "*(n-i),end="")
    print("*"*i)
************
*****  *****
****    ****
***      ***
**        **
*          *"""
"""#pattern 3 circle worsk for only even numbers
def circle(n):
    row=n
    col=n
    for i in range(row):
        for j in range(col):
            if i==j or (i+j)==n-1:
                print(" ",end=" ")
            else: 
                print("*",end=" ")
        print()
n=int(input("enter the size: "))
circle(n)
  * * * * * *   
*   * * * *   * 
* *   * *   * * 
* * *     * * * 
* * *     * * * 
* *   * *   * * 
*   * * * *   * 
  * * * * * *  """
"""def circle(n):
    row=n
    col=n
    for i in range(row):
        for j in range(col):
            if i==j or (i+j)==n-1:
                print(" ",end=" ")
            elif i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print()
n=int(input("enter the size: "))
circle(n)
  * * * * * *   
*             * 
*             * 
*             * 
*             * 
*             * 
*             * 
  * * * * * *"""
"""def circle(n):
    row=n
    col=n
    for i in range(row):
        for j in range(col):
            if i==j or (i+j)==n-1:
                print("*",end=" ")
            elif i==0 or i==n-1 or j==0 or j==n-1:
                print(" ",end=" ")
            else: 
                print("*",end=" ")
        print()
n=int(input("enter the size: "))
circle(n)
*             * 
  * * * * * *   
  * * * * * *   
  * * * * * *   
  * * * * * *   
  * * * * * *   
  * * * * * *   
*             * """
"""def upperTriangular(n):  
    char="a"
    for i in range(1,n+1):
        for j in range(i):
            print(char,end=" ")
            char=chr(ord(char)+1)
            if char>"z":
                char="a"
        print()
n=int(input("enter the size: "))
upperTriangular(n)
a 
b c 
d e f 
g h i j 
k l m n o 
p q r s t u 
v w x y z a b 
c d e f g h i j 
k l m n o p q r s"""
"""def hollow_pyramid(n):
    row = n
    col = 2*n-1
    var=2
    start,end = n-1, n-1
    for i in range(row):
        for j in range(col):
            if (j==start or j==end) and i!=n-1:
                print("*",end="")
            elif i==n-1 and (j>=start and j<=n-1):
                print("*",end=" ")
            else:
                print(" ",end="")
        print()
        start-=1
        end+=1
n=int(input("size:"))
hollow_pyramid(n)
    *    
   * *   
  *   *  
 *     * 
* * * * * """
"""n=int(input())
for i in range(n):
    print((n-i)*" ",end="")
    for j in range(i):
        
        print("*",end="")
    print("\n")"""
"""5
     

    *

   **

  ***

 ****"""
"""def min_maxx(arr,target):
    for i in range(len(arr)-1):
        if arr[i]==target:
            minn=arr[i]-arr[i-1]
            maxx=arr[i+1]-arr[i]
    if minn > maxx:
        tem=minn
        minn=maxx
        maxx=tem
        print("min=",minn,"max=",maxx)
    print("min=",minn,"max=",maxx)
arr=list(map(int,input().split(",")))
target=int(input())
min_maxx(arr,target)"""
"""n=int(input())
for i in range(0,n):
    for k in range(i+1,0,-1):
        print(k,end=" ")
    print()


5
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1"""
"""arr=list(map(int,input().split(",")))
k=int(input())
for i in range(len(arr)-1):
    for j in range(len(arr)-1,i,-1):
        summ=arr[i]+arr[j]
        if summ==k:
            print(i,j)"""
