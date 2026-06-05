# Program to randomise words read in from data
# structure held in a binary file
# Author: Stephen C
# 16/01/26

import pickle
import random

# Global constant for menu choices
ADD = 1
REMOVE = 2
RANDOM = 3
SHUFFLE = 4
DISPLAY = 5
EXIT = 6

# Global constant for filename
FILENAME = 'words_list.dat'

def save_file(word_list):
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(word_list, output_file)
    print(f'Words have been successfully saved to: {FILENAME}.')


def load_file():
    try:
        with open(FILENAME, 'rb') as input_file:
            word_list = pickle.load(input_file)
            print('\nFile has been loaded successfully.')
            return word_list
    except FileNotFoundError:
        print('File has not been found. A new file will be created.')
        return []
    except Exception as err:
        print(f'An error occurred while loading the file {err}')

def display_data(word_list):
    for words in word_list:
        print(words)


def remove(word_list):
    # BE CAREFUL, .remove() removes first instance of item in the list
    x = input("What word, words, or phrase would you like to remove?: ")
    try:
        word_list.remove(x)
        print(f'\n{x} has been removed successfully.\n')
    except ValueError:
        print(f'\n{x} has not been found in the list.\n'
              f'Please try again.\n')

def display_menu():
    print('\n\tMain Menu')
    print('--------------------')
    print('1. Add Words')
    print('2. Remove Words')
    print('3. Randomise Words')
    print('4. Shuffle Words')
    print('5. Display Words')
    print('6. Exit')
    print('--------------------\n')

    # Getting user choice
    # print('Choose an option from the menu.')
    choice = int(input('What would you like to do? \n'
                       'Continue by choosing an option from the menu: '))

    # Validating choice
    while choice < ADD or choice > EXIT:
        choice = int(input('Enter a valid choice: '))

    return choice


def add_words(word_list):
    again = 'y'

    while again == 'y' or again == 'Y':
        words = input("Enter the words you would like to add: ")
        word_list.append(words)

        again = input('\nWould you like to add more words? (Enter \'y\' or \'n\'):')
        if again == 'n' or again == 'N':
            save_file(word_list)

    return word_list


def randomise_words(word_list):
    # is creating a new list by choosing a random sample from the original
    split = [item.split(' ')[0] for item in word_list]
    num_words = int(input('\nYou can randomise words from your saved list here. \n'
                          'How many words would you like to randomise?: '))
    random_words = random.choices(split, k = num_words) # will repeat values list
    random_sample = random.sample(split, num_words) # will not repeat values from list
    # generator_expr = (str(element) for element in random_sample)
    separator = ' '
    # print(f"Your randomly generated band name is: ", separator.join(generator_expr))
    # print(f"Band name is: ", separator.join(random_words))
    print(f'\nTry this as your band name: {separator.join(random_sample)}\n')
    print('Try shuffling these words to generate another new band name.\n'
          'Just go to option 4 from the Main Menu.\n')

    # return random_words
    return random_sample

# shuffling random_sample word sequence returned from randomise_words()
# reordering words in list, not returning new list
def shuffle_words(random_sample):
    print('\nShuffling randomised words...')
    separator = ' '
    random.shuffle(random_sample)
    shuffled = separator.join(random_sample)
    print(f'How about this: {shuffled}')


def main():
    items = load_file()

    # Initialising variable for user choice
    choice = 0

    # Processing menu selection until user wants to quit
    while choice != EXIT:
        choice = display_menu()

        if choice == ADD:
            add_words(items)
        elif choice == REMOVE:
            remove(items)
        elif choice == RANDOM:
            random_result = randomise_words(items)
        elif choice == SHUFFLE:
            try:
                shuffle_words(random_result)
            except NameError:
                print('Choose option 3 from the Main Menu and randomise some words before'
                      ' shuffling.')
        elif choice == DISPLAY:
            display_data(items)
        elif choice == EXIT:
            save_file(items)
            break

if __name__ == "__main__":
    main()