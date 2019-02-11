import matplotlib.pyplot as plt

file=open("Sequence.txt")
file=file.read().splitlines()
seq=''.join(file[1:])

A,C,G,T=tuple(map(lambda x:float(seq.count(x))/float(len(seq))*100 , ['A','C','G','T']))

plt.figure(figsize=(10,10))
labels = 'Adenine', 'Cytocine', 'Gaunine', 'Thimine'
sizes = [A,C,G,T]
plt.title('Pie plot')
plt.pie(sizes,labels=labels,autopct='%1.2f%%',shadow=True)
plt.show()