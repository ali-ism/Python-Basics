from random import randint

def list_shuffle(data):
    shuffled_list = []
    lngth = len(data)
    for i in range(lngth):
        j = randint(0, len(data) - 1)
        shuffled_list.append(data.pop(j))
    data.extend(shuffled_list[:])
    del shuffled_list

data_string = input("Enter data separated by spaces: ")
data = data_string.split()
data = [int(i) for i in data]
list_shuffle(data)
print(data)