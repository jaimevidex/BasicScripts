# Script to count the number of lines in a text file
def count_lines(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"The number of lines in the file is: {num_lines}")
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the path to the file
filepath = input("Enter the complete path to the file: ")
count_lines(filepath)