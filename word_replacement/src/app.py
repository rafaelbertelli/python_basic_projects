def replace_word():
    str = "Hi guys, i am Rafael, and hi hi hi hi hi hi"
    word_to_replace = input("Enter the word to replace:")
    word_replacement = input("Enter the word to replacement:")
    print(str.replace(word_to_replace, word_replacement))


if __name__ == "__main__":
    replace_word()
