#1.2.2 Experimental Operation on Lists
x = [1,2,3]
y = [4,5]
x.append(y)
print(x)
#extend
x = [1,2,3]
y = [4,5]
x.extend(y)
print(x)
#equal to
for i in y:
    x.append (i)
    print(x)
#check whther the list is empty
items = list()
if len(items) == 0:
    print("empty list")
if items == []:
    print("empty list")
items2 = []
if len(items2) == 0:
    print("empty list")
if items2 == []:
    print("empty list")
#copy a list
old_list = [1,2,3]
#method one
new_list = old_list[:]
#method two
new_list = list(old_list)
#method three
import copy
new_list = copy.copy(old_list)#copy
new_list = copy.deepcopy(old_list)#deep copy
#Get the last element of a list
a = [1,2,3,4,5,6,7,8,9,10]
print(a[len(a)-1])
print(a[-1])
#sort lists
items = [{'name':'Homer','age':39},
         {'name':'Bart','age':10},
         {"name":'cater','age':20}]
items.sort(key=lambda item:item.get("age"))
print(items)
#remove elements from a list
a = [0,2,2,3]
a.remove(2)
print(a)
#connect two lists
listone = [1,2,3]
listtwo = [4,5,6]
mergelist = listone + listtwo
print(mergelist)
#1.2.3 Experimental Operations on Tuples
t = (1,)
#define a changeable tuple
cn = ('yi','er','san')
en = ('one','two','three')
num = (1,2,3)
tmp = [cn,en,num,[1.1,2.2],'language']
print(tmp)
print(tmp[0])
print(tmp[0][0])
print(tmp[0][0][0])
