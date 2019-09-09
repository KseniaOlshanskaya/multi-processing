class Client:
    def __init__(self, name, phone_number, balance):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        if self.balance < 0:
            self.debt = self.balance
        else:
            self.debt = 0
        self.condition = None
        self.service = True

    def __str__(self):
        s = "Имя: " + self.name + "\n"
        s += "Телефон: " + self.phone_number + "\n"
        s += "Баланс: " + str(self.balance) + "\n"
        if self.balance < 0:
            s += "Сумма задолженности: " + str(self.debt) + " руб." + "\n"
        else:
            s += "Задолженность отсутствует. " + "\n"
        return s

    def __repr__(self):
        return self.__str__()

    def check_balance(self):
        if self.balance > 0:
            return self.__str__() + self.ok()
        elif self.balance < -200:
            return self.__str__() + self.call()
        elif self.balance <= -100:
            return self.__str__() + self.message2()
        elif self.balance == 0:
            return self.__str__() + self.message1()


    def ok(self):
        self.condition = "OK"
        return "\nОповещение: \nПоложительный баланс" + "\n"

    @staticmethod
    def message1():
        message = "\nОповещение: \nУважаемый абонент! На Вашем балансе 0 руб. Пополните счет и оставайтесь на связи!"
        return message + "\n"

    def message2(self):
        self.service = False
        message = "\nОповещение: \nУважаемый абонент! На Вашем балансе меньше -100 руб. " \
                  "Временно приостановлена передача пакета услуг. Пополните баланс и оставайтесь на связи!"
        return message + "\n"

    def call(self):
        self.service = False
        woman_voice = "\nОповещение: \nЗдравствуйте! Вас приветствует Ваш сотовый оператор." \
                " В данный момент на вашем счете " + str(self.debt) + " рублей." \
                "\nВ связи с этим услуги, предоставляемые Вам временно приостановленны." \
                " Пополните счет и оставайтесь на связи!"
        return woman_voice + "\n"

    def debts_txt(self):



class ProcessRunner:
    @staticmethod
    def first_process():
        clients_base = []
        with open("file.txt", "r") as file:
            for i in range(100000):
                c = file.readline().strip()
                phone_number = c[:16]
                name = c[16:-4]
                balance = c[-4:]
                try:
                    balance = int(balance)
                except ValueError:
                    balance = balance[2:]
                    balance = int(balance)
                client = Client(name, phone_number, balance)
                clients_base.append(client)
                client.check_balance()
            print(client)
