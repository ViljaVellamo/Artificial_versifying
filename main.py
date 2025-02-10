import csv
import random


def fetch_letters(input, order_number):
    #Each table represents one word in a verse (Table 1 is used to generate the first word, Table 2 the second word etc.)
    with open('Table ' + str(order_number) + '.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        letters = []
        for row in reader:
            for cell in row:
                letters.append(cell)

        printed_string = ""

        #The letters for each word are hidden in the tables, and are indexed by the chosen digit.
        #The first letter is determined by counting 9 minus the given digit (for example, if the digit is 2, the first letter is the 7th in the top row of the table).
        #After that, every 9th letter is added to the word.

        for i in range(8 - input, len(letters), 9):
            if i == -1:
                continue
            if letters[i] == '':
                break
            printed_string += letters[i]

        #The function returns one word for the verse.
        return printed_string

while True:

    number_int = input("Welcome to Artificial Versifying. Please enter a six-digit number sequence, "
                       "numbers ranging from 1 to 9. \n"
                       "If you wish to generate a random poem, press 'r'. \n"
                       "If you wish to end the program, please press 'q'. \n")

    if number_int == "q":
        print("Thank you for versifying!")
        quit()

    if number_int == "r":
        random_number = ""

    # a random six-digit number sequence containing numbers ranging from one to nine is generated
        for i in range(6):
            random_number += str(random.randint(1, 9))
            i += 1

        #The verse is created word by word. Eacg digit in the random_number represents one word in the verse.
        verse = ""
        a = 0
        for char in random_number:
            verse += fetch_letters(int(random_number[a]), a + 1) + " "
            a += 1
        print("The number " + random_number + " produces the following verse:\n" + verse + "\n")
        continue

    if number_int.isdigit():
        if len(str(number_int)) == 6:
            if ("0" not in str(number_int)) & ("-" not in str(number_int)):
                number_string = str(number_int)

                #The verse is created word by word. Eacg digit in the number_string represents one word in the verse.

                verse = ""
                # The variable a represents
                a = 0
                for char in number_string:
                    verse += fetch_letters(int(number_string[a]), a + 1) + " "
                    a += 1
                print("The number " + number_int + " produces the following verse:\n" + verse + "\n")
            else:
                print("The allowed range for numbers is from 1-9. Please enter a valid number sequence to continue.\n")
        else:
            print("Please enter exactly 6 numbers to generate verse.\n")
    else:
        print("Please only use numbers to generate verse.\n")

