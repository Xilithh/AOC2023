import numbers

def find_numbers(filename):
    with open(filename, 'r')as file:
        lines = file.readlines()

        final_numbers = []

        for i in lines:
            i = i.strip()
            if i:
                numbers = [char for char in i if char.isdigit()]
                print(numbers)




file = 'Insert File Name Here'

find_numbers(file)



