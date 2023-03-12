print("Я кофейный аппарат")
print("1. Чай - 1 BYN")
print("2. Американо - 2 BYN")
print("3. Латте - 3 BYN")
while (True):
    money = input("Вставьте купюру в купюроприёмник: ")
    if money == '1':
        print("Заберите ваш чай")
    elif money == '2':
        print("Заберите ваш Американо")
    elif money == '3':
        print("Латте")
    elif money == '4':
        break
    else:
        print("Поздравлю, вы потратили деньги просто так :)")
print('Кофейный аппарат выключен')