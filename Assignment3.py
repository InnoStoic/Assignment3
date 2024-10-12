# Student name: Innocent Mohoerane
#Student no: 217499798
#Date: 12/10/2027
#Assignmenr 3: Python

#Problem 1
# Given the string:
s = 'fullstackslp'

#Use indexing to print out the following:

print(s[0])

print(s[-1])

print(s[4:9])

print(s[7:10])

print(s[9:12])

print(s[::-1])
print()

# Problem 2

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'K1':{'k2':'hello'}}
print(d2['K1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
print()

#Problem 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

new_list = set(mylist)
print(new_list)
print()

#Problem 5 - FORMATTING - 5
age = 45
name = "Kyle"

print("Hello my dog's name is {} and he looks {} years old".format(name,age))