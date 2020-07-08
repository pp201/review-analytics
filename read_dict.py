data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
        
print('The files are read, there are', count, 'data in total')

# Dictionary is suitable to count words
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # add a new key into the dictionary
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('which word do you want to check? ')
	if word == 'q':
		break
	elif word in wc:
		print(word, 'is counted', wc[word], 'times')
	else:
		print('Cannot find the word')

print('thank you for using!')









# # calc avg
# sum_len = 0
# for d in data: # for loop means 把清單中的東西一個一個拿出來
# 	sum_len += len(d) # sum_len = sum_len + len(d)
# 	average = sum_len / len(data)
# print('The average length of message is', average)

# # Filter the information from a list
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('There are', len(new), 'left messages less than 100 letters')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d: # if 後面接是非題
# 		good.append(d)
# print('There are', len(good), 'left messages mentioned good')
# print(good[0])



