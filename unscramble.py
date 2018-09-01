import sys


def create_dictionary(wordList):
    with open("./dictionaries/{}.txt".format(wordList), "r") as f:
        dictionary = f.read()
        dictionary = dictionary.split('\n')
    return dictionary


def main():
    user_input = input("Enter a word to be unscrambled:").upper()
    
    # creates a list of all possible combinations of letters from user_input
    all_words = permutate(user_input)

    final_words = []

    for letter in user_input:
        dictionary = create_dictionary(letter.lower())
        for word in all_words:
            if word[0] == letter:
                for real_word in dictionary:
                    if word == real_word and word not in final_words:
                        final_words.append(word)
        dictionary = []

    print(final_words)


def permutate(w):
    word = w.upper()
    perms = []
    if len(word) <= 1:
        return word

    else:
        for x in permutate(word[1:]):
            if x not in perms:
                perms.append(x)
            for y in range(len(x)+1):
                check = x[:y] + word[0] + x[y:]
                if check not in perms:
                    perms.append(check)
        return perms


if __name__ == "__main__":
    main()
