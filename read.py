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

print('檔案讀取完成! 總共有', len(data), '筆資料')
print('平均留言長度為：',sum_len / len(data))





