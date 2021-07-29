data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		sum_len += len(data[count])
		count += 1 # count = count + 1
		
avg_len = sum_len / len(data) 
print('檔案讀取完成! 總共有', len(data), '筆資料')
print('平均留言長度為：',avg_len)
print(data[0])

wc = {}	#word_conut
sw = '.:!~-#@$%^&*()+'
for d in data:
	words = d.lower().strip().split()
	for word in words:
		#移除特殊字元
		for s_w in sw:
			if s_w in word:
				word = word.replace(s_w,'')
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
while True:
	word = input('請輸入想查詢的文字：')
	wordlower = word.lower()
	if word == 'qq123':
		print('感謝使用本功能~')
		break
	if wordlower in wc:
		print('"', word, '"出現過', wc[wordlower], '次')
	else:
		print('"', word, '"此文字沒有出現過!')