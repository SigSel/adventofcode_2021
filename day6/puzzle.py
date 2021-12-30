def main():
    filename = "input6.txt"
    with open(filename, 'r') as f:
        initial_list = list(map(int, f.readline().split(",")))
    
    number_of_days = [80, 256]
    for days in number_of_days:
        fish = [initial_list.count(day) for day in range(9)]
        for i in range(days):
            parents_today = fish.pop(0)
            fish[6] += parents_today
            fish.append(parents_today)
        print(sum(fish))


if __name__ == "__main__":
    main()
