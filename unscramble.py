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
    # take each letter and open up the corresponding dictionary
        dictionary = create_dictionary(letter.lower())
        print(dictionary)
        exit()
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
        for a in permutate(word[1:]):
            if a not in perms:
                perms.append(a)
            for b in range(len(a)+1):
                check = a[:b] + word[0] + a[b:]
                if check not in perms:
                    perms.append(check)
        return perms


if __name__ == "__main__":
    main()
