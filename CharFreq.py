import matplotlib as plt
import string

file = open('CharFreq.txt','r')
data = file.read()
file.close()

alphabet = list(string.ascii_lowercase)
data = data.replace(' ','')
letter_freq = [0] * len(alphabet)

for i in range(len(alphabet)):
    letter_freq[i] = data.count(alphabet[i])

plt.pyplot.bar(alphabet,letter_freq)