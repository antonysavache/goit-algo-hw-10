"""
Задача оптимізації виробництва напоїв.
Використовує лінійне програмування для максимізації виробництва двох видів напоїв
з урахуванням обмежених ресурсів.
"""

import pulp

def optimize_production():
    prob = pulp.LpProblem("Beverage_Production_Maximization", pulp.LpMaximize)
    lemonade = pulp.LpVariable("Lemonade", 0, None)  # кількість лимонаду
    fruit_juice = pulp.LpVariable("Fruit_Juice", 0, None)  # кількість фруктового соку
    prob += lemonade + fruit_juice
    prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"  # вода
    prob += lemonade <= 50, "Sugar_Constraint"  # цукор
    prob += lemonade <= 30, "Lemon_Juice_Constraint"  # лимонний сік
    prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"  # фруктове пюре
    prob.solve()

    # Виводимо результати
    print("\nРезультати оптимізації виробництва:")
    print(f"Статус: {pulp.LpStatus[prob.status]}")
    print(f"Кількість лимонаду: {pulp.value(lemonade)}")
    print(f"Кількість фруктового соку: {pulp.value(fruit_juice)}")
    print(f"Загальна кількість напоїв: {pulp.value(prob.objective)}")

    # Виводимо використання ресурсів
    print("\nВикористання ресурсів:")
    print(f"Вода: {2 * pulp.value(lemonade) + pulp.value(fruit_juice)}/100")
    print(f"Цукор: {pulp.value(lemonade)}/50")
    print(f"Лимонний сік: {pulp.value(lemonade)}/30")
    print(f"Фруктове пюре: {2 * pulp.value(fruit_juice)}/40")

    return {
        "lemonade": pulp.value(lemonade),
        "fruit_juice": pulp.value(fruit_juice),
        "total": pulp.value(prob.objective)
    }

if __name__ == "__main__":
    optimize_production()