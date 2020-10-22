file = open("text.txt", "w", encoding="utf-8")
text = input("Введите текст: \n")
while text:
    file.write(f"{text}\n")
    text = input("Введите текст: \n")

file.close()