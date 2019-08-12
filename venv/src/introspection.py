__author__ = 'Amit Verma'

string_1 = "Hey, I'm a string"
num_1 = 123
my_array = [1,2,3,4,5,6,7]
my_dict = {"Jordan" : "31","Chase" : "26", "Tiffany" : "25"}

if type(string_1) == str:
    print(string_1)

if type(num_1) == int:
    print(num_1)

if type(my_array) == list:
    for i in my_array:
        print(i)

if type(my_dict) == dict:
    for key,value in my_dict.items():
        print(key + ":" + value)

print(id(my_array))