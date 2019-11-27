#common built-in functions
a = int('123')
b = int(12.34)
c = float('12.34')
d = str(1.23)
e = str(100)
f = bool(1)
g = bool("")#it must be two ""
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
#function name
a = abs#variable a points to function abs
print(a(-1))#Therefore,the"abs" can be called by using "a"
#define functions
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
#you can use the "pass" statement to define a void function, placeholder
#isinstance can check data type
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >=0:
        return x
    else:
        return -x
#keyword arguments
    #you can only input essential arguments when calling this function
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
#you can also input any number of keyword arguments
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job = 'Engineer')
#you can assmble a dictionary and convert it into keyword arguments as inputs
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
#you can certainly simplify the above-mentioned complex function calling
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
#Name keyword arguments
def person(name,age,*,city,job):
    print(name,age,city,job)
#a special character * is required to name a keyword argument
#arguments after * are regarded as naming keyword arguments
person('Jack',24,city='Beijing',job='Engineer')
#The special separator * is not required in the keyword argument after a
#changeable argument in a function
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)
#Because the keyword argument "city" has a default value
#you do not need to input a parameter of "city" for calling
person('Jack',24,job='Engineer')
#Argument combination
#For example, to define a function that includes the above-mentioned arguments:
def f1(a,b,c=0,*args,**kw):
    print('a=')
