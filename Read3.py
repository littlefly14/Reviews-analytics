import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:  #'r'表示讀取模式，'w'表示寫入模式
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
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


good = [d for d in data if 'good' in d]
#第一個d代表若符合條件就把什麼東西裝進去，後面則表條件
print('一共有', len(good), '筆留言提到good')


#文字計數
start_time = time.time()
wc = {}  #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1    #新增key進去wc

for word in wc:
	if wc[word] > 1000000:
	    print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Amber'])

while True:
	word = input('請問你想要查甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過喔!')


print('感謝使用本查詢功能')


bad = ['bad' in d for d in data] #清單裡會裝True 或 false 分析每一筆留言裡是否有bad


