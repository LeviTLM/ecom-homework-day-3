my_list = []
for i in range(80, 100):
    my_list.append(i)

print(my_list[0])

print(my_list[-1])

print(len(my_list))

print(my_list[3:13])

print(my_list[3:])

print(my_list[:10])

my_list.insert(len(my_list)//2, 999)
print(my_list)

print(my_list[::-1])

print(my_list[1::2])