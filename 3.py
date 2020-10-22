with open("text3.txt", "r", encoding="utf-8") as file:
    salaries = []
    for work in file:
        name, salary = work.split()
        salary = float(salary)
        if salary < 20000:
            print(f"Зарплата ниже 20000 рублей: {name} - {salary} руб.")
        salaries.append(salary)
    print(f"Средний оклад: {sum(salaries) / len(salaries)}")



