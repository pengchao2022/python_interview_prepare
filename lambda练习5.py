#排序练习

words = ['apple', 'orange', 'cherry', 'tomato', 'bananer', 'pig', 'kiwi', 'grape']

#按字符串的长度排序
sorted_words = sorted(words, key=lambda s: len(s))

print(sorted_words)

#按照字典的值value排序

score_dict = {'lily':90, 'kate':67, 'tim':22, 'jack':88, 'sisi':99}

# item[0] 是key, item[1]是value
sorted_score = sorted(score_dict.items(), key=lambda item: item[1])

print(sorted_score)

print(score_dict.items())