import csv
import random


def fetch_letters(input, order_number):

    with open('Table ' + str(order_number) + '.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        letters = []
        for row in reader:
            for cell in row:
                letters.append(cell)

        printed_string = ""

        for i in range(8 - input, len(letters), 9):
            if i == -1:
                continue
            if letters[i] == '':
                break
            printed_string += letters[i]

        return printed_string

while True:

    number_int = input("Welcome to Artificial Diversifying. Please enter a 6 digit number sequence, "
                       "numbers ranging from 1 to 9. \n"
                       "If you wish to generate a random poem, press 'r'. \n"
                       "If you wish to end the program, please press 'x'. \n")

    if number_int == "x":
        print("Thank you for versifying!")
        quit()

    if number_int == "r":
        random_number = ""

        for i in range(5):
            random_number += str(random.randint(1, 9))
            i += 1
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
                verse = ""
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

