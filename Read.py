data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 用來求餘數
			print(len(data))
#利用計數來知道讀取狀態
print(len(data))

print(data[0])