def popular_words(text, words):
    count_words = {}
    words = [w.lower() for w in words]
    text = text.lower()
    parts = text.split(" ")
    for i in parts:
        if i in words:
                count_words.setdefault(i, 0)
                count_words[i] += 1
    for word in words:
        if word not in count_words:
            count_words.setdefault(word, 0)

    return count_words

#print(popular_words("When I was One I had just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
