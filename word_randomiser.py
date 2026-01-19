# Program to randomise words read in from data
# structure held in a binary file
# Author: Stephen C
# 16/01/26

import pickle

# Global constant for menu choices
ADD = 1
RANDOM = 2
SHUFFLE = 3
EXIT = 4

# Global constant for filename
FILENAME = 'words_list.dat'

def save_file(items):
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(items, output_file)
    print(f'Words have been successfully saved to: {FILENAME}.')

def load_file():
    try:
        with open(FILENAME, 'rb') as input_file:
            word_list = pickle.load(input_file)
            print('File has been loaded successfully.')
            return word_list
    except FileNotFoundError:
        print('File has not been found. A new file will be created.')
        return []
    except Exception as err:
        print(f'An error occurred while loading the file {err}')


def display_data(items):
    pass

def display_menu():
    print('Main Menu')
    print('1. Add Words')
    print('2. Randomise Words')
    print('3. Shuffle Words')
    print('4. Exit')

    # Getting user choice
    choice = int(input('\nWhat would you like to do? '))

    # Validating choice
    while choice < ADD or choice > EXIT:
        choice = int(input('Enter a valid choice: '))

    return choice


def add_words(items):
    again = 'y'

    with open('words_list.dat', 'wb') as output_file:
        while again == 'y':
            save_file(items)

            again = input('\nWould you like to add more words?')


def randomise_words(items):
    pass

def shuffle_words(items):
    pass

def main():

    items = load_file()

    # Initialising variable for user choice
    choice = 0

    # Processing menu selection until user wants to quit
    while choice != EXIT:
        choice = display_menu()

        if choice == ADD:
            add_words(items)
        elif choice == RANDOM:
            randomise_words(items)
        elif choice == SHUFFLE:
            shuffle_words(items)
        elif choice == EXIT:
            save_file(items)
            break
        # else:
        #     print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()