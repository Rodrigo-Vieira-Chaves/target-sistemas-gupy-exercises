chosen_number = int(input("Favor informe um número: "))

fibonacci_sequence = [0, 1]

while fibonacci_sequence[-1] <= chosen_number:
    fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])

print(f"O número informado{ '' if chosen_number in fibonacci_sequence else ' NÃO' } pertence à sequência de Fibonacci")
