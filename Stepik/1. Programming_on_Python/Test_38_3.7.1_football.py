data = []

count_input = int(input())

for x in range(count_input):
    line = input()
    c = []
    for xx in line.strip().split(';'):
        c.append(xx)
    data.append(c)


def list_of_commands(input_data):
    commands_list = []
    for i in input_data:
        commands_list.append(i[0])
        commands_list.append(i[2])
    commands = set(commands_list)
    return commands


def total_games(input_data):
    all_data = []
    for i in input_data:
        for ii in i:
            all_data.append(ii)
    dictionary = {}
    for i in list_of_commands(input_data):
        dictionary[i] = all_data.count(i)
    return dictionary


def list_of_winners(input_data):
    winners = []
    for i in input_data:
        if i[1] > i[3]:
            winners.append(i[0])
        elif i[1] < i[3]:
            winners.append(i[2])
    return winners


def list_of_losers(input_data):
    losers = []
    for i in input_data:
        if i[1] < i[3]:
            losers.append(i[0])
        elif i[1] > i[3]:
            losers.append(i[2])
    return losers


def list_of_draws(input_data):
    drawn = []
    for i in input_data:
        if i[1] == i[3]:
            drawn.append(i[0])
            drawn.append(i[2])
    return drawn


list_commands = list_of_commands(data)
total_game = total_games(data)
list_of_winner = list_of_winners(data)
list_of_draw = list_of_draws(data)
list_of_loser = list_of_losers(data)

for x in list_commands:
    number_of_games = total_game[x]
    wins = list_of_winner.count(x)
    draw = list_of_draw.count(x)
    lose = list_of_loser.count(x)
    total_points = wins * 3 + draw
    print(x + ':' + str(number_of_games), wins, draw, lose, total_points)
