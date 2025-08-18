# 30/3/2025    LIST

# ln = [11, 32, 13, 8, 27, 41, 23]

# print(ln)
# print(ln[2:5])
# print(ln[::7])
# print(ln[5:7])

# ln.append('Hitesh')
# ln.sort()
# ln.reverse()

# print(ln)




#### Dictionary ####

dict = {'name':'Dipesh','age':'19', 'address':'Aundh', 'education':'Pursuing CA'}
print(dict)
print(dict['name'])           # Accessing the key value pair without using get function
print(dict.get('age'))        # Using Get function
print(dict['education'])

dict['education']='CA'         #Updating an key's value also can be used to add a key and pair value
print('\n',dict)

del dict['address']            #deleting an key value pair
print(dict)

keys = dict.keys()             # Getting all keys in one place
print('\n',keys)

values = dict.values()         # Getting all the values in one place
print('\n',values)

items = dict.items()           # Getting all key value pairs
print('\n',items, '\n')

for key in dict.keys():          #getting keys using .keys() function
    print(key)
print('\n')

for value in dict.values():       #getting values using .values() function
    print(value)
print('\n')

for key, value in dict.items():   #getting keys and values using .items() function
    print(f'{key} : {value}')
print('\n')

#Nested Dictionary
flatmates = {
    'hitesh':{'age':20,'food':'non-veg', 'room':'Hall'},
    'dipesh':{'age':19,'food':'veg', 'room':'Bedroom'},
    'ayush':{'age':18,'food':'cheap', 'room':'Bedroom'},
}

#Iterating over nested dictionaries
for member, member_info in flatmates.items():
    print(f'{member}:{member_info}')
    for key, value in member_info.items():
        print(f'{key}:{value}')
    print('\n')


#Dictionary comprehension
n = int(input("Enter the number until to calculate square: "))
square = {x:x**2 for x in range(1,n+1)}
print(square)

#Condition Dictionary comprehension
n = int(input("\nEnter the number until to calculate square: "))
esquare = {x:x**2 for x in range(1, n+1) if x%2 == 0}
print(esquare)


#Pratical use example
l = [1,1,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5]
frequency = {}

for n in l:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] =1
print(f'\n{frequency}\n')


#Merging two dictionaries
dict1 = {'a':'A', 'b':'B', 'c':'C'}
dict2 = {'A':1, 'B':2, 'c':'3'}
merged_dict = {**dict1, **dict2}
print(merged_dict)