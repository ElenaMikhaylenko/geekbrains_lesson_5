NUMBER_TRANSLATE = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}

with open("text4.txt", "r", encoding="utf-8") as file:
    with open("text4_translate.txt", "w", encoding="utf-8") as out:
        for line in file:
            number, *other = line.split()
            number_translated = NUMBER_TRANSLATE[number.lower()]
            out.write(' '.join([number_translated.title(), *other]) + "\n")
