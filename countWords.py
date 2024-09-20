# Script to count the number of words in a text file
def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
            print(f"The number of words in the file is: {num_words}")
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the path to the file
filepath = input("Enter the complete path to the file: ")
count_words(filepath)