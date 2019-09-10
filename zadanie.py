import random


with open("file.txt", "w") as file:
    clients_base = []
    list_of_defs = ["875", "840", "826", "898", "971"]
    first_names = ["Иван", "Георгий", "Кирилл", "Дмитрий", "Ефим", "Елена",
                   "Наталья", "Анастасия", "Вероника", "Виктория", "Ксения",
                   "Ольга", "Олеся", "Лилия", "Павел", "Екатерина", "Мария",
                   "Евгений", "Мия", "Станислав", "Надежда", "Максим", "Дамир"]
    last_names = ["Приходько", "Хикс", "Штепа", "Красько", "Блэк", "Уайт",
                    "Эпл", "Абенд", "Вивальди", "Бах", "Игрек", "Сириус",
                    "Нефть", "Попов", "Альба", "Ненси", "Пирс", "Мэнсон", "Кларкс"]
    list_of_phones = []

    for i in range(1000000):
        phone_number = "+7-" + random.choice(list_of_defs) \
                       + "-" + str(random.randint(100, 999)) + "-" \
                       + str(random.randint(10, 99)) + "-" + str(random.randint(10, 99))
        if phone_number not in list_of_phones:
            pass
        else:
            while phone_number in list_of_phones:
                phone_number = "+7-" + random.choice(list_of_defs) \
                               + "-" + str(random.randint(100, 999)) + "-" \
                               + str(random.randint(10, 99)) + "-" + str(random.randint(10, 99))

        name = random.choice(first_names) + " " + random.choice(last_names)
        balance = random.randint(-1000, 1000)
        print(phone_number + " " + name + " " + str(balance), file=file)
