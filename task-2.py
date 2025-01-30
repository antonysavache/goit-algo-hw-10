"""
Обчислення визначеного інтеграла методом Монте-Карло.
Порівнює результати методу Монте-Карло з аналітичним розв'язком
та візуалізує результати.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def monte_carlo_integration(func, a, b, n=1000000):
    """
    Обчислює визначений інтеграл методом Монте-Карло.

    Args:
        func: Функція для інтегрування
        a: Нижня межа
        b: Верхня межа
        n: Кількість випадкових точок

    Returns:
        float: Значення інтеграла
    """
    x = np.random.uniform(a, b, n)
    y_max = max(func(np.linspace(a, b, 1000)))
    y = np.random.uniform(0, y_max, n)
    points_under = sum(y <= func(x))
    area = (b - a) * y_max * (points_under / n)

    return area

def plot_integration_results(func, a, b, monte_carlo_result, analytical_result):
    """
    Візуалізує результати інтегрування.

    Args:
        func: Функція для інтегрування
        a, b: Межі інтегрування
        monte_carlo_result: Результат методу Монте-Карло
        analytical_result: Аналітичний результат
    """
    x = np.linspace(a-0.5, b+0.5, 1000)
    y = func(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='f(x)')

    x_fill = np.linspace(a, b, 100)
    plt.fill_between(x_fill, func(x_fill), alpha=0.3)

    plt.axvline(x=a, color='r', linestyle='--', label='Межі інтегрування')
    plt.axvline(x=b, color='r', linestyle='--')

    plt.title(f'Інтеграл f(x) від {a} до {b}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    plt.text(0.02, 0.98,
             f'Монте-Карло: {monte_carlo_result:.6f}\n'
             f'Аналітично: {analytical_result:.6f}\n'
             f'Похибка: {abs(monte_carlo_result - analytical_result)/analytical_result*100:.2f}%',
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(facecolor='white', alpha=0.8))

    plt.grid(True)
    plt.show()

def main():
    def f(x): return x**2

    a, b = 0, 2

    mc_result = monte_carlo_integration(f, a, b)

    analytical_result, _ = integrate.quad(f, a, b)

    print("\nРезультати обчислення інтеграла:")
    print(f"Метод Монте-Карло: {mc_result:.6f}")
    print(f"Аналітичний результат: {analytical_result:.6f}")
    print(f"Відносна похибка: {abs(mc_result - analytical_result)/analytical_result*100:.2f}%")

    # Візуалізуємо результати
    plot_integration_results(f, a, b, mc_result, analytical_result)

if __name__ == "__main__":
    main()