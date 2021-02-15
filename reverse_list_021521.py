#!/usr/bin/python

class longweekend():
  day1="smug test plus wash car plus lubricant garage door"
  day2="go Lowes buy garage door lubricant"
  day3="file tax return"
  extra_day="yes extra day"
  extra_break="yes extra break"

  def __init__(self, whatday, dowhat):
    self.whatday=whatday
    self.dowhat=dowhat
 
  def whether(self, temperature):
    print('During longweekend like ' + self.whatday + ' working on ' + self.dowhat + ' under ' + temperature + ' which is fun ')
 
l1=longweekend('Sat', 'Wash car plus bricant garage door')

print(l1.dowhat)

print(l1.day1)

l1.whether('Raining day')

class longweekend2(longweekend):
  pass

l2=longweekend2('Sun', 'fold clothing')

print(l2.dowhat)

# dict

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

for a in thisdict:
  print(a)


# invert dict

invert={}

for b in thisdict:
  invert[thisdict[b]]=b

print('after inverted becomes ', invert)

for c in invert:
  print(c)

for d in invert:
  print(invert[d])

# adding items in dict

thisdict["Thurs"]="Four"

for e in thisdict.keys():
  print(e)

for f in thisdict.values():
  print(f)

for g, h in thisdict.items():
  print(g, h)

# remove item from dict

thisdict.pop('Tue')

print(thisdict)

# add item

thisdict["Tue"]="Two"

print(thisdict)

# print the length of dict

# python len function

print(len(thisdict))

# python open function

# read method

i=open("items.txt", "r")
print(i.read())

# if else statement

today="Mon"

if today == "Mon":
  print('today is Mon')
else:
  print('today is NOT Mon')


# list 

thatlist=["one", "two", "three"]

for k in thatlist:
  print(k)

# how to append two lists together

l=['A', 'B', 'C']
l.reverse()
print(l)
m=["D", "E", "F"]

for n in m:
  l.append(n)

#print(l)

# how to reverse order of a list using reverse method

#print(l.reverse())
