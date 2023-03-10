import json
import sys

try:
    file = open('faturamento.json')
except FileNotFoundError:
    print('Arquivo não existe')
    sys.exit()

data = json.load(file)
file.close()

earnings = []
total_earnings = 0

for i in data:
    ammount = i['valor']
    if ammount > 0:
        earnings.append(ammount)
        total_earnings += ammount

earnings_average = total_earnings / len(earnings)
earnings.sort()

print(f'O menor faturamento do mês é de: {earnings[0]}')
print(f'O maior faturamento do mês é de: {earnings[-1]}')
print(f'Em {len(list(filter(lambda earning: earning > earnings_average, earnings)))} dias o faturamento foi maior que a média mensal.')
