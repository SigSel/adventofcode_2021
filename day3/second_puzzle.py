from first_puzzle import *

def get_count(input_array, cond):

    index_len = len(input_array[0])
    
    for index in range(index_len):
        max_string = number_count(input_array, index, cond)
        input_array = filter_array(input_array, index, max_string)
        if len(input_array) == 1:
           break 
    
    rate = input_array[0].strip("\n")

    return int(rate, 2) 

        

def filter_array(array, index, max_string):
    return [line for line in array if line[index] == max_string]

def main():
    filename="input3.txt"
    with open(filename, 'r') as my_file:
        input_array = my_file.readlines()
    
    ox = get_count(input_array.copy(), "max")
    co2 = get_count(input_array.copy(), "min")


    print(ox*co2)

if __name__ == "__main__":
    main()
