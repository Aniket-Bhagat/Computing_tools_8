import numpy, re, matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde

file=open('random.txt')
file=file.read()
allWords = re.sub("[^\w]", " ",  file).split() # https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
wordList=['a','it','the','spot','among','income','several']
x=(1,2,3,4,5,6,7)
y=tuple(map(lambda x : allWords.count(x) , wordList))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks(range(1,8))
ax.set_xticklabels(wordList)
plt.title('Length of each word v/s Count')
plt.bar(x,y,align='center')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.show()