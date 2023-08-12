"""
Question-1:
Lists and Tuples You have been given the following data:

temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

a) Create a new list containing the temperature and day pairs as tuples.
b) Find the maximum temperature from the list and print it along with the corresponding day.
c) Calculate and print the average temperature.
"""

temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(max(temperatures))
print(days[temperatures.index(max(temperatures))])

average = sum(temperatures)/len(temperatures)
print(average)
