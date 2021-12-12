def get_count(filename="input2.txt"):
    with open(filename, 'r') as my_file:
        input_array = my_file.readlines()

    horizontal = 0
    depth = 0
    for line in input_array:
       direction, amount = line.split(" ") 

       if direction == "forward":
           horizontal += int(amount)
       elif direction == "up":
           depth -= int(amount)
       elif direction == "down":
           depth += int(amount)


    return horizontal*depth

print(get_count())       
