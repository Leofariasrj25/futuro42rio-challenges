# Desafio 3 - soma de todo os números

numbers = input("Digite em formato de lista os números a serem somados\n>")
numbers = numbers.replace(" ", "")
sum_of_n = 0

for number in numbers:

    number = int(number)
    sum_of_n += number

print(f"O total da soma dos {len(numbers)} números é {sum_of_n}")
