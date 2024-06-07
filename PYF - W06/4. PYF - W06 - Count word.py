
def count_word(text = ''):
    text_list = text.split(' ')
    num_words = {}
    for word in text_list:
        word = word.lower().strip()
        if word in num_words:
            num_words[word] = num_words.get(word) + 1
        else:
            num_words[word] = 1
    print(num_words)

text = "Ngô Văn Đồng, Ngô Thị Như Ý, Ngô Khánh Ngọc, Tăng Huỳnh Ngọc Hiền, Nguyễn Thị Yến Nhi, Ngô Duy Linh"
count_word(text)