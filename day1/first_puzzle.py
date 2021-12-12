def get_count(filename="puzzle_input1.txt"):
    with open(filename, 'r') as input_file:
        input_array = input_file.readlines()

    count = 0
    for idx, line in enumerate(input_array):
        if not idx:
            continue
        if int(line) > int(input_array[idx-1]):
            count +=1
    return count

print(get_count())
