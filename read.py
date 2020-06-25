data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
        
print('The files are read, there are', count, 'data in total')

# calc avg
sum_len = 0
for d in data: # for loop means 把清單中的東西一個一個拿出來
	sum_len += len(d) # sum_len = sum_len + len(d)
	average = sum_len / len(data)
print('The average length of message is', average)

#Extract the information in a list
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'left messages less than 100 letters')
print(new[0])
print(new[1])