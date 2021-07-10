data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		sum_len += len(data[count])
		count += 1 # count = count + 1
		#if count % 1000 == 0:
		#	print(len(data))

avg_len = sum_len / len(data) 
print('檔案讀取完成! 總共有', len(data), '筆資料')
print('平均留言長度為：',avg_len)

new = []
new_2 = []
for d in data:
	if len(d) < 100:
		new.append(d)
	elif len(d) < avg_len:
		new_2.append(d)

print('留言長度小於100的留言有', len(new), '筆')
print('留言長度大於100,小於平均值的留言', len(new_2), '筆')
print(new[0])
print('-----------')
print(new_2[0])





