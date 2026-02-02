# Find common elements between two lists.

my_list = ['Manish','Radhe','Vivek','Todays_spotlight','Manish']
my_list2 = ['Bhumika','Mahima','Neha','Manish']

common_element = set(my_list).intersection(my_list2) 

print(common_element)
