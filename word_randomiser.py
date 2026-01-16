# Program to randomise words read in from data
# structure held in a binary file
# Author: Stephen C
# 16/01/26

import pickle

def save_file(filename, items):
    with open(filename, 'wb') as output_file:
        pickle.dump(items, output_file)
    print(f'Words have been successfully saved to: {filename}.')

def load_file(filename):
    end_of_file = False

    with open(filename, 'rb') as input_file:

        while not end_of_file:
            try:
                with open(filename, 'rb') as input_file:
                    word_list = pickle.load(input_file)
                    print('File has been loaded successfully.')
                    display_data(word_list)
            except FileNotFoundError:
                print('File has not been found. A new file will be created.')
                return []
            except:
                end_of_file = True

        return word_list

def display_data(items):
    pass

def display_menu():
    print('Main Menu')
    print('1. Add Words')
    print('2. Randomise Words')
    print('3. Shuffle Words')
    print('4. Exit')


def add_words(filename, items):
    again = 'y'

    with open('words_list.dat', 'wb') as output_file:
        while again == 'y':
            save_file(filename, items)

            again = input('\nWould you like to add more words?')


def randomise_words(items):
    pass

def shuffle_words(items):
    pass

def main():
    filename = "words_list.dat"
    items = load_file(filename)

    while True:
        display_menu()
        choice = input('\nWhat would you like to do?')
        if choice == '1':
            add_words(filename, items)
        elif choice == '2':
            randomise_words(items)
        elif choice == '3':
            shuffle_words(items)
        elif choice == '4':
            save_file(filename, items)
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()