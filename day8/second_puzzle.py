def decode_line(line):
    coded_numbers, output_signals = line.split(" | ")
    coded_numbers = coded_numbers.split(" ")
    output_signals = output_signals.split(" ")

    one, four, seven, eight, unknown_numbers = split_numbers(coded_numbers)

    three = find_number(unknown_numbers, seven, 5)
    unknown_numbers.remove(three)

    nine = find_number(unknown_numbers, three, 6)
    unknown_numbers.remove(nine)

    zero = find_number(unknown_numbers, seven, 6)
    unknown_numbers.remove(zero)

    six = find_number(unknown_numbers, "", 6)  # Last number with len == 6
    unknown_numbers.remove(six)

    tmp_filter = remove_from_string(four, one)
    five = find_number(unknown_numbers, tmp_filter, 5)
    unknown_numbers.remove(five)
    two = find_number(unknown_numbers, "", 5)  # Last number with len == 5

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    numbers = sort_strings(numbers)
    output_signals = sort_strings(output_signals)
    decoded_signals = [str(numbers.index(signal)) for signal in output_signals]

    return int(''.join(decoded_signals))


def sort_strings(strings):
    for idx, _ in enumerate(strings):
        strings[idx] = ''.join(sorted(strings[idx]))
    return strings


def find_number(unknown_numbers, known, unknown_length):
    for number in unknown_numbers:
        if len(number) == unknown_length and is_in_string(known, number):
            return number
    raise


def remove_from_string(input_string, to_remove):
    for letter in to_remove:
        input_string = input_string.replace(letter, '')
    return input_string


def split_numbers(numbers):
    one, four, seven, eight = None, None, None, None
    for number in numbers:
        if len(number) == 2:
            one = number
        elif len(number) == 4:
            four = number
        elif len(number) == 3:
            seven = number
        elif len(number) == 7:
            eight = number
        else:
            continue
    try:

        numbers.remove(one), numbers.remove(four), numbers.remove(seven), numbers.remove(eight)
    except ValueError as e:
        print("Something is fishy")
        print(e)

    return one, four, seven, eight, numbers


def is_in_string(known, unknown):
    for letter in known:
        if letter not in unknown:
            return False
    return True


def main():
    filename = "input8.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    total_sum = 0

    for line in lines:
        total_sum += decode_line(line)
    print(total_sum)


if __name__ == "__main__":
    main()
