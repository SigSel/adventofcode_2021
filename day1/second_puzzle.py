def get_count(filename="puzzle_input1.txt"):
    with open(filename, 'r') as input_file:
        input_array = input_file.readlines()

    input_array = [int(line) for line in input_array]
    count=0
    
    for idx, line in enumerate(input_array):
        try:
            first_sum = input_array[idx] + input_array[idx+1] + input_array[idx+2]
            second_sum = input_array[idx+1] + input_array[idx+2] + input_array[idx+3]
        except:
            return count
        if second_sum > first_sum:
            count+=1


print(get_count())
