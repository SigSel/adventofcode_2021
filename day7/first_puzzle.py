def main():
    filename = "input7.txt"
    with open(filename, 'r') as f:
        initial_list = list(map(int, f.readline().split(",")))
    best_fuel = None
    best_index = None

    for target in range(min(initial_list), max(initial_list)+1):
        total_fuel = 0
        for element in initial_list:
            total_fuel += abs(element-target)

        if best_index is None:
            best_index, best_fuel = target, total_fuel
        elif best_fuel > total_fuel:
            best_index, best_fuel = target, total_fuel

    print(best_index, best_fuel)


if __name__ == "__main__":
    main()
