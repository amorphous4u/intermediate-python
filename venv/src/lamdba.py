__author__ = 'Amit Vermaa'

# def fahrenheit(temp):
#     return((float(9)/5) * temp + 32)
#
# celsius_temperatures = (36.5, 37, 35, 33)
#
# f = map(fahrenheit, celsius_temperatures)
#
# for t in f:
#     print(t)

celsius_temperatures = (36.5, 37, 35, 33)

fahrenheit = map(lambda x : (float(9)/5) *x + 32, celsius_temperatures)

for t in fahrenheit:
    print(t)