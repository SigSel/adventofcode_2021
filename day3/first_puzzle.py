
def get_count(filename="input3.txt"):
    with open(filename, 'r') as my_file:
        input_array = my_file.readlines()

    index_len = len(input_array[0])
    gamma_string = ""
    for index in range(index_len):
        gamma_string += number_count(input_array, index)

    epsilon_string = ''.join(['1' if i == '0' else '0' 
                        for i in gamma_string])
    return  int(gamma_string, 2) * int(epsilon_string, 2)



def number_count(array, index, cond="max"):
    zeros = 0
    ones = 0
    for line in array:
        if line[index] == "0":
            zeros += 1
        elif line[index] == "1":
            ones += 1
        else:
            return ""

    if zeros > ones:
        return "0" if cond == "max" else "1"
    else:
        return "1" if cond == "max" else "0"

def main():
    print(get_count())

if __name__ == "__main__":
    main()
