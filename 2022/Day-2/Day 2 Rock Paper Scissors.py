
with open('Day 2 Rock Paper Scissors input.txt', mode='r') as data:
    converted_data = data.read().replace('X', 'A').replace(
        'Y', 'B').replace('Z', 'C').split(2*'\n')
    clear_data = [element.split('\n') for element in converted_data][0]
    score = 0
    for element in clear_data:
        if element[-1] == 'A':
            score += 1
        elif element[-1] == 'B':
            score += 2
        elif element[-1] == 'C':
            score += 3
        win = 0
        if element[0] == element[-1]:
            score += 3
        elif (element[-1] == 'A' and element[0] == 'C') or (element[-1] == 'B' and element[0] == 'A') or (element[-1] == 'C' and element[0] == 'B'):
            score += 6
        else:
            score += 0
    print(score)
    strategy = {'A': 'C', 'B': 'A', 'C': 'B'}
    score = 0
    nr = 0
    for element in clear_data:
        s = 0
        pick = ''
        if element[-1] == 'A':  # lose
            pick = strategy.get(element[0])
        elif element[-1] == 'B':  # draw
            pick = element[0]
            score += 3
        elif element[-1] == 'C':  # win
            pick = str([key for key, value in strategy.items() if value ==
                        element[0]])[2]
            s = 6
            score += 6
        if pick == 'A':
            score += 1
        elif pick == 'B':
            score += 2
        elif pick == 'C':
            score += 3
        nr += 1
    print(score)

    # A-rock C-Scissors
    # B-Paper A-rock
    # C-Scissors B-paper
