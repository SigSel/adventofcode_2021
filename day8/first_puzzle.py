def main():
    filename = "input8.txt"
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_segments = [segment for idx, segment in enumerate(segments) if idx in [1, 4, 7, 8]]
    regular_segments = [segment for idx, segment in enumerate(segments) if idx in [0, 2, 3, 5, 6, 9]]
    number_of_unique = 0

    for element in lines:
        _, output_signals = element.split(" | ")
        signals = output_signals.split(" ")
        uniques = [signal for signal in signals if len(signal) in unique_segments]
        number_of_unique += len(uniques)
    print(number_of_unique)


if __name__ == "__main__":
    main()

