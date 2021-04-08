try:
    nb = str(input("Enter number: "))
    nb = nb.replace(" ","")
    nb_list = list(nb)
    for i in range(len(nb_list)):
        nb_list[i] = int(nb_list[i])
except ValueError:
    raise ValueError("Enter Positive Integer Numbers Only!")

for i in range(0,len(nb_list),2):
    nb_list[i] *= 2
    if nb_list[i] > 9:
        nb_list[i] -= 9

if sum(nb_list) % 10 == 0:
    print("Valid Number")
else:
    print("Invalid Number")