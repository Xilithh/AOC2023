#part 1

def find_numbers(filename):
    with open(filename, 'r')as file:
        lines = file.readlines()

        final_numbers = []

        for i in lines:
            i = i.strip()
            if i:
                numbers = [char for char in i if char.isdigit()]
                

            if len(numbers) <= 1:
                 final_numbers.append(int(numbers[0]) * 11)
                 
            if len(numbers) >= 2:
                 final_numbers.append(int(numbers[0] + numbers[-1]))
                
    code = sum(final_numbers)

    print(code)
    


file = 'placeholder.txt'

find_numbers(file)



#part 2

word_to_digit = {
'zero':0,
"one":1,
'two':2,
'three':3,
'four':4,
'five':5,
'six':6,
'seven':7,
'eight':8,
'nine':9
}




