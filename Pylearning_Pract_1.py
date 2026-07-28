"""
a = "bad is good"
print(type(a))

b = 28
print(type(b))

print(a+" "+str(b))

da = '25-08-2026'

print(da)
"""
"""
# IF else
num=int(input("Please enter the No:"))
if num%2==0 and num!=0:
    print(f"{num} is Even number")
else:
    print(f"{num} is not Even number. it's Odd!")

"""


# For loop
"""
fruit_list = ["apple", "banana", "cheery", "pina apple", "watermelon", "papayya"]

for x in fruit_list:
    print("Fruits to eat list:- ", x)

std_data = "Shiva"

for x in std_data:
    print("string data-",x)

# Break
l = [1, 3, 5, 7, 8, 9,12]

for i in l:
    if i ==7:
        break
    print(i)


# continue
nam = "Shiva"

for i in nam:
    if i =="h":
        continue
    print(i)

# range
for i in range(2,10,2):
    print(i)

for i in range(3):
    print("Chandrashekhara")

# nested loop
team_A = ["Ind", "Pak","Srilanka"]
team_B = ["Aus", "NZ", "SA"]

s = 1
for i in team_A:
    for j in team_B:
        print(s,". ", i, "vs",j)
        s+=1
"""
# while loop
"""
i = 0
while i <7:
    print(i)
    i = i +1

#break
a = 0
while a <=5:
    if a ==4:
        break
    print(a)
    a+=1
# continue

b = 0
while b <8:
    b+=1
    if b==5:
        continue
    print(b)


i = 0
while i<21:
    i+=1
    if i%2==0:
        continue
    print("odd no:-",i)

"""
# list & list methods

"""
lt = [ 1, 2, 4, 3, "Siva", 2, 15 ]
lt.append(51)

lt.append("prasad")

lt.insert(1,10)
lt.remove(2)
lt.pop()
print(lt)
lt.pop(4)
print(lt)

lt_b = [25, 28, 51,3]

lt.extend(lt_b)

print(lt_b)
print(lt)
lt.sort()
print(lt)
# lt.reverse()
# print(lt)
print(lt.index(28))

print(lt.count(3))

print(len(lt))
print(type(lt))

# find largest number
q = [3, 8, 2, 3644, 14, 92, 21, 28, 25,1997, 246 ,-3, -9]
print(max(q)) # inbuilt method
q.sort()
print(q)
print(q[-1])

# with out inbuilt

largest = 0

for i in q:
    if i > largest:
        largest = i
print(largest)

# smaletst

sm = q[-1]
for i in q:
    if i < sm:
        sm =i
print(sm)

print(min(q))

# to interchange the first and last item's
print(q)
q[0],q[-1]=q[-1],q[0]
print(q)

#to swp elements 14 to 246
el_a = q.index(14)
ele_b= q.index(246)
print(el_a)
print(ele_b)
q[el_a], q[ele_b]=q[ele_b], q[el_a]

print(q)

# reverse a list with inbuilt

q.reverse()
print(q)

print(q[::-1])


# reverse a list without inbuilt
r = []
for i in range(len(q)-1,-1,-1):
    r.append(q[i])

print(r)

# find sum of list
s = [1, 4, 7, 3, 2,9, 2, 17, 28]

print(sum(s)) # in built
print(s)

sm = 0
for i in s:
    sm+= i
    print("sum in loop", sm)

avg = sm//len(s)
lth = len(s)
print(f"final sum of list :- {sm} & average is {avg}, no of items in list {lth}")

# print even/odd numbers from list

Noli = [1, 2,3, 4,5, 6, 8]
even = []
for i in Noli:
    if i%2==0:
        print(i)
        even.append(i)

print(even)
odd =[]
for i in Noli:
    if i%2 !=0:
        print(i)
        odd.append(i)
print(odd)


# remove duplicates
duplt = [1,2, 2, 3, 4, 3, 5, 7, 7, 5,6]

nlt= []
for i in duplt:
    if i not in nlt:
        nlt.append(i)
        print(nlt)
print("unique values list :", nlt)

# list comprehension
#square of number
sql =[]
for i in nlt:
    sql.append(i*i)

print(sql)

print([i* i for i in sql])

# filter even no by list comprehension
print(duplt)
print([i for i in duplt if i %2==0])

tx = ["Hello", "siva","prasad"]

print([i.upper() for i in tx])

"""
#tuple
tp_a = ("Shiva", "Keshva" , "ganesh", "Krishna", "Govnda", " Shiva")

print(tp_a)

print("printing the item by index:", tp_a[2])

#tp_a[0]="ganesh"

print("accessing last element :",  tp_a[-1])


tp_a =list(tp_a)

tp_a.append(7)
print("this is the list ,", tp_a)
tp_a = tuple(tp_a)

print("this is the tuple", tp_a)


# we can add tuple to tuple

b = (1, 5, 7, 31.0)
c = (9,6,7,)
print ("before adding the tuple", b)
b+=c
print("after adding tuple to tuple", b)

# delete the tuple
# del b
# print(b)

print(tp_a.count("Shiva"))