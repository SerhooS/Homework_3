# Homework_3

#######Task_01
# Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

#######Task_02
# Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

#######Task_03
# Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

#######Task_01

# try:
#     choice = int(input("Оберіть номер дня (1 - 7): "))
#
#     match choice:
#         case 1:
#             print("Понеділок")
#         case 2:
#             print("Вівторок")
#         case 3:
#             print("Середа")
#         case 4:
#             print("Четвер")
#         case 5:
#             print("П'ятниця")
#         case 6:
#             print("Субота")
#         case 7:
#             print("Неділя")
#         case _:
#             raise Exception("Будь-ласка введіть цифру від 1 - 7")
#
# except Exception as e:
#     print(f"Невірний вибір: {e}")
# finally:
#     print("На все добре!")

#######Task_02

# try:
#     # Введення двох чисел від користувача
#     number1= int(input("Введіть перше число: "))
#     number2= int(input("Введіть друге число: "))
#
#     # Порівняння чисел та виведення результату
#     if number1 == number2:
#         print("Числа рівні")
#     else:
#         # Виведення чисел у порядку зростання
#         print("Числа у порядку зростання:")
#         print(min(number1, number2), max(number1, number2))
#
# except ValueError:
#     print("Будь-ласка введіть коректні числа.")

#######Task_03

# try:
#     while True:
#         try:
#             # Введення двох чисел та математичної операції від користувача
#
#             number1 = int(input("Введіть перше число: "))
#             number2 = int(input("Введіть друге число: "))
#             operation = input("Введіть математичну операцію (+, -, *, /)")
#
#             if operation == '+':
#                 print(number1 + number2)
#             elif operation == '-':
#                 print(number1 - number2)
#             elif operation == '*':
#                 print(number1 * number2)
#             elif operation == '/':
#                 print(number1 / number2)
#             else:
#                 raise ValueError("Невідома математична операція.")
#
#         except ValueError as error:
#             print("Введіть тільки цифри!")
#         except ZeroDivisionError as error:
#             print(f"Ділення на нуль неможливе: {error}")
#
# except ValueError as e:
#     print(f"Помилка: {e}")
# except Exception as e:
#     print(f"Виникла невідома помилка: {e}")