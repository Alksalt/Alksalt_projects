def correct_sentence(text):
    text = text.strip()

    if text.endswith("."):
        text = text[:-1]

    if "." in text:
        parts = text.split(".", 1)
        text = parts[0].strip().capitalize() + ". " + parts[1].strip().capitalize() + "."

    elif "," in text:
        parts = text.split(",", 1)
        text = parts[0].strip().capitalize() + ", " + parts[1].strip() + "."

    elif " " in text:
        parts = text.split(" ", 1)
        text = parts[0].strip().capitalize() + ", " + parts[1].strip() + "."


    else:
        text = text.capitalize() + "."

    return text


x = input("gr? ")
print(correct_sentence(x))
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
assert correct_sentence("greetings friends.") == "Greetings, friends.", 'Test6'
print('ОК')