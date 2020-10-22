with open("text2.txt", "r", encoding="utf-8") as file:
    line_count = 0
    word = 0
    for line in file:
        line_count += 1
        word += len(line.split())
    print(f"Количество строк в файле: {line_count}")
    print(f"Количество слов в файле: {word}")


