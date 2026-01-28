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
            print('\nFile has been loaded successfully.\n')
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
    word_list.remove()

def display_menu():
    print('\tMain Menu')
    print('--------------------')
    print('1. Add Words')
    print('2. Remove Words')
    print('3. Randomise Words')
    print('4. Shuffle Words')
    print('5. Display Words')
    print('6. Exit')
    print('--------------------')

    # Getting user choice
    choice = int(input('\nWhat would you like to do? '))

    # Validating choice
    while choice < ADD or choice > EXIT:
        choice = int(input('Enter a valid choice: '))

    return choice


def add_words(word_list):
    again = 'y'

    while again == 'y' or again == 'Y':
        words = input("Enter the words you would like to add: ")
        word_list.append(words)

        again = input('\nWould you like to add more words? ')
        if again == 'n':
            save_file(word_list)

    return word_list


def randomise_words(word_list):
    # is creating a new list by choosing a random sample from the original
    # can work for randomising individual words???
    split = [item.split(' ')[0] for item in word_list]
    random_words = random.choices(split, k=2) # will repeat values list
    random_sample = random.sample(split, 10) # will not repeat values from list
    print(split)
    print(random_words)
    print(random_sample)

def shuffle_words(items):
    # random.shuffle(word_list)
    # print(word_list)
    pass

def main():
    # word_list = []
    # print(type(word_list))
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
            randomise_words(items)
        elif choice == SHUFFLE:
            shuffle_words(items)
        elif choice == DISPLAY:
            display_data(items)
        elif choice == EXIT:
            save_file(items)
            break
        # else:
        #     print('Invalid choice. Please try again.')

    # return word_list

if __name__ == "__main__":
    main()