data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
        
print('The files are read, there are', count, 'data in total')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
	average = sum_len / len(data)
print('The average length of message is', average)