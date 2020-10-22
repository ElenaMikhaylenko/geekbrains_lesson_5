import json


with open("text7.txt", encoding="utf-8") as file:
    companies_data = {}
    avg_profit = 0
    profitable_companies_count = 0
    for line in file:
        company, company_type, benefit, costs = line.strip().split()
        benefit, costs = float(benefit), float(costs)
        profit = benefit - costs
        companies_data[company] = profit
        if profit > 0:
            profitable_companies_count += 1
            avg_profit += profit
    result = [companies_data, {"average_profit": avg_profit / profitable_companies_count if profitable_companies_count else 0}]
with open("text7_result.txt", "w") as file:
    json.dump(result, file)
