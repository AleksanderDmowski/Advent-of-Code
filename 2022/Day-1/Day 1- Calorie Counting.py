
with open('Day 1- Calorie Counting input.txt', mode='r') as data:
    converted_data = data.read().split(2*'\n')
    clear_data = [element.split('\n') for element in converted_data]
    # end_data = [' '.join(element) for element in clear_data]
    end_data = [sum(list(map(int, element))) for element in clear_data]
    print(max(end_data))  # part one
    print(sum(sorted(end_data)[-3:]))  # part two
