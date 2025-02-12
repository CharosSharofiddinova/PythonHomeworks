#Given a list and a number, create a new list where each element is repeated that number of times.
list_numbers=[4,5,6]
a=2
new_list=[]

for n in list_numbers:
    for _ in range(a):
        new_list.append(n)
print(new_list)      