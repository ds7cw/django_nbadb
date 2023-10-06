with open('stats.csv', 'r') as stats_file:
    stats_data = stats_file.readlines()

with open('contracts.csv', 'r') as contracts_file:
    contracts_data = contracts_file.readlines()

contracts_dict = {}

for line in contracts_data:
    k, v = line.strip().split(',')
    contracts_dict[k] = v

stats_list = []

for row in stats_data[1:]:
    player_name = ' '.join(row.split(',')[:2])
    salary = contracts_dict.get(player_name, '0')

    row_and_salary = row.strip() + f',{salary}\n'

    with  open('dataset.txt', 'a') as file:
        file.write(row_and_salary)
