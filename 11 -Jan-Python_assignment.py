x=1
y=50
for num in range(x,y+1):
    if num >1 :
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)



n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))

if n1 > n2 and n1 > n3:
    print("first number is greater")
elif n2 > n1 and n2 > n3:
    print("second number is greater")
else:
    print("Third number is greater")




for i in range(1,11):
    print(i)


num = 10
sum = 0
for i in range(1,num+1):
    sum=sum+i
print(sum)



n = 13
for i in range(1,11):
    print(n,'x',i,n*i)


list1 = [10,20,30,40,50]
x=(str(list1[::-1]))
print(x)
print(max(list1))


n=5
for i in range(1,n+1):
    print(i,'square of',i,'is',i*i)
    print(i,"cube of",i,"is",i*i*i)



units=int(input("Enter units "))
bill=0
if units == 100:
    print('Bill is:',units)
elif units > 100 and units < 200:
    print('Bill is',units+(units)*(20/100))
elif units > 200:
    print('Bill is: ',units+(units)*40/100)
else:
    print("Please enter 100 or above")



for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j,end="")
    print("")

    
