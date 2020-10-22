with open("text5.txt", "w") as file:
    numbers = input("Введите цифры через пробел: \n")
    file.write(numbers)
with open("text5.txt") as file:
    file_numbs = [int(n) for n in file.readline().split()]
print(sum(file_numbs))

