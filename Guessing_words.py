import requests  # This library helps us to download the webpage
from bs4 import BeautifulSoup  # This library helps us to parse the HTML content
import re  # This library helps us to use regular expressions to find words
import random


def get_words_from_url(url):
    # Step 3: Fetch the content of the webpage
    response = requests.get(url)  # Downloads the content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')  # Parses the downloaded content as HTML

    # Step 4: Extract text from the webpage
    text = soup.get_text()  # Gets all the text from the webpage

    # Step 5: Use regex to find words of length 3 to 10 characters
    words = re.findall(r'\b\w{3,10}\b', text)  # Finds all words that are 3 to 10 characters long

    # Step 6: Filter out words that are purely numerical
    words = [word for word in words if word.isalpha()]  # Keeps only the words that are made of letters

    return words  # Returns the list of words

my_url = "https://en.wikipedia.org/wiki/Human"  # URL of a page
words = get_words_from_url(my_url)  # Get the words from the page

words = list(set(words))


computer = random.choice(words).lower()

guessed_letters = []
#update the word
def updated_word(computer, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in computer])

#getting valid letter
def valid_letter():
    while True:
        gamer = input("Choose a letter: ").lower()
        if len(gamer) == 1 and gamer.isalpha():
            return gamer
        else:
            print("Enter a letter to continue ")

#all() = True = all letters in the word
def is_word_guessed(computer, guessed_letters):
    return all(letter in guessed_letters for letter in computer)

#main gameplay
def main():
    while True:
        gamer = valid_letter()
        guessed_letters.append(gamer)
        print("Result: " + updated_word(computer,guessed_letters))

        if gamer not in computer:
            print(f"{gamer} is not in the word. Try again :)")

        if is_word_guessed(computer, guessed_letters):
            print("Congratulations, you guessed the word!")
            break
main()



