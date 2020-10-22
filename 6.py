def calculate_hours(hours):
    result = 0
    for hour in hours:
        if hour == "—":
            continue
        result += int(hour.split("(")[0])
    return result


with open("text6.txt", encoding="utf-8") as file:
    result = {}
    for line in file:
        subject, *hours = line.strip().split()
        result[subject] = calculate_hours(hours)
    print(result)
