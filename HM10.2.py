#import re
#def first_word(text):
#    filtered_text = re.findall(r"\b[a-zA-Z']+\b", text)
#    for word in filtered_text:
#        return word

def first_word(text):
    punct = '!"#$%&)(*+,-./:;<=>?@][\\^_`}{|~'
    if "." in text:
        text = text.replace(".", " ")
    elif "," in text:
        text = text.replace(",", " ")
    text = text.strip()
    words = text.split(" ")
    for word in words:
        new_str = "".join(i for i in word if i not in punct)
        if len(new_str) > 1:
            return new_str





print(first_word(".., and so on ..."))
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
