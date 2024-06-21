import re

def is_palindrome(text):
    text_just_letters = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    reversed_text = text_just_letters[::-1]
    return text_just_letters == reversed_text




assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
