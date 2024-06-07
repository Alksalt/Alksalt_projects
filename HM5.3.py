str_punct = " !\"#$%&\')(*+,_-./_:;<=>?@\\][^`|}{~"

hashtag = input("Create a hashtag?: ").lower().title()
new_hash = ''
if len(hashtag) > 140:
    print("too long, should be less than 140 symbols")
    hashtag = hashtag[:141]
for i in hashtag:
    if i not in str_punct:
        new_hash += i
print(f"#{new_hash}")


