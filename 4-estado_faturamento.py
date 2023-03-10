states_earnings = { 'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53 }
total_earnings = 0

for value in states_earnings.values():
    total_earnings += value

for key, value in states_earnings.items():
    print(f'{key} representa {value / total_earnings * 100.0:.2f}% do total de ganhos.')