data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: 
			print(len(data))
print('檔案讀取完了', '總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	
print('留言的平均長度是', sum_len/len(data), '個字')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100字')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料含有good')
print(good[0])
