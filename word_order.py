from collections import OrderedDict
words = OrderedDict()
i = input()
for j in range(0,i,1):
    word = raw_input()
    if word in words:
        words[word]+=1
        continue
    else:
        words.update({word:1})
print(len(words))
for i,j in words.items():
    print(j),