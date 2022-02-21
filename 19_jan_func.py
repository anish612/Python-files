def greet(name):
    print("Hey this is "+name)
greet('Anish Dhiman')
greet('Peter')



def func(country='India'):
    print("Hey i am from " + country)
func()


def func1(fname,lname):
    print(fname+" "+ lname)
func1('Mohit','Guleria')
func1('Rajesh','Dhiman')
func1('Prince','Dhiman')

def add(a,b):
    print(a + b)
add(a=5,b=8)
add(34,65)


def sname(*name):
    print("Surname of Anish is " + name[2])
sname("Kumar","thakur","Dhiman")

def printme(name,age=22):    
    print("My name is",name,"and age is",age)    
printme(name = "Anish") 



def printme(*names):    
    print("type of passed argument is ",type(names))     
    for name in names:    
        print(name)    
printme("Gaurav","David","smith","Peter") 



def plus(*args):
  return sum(args)        #sum function is used to add values
print(plus(10,40,50,70,90))


def my_function(stu1,stu2,stu3):
  print("The topper student is " + stu3)

my_function(stu1 = "Aman", stu2 = "Gurpreet", stu3 = "Ajay")



def prod(a,b,c,):
    return a*b*c
print(prod(6,4,6))



def my_func():
	x = 10
	print("Value inside the function:",x)

x = 20
my_func()
print("Value outside the function:",x)


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry","orange","grapes"]

my_function(fruits)

    


def my_func2(x):
  return 5 * x

print(my_func2(3))
print(my_func2(5))
print(my_func2(9))
