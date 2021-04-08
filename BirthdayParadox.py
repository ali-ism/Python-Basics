from random import randint

n = 23
nb_groups = 200
dataset = [[randint(1,365) for i in range(n)] for j in range(nb_groups)]

nb_samebday = 0

for data in dataset:
    for elem in data:
        if data.count(elem) > 1:
            nb_samebday += 1
            break
proba = nb_samebday / nb_groups
print(proba)