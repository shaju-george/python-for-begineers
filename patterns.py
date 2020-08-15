#1
'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

n= int(input(' how many rows / columns you need = '))

for i in range(n) :
    print('*'*10)

#2

1111111111
2222222222
3333333333
4444444444
5555555555
6666666666
7777777777
8888888888
9999999999
10101010101010101010

n= int(input('Enter the limit ='))

for i in range(1,n+1):
    print(str(i)*n)


#3

1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10

n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
  for j in range(n):
    print(i , end=' ')
  print()


#4
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

#5

A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J

n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64) ,end=' ')
    print()


#6

10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8 8 8
7 7 7 7 7 7 7 7 7 7
6 6 6 6 6 6 6 6 6 6
5 5 5 5 5 5 5 5 5 5
4 4 4 4 4 4 4 4 4 4
3 3 3 3 3 3 3 3 3 3
2 2 2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1

n=int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        print(n-i ,end=' ')
    print()


#7

10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1

n=int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        print(n-j ,end=' ')
    print()


  

import snaps

snaps.display_message('hello world')



#8

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *

n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    print('*'* i)

                    
#9

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10

n = int(input('Enter the input'))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()
#10
    
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10
n = int(input('Enter the input'))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

#11
    
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J


n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
 for j in range(1,i+1):
    print(chr(64+i),end=" ")
 print()

#12

A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
A B C D E F G 
A B C D E F G H 
A B C D E F G H I 
A B C D E F G H I J 



n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
 for j in range(1,i+1):
    print(chr(64+j),end=" ")
 print()
