def solve(meal_cost, tip_percent, tax_percent):
    if __name__ == '__main__':
        tip_cost = (tip_percent / 100) * meal_cost
        tax_cost = (tax_percent / 100) * meal_cost
        total_meal_cost = meal_cost + tip_cost + tax_cost
        print(round(total_meal_cost))


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)
