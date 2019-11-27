#Create a dictionary
a = {'one':1,'two':2,'three':3}
print(a)
b = dict(one=1,two=2,three=3)
print(b)
c = dict([('one',1),('two',2),('three',3)])
print(c)
d = dict(zip(['one','two','three'],[1,2,3]))
print(d)
e = dict({'one':1,'two':2,'three':3})
print(e)
print(a==b==c==d==e)
#dictcomp build a dictionary from iterated objects that use
#key/value pairs as elements
data = [("John","CEO"),("Nacy","hr"),("LiLei","engineer")]
employee = {name:work for name,work in data}
print(employee)
#Dictionary lookup
#Look up directly according to a key value
print(employee["John"])
#If there is no matched key value in a dictionary, KeyError is returned.
#print(employee["Joh"])
#If you use dic.get(key,default) to look up a key value,
#it will return default if there is no such key value


