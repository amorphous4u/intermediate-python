__author__ = 'Amit Verma'

my_array = [1,2,3,4,5,6,7]
zip_dictionary = {'Jordan': '21413', 'Tifany': '12413242', 'Chase':'13123'}

# for i in zip_dictionary.values():
#     print(i)

it = iter(zip_dictionary.values())
print(next(it))
print(next(it))
print(next(it))
print(next(it))