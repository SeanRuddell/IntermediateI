# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0]=15

#2
Lname = 'last_name'
students[0][Lname] = 'Bryant'

#3
sports_directory['soccer'][0] = 'Andres'

#4
z[0]['y'] = 30
print(z)

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the 
# function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(name_list):
    for entry in range(len(name_list)):
        dict = name_list[entry] 

        f_name = dict['first_name']
        l_name = dicti['last_name']
        print(f"first_name is {f_name}, last_name is {l_name}")

iterateDictionary(students)

#Create a function iterateDictionary2(key_name, some_list) that ---- given a list of dictionaries and a key name ----
# the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key, name_list):
    for dict in name_list:
        print(dict[key])

print(iterateDictionary2('last_name', students))
print(iterateDictionary2('first_name', students))
