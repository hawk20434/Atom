import random

print("Добро пожаловать в Атом-Инвест!")
listakt = []  # список активов
ballanse = 0  # общий  баланс счета
artivy = 0  # сумма активов
komissi = 0  # общая сумма комиссии
stavka = 0.0007  # процент от сделки


class stocks:
    # Класс акций
    def __init__(self, name, price, sector):
        self.name = name
        self.price = price
        self.sector = sector

    def showInfo(self):
        print("Наименование: ", self.name)
        print("Цена: ", self.price)
        print("Сектор экономики: ", self.sector)
        print("-------------------")


Apple = stocks("Apple", 182, "Информационные технологии")
Nike = stocks("Nike", 122, "Потребительские товары и услуги")
Pfizer = stocks("Pfizer", 54, "Здравоохранение")
Google = stocks("Google", 312, "Информационные технологии")
Fox = stocks("Fox", 98, "Потребительские товары и услуги")
Tesla = stocks("Tesla", 412, "Потребительские товары и услуги")
Visa = stocks("Visa", 156, "Финансовый сектор")
Walmart = stocks("Walmart", 296, "Потребительские товары и услуги")
Uber = stocks("Uber", 41, "Транспорт и машиностроение")
FedEx = stocks("FedEx", 212, "Потребительские товары и услуги")

class bonds:
    # класс облигаций
    def __init__(self, name, price, coupon):
        self.name = name
        self.price = price
        self.coupon = coupon

    def showInfo(self):
        print("Наименование: ", self.name)
        print("Цена: ", self.price)
        print("Доходность: ", self.coupon)
        print("-------------------")


OFZ_1 = bonds("ОФЗ-1", 12, "2%")
OFZ_2 = bonds("ОФЗ-2", 8, "3%")
OFZ_3 = bonds("ОФЗ-3", 9, "4%")
OFZ_4 = bonds("ОФЗ-4", 15, "2%")
OFZ_5 = bonds("ОФЗ-5", 11, "1%")


class fonds:
    # класс фондов
    def __init__(self, name, price, country, dicription):
        self.name = name
        self.price = price
        self.dicription = dicription
        self.country = country

    def showInfo(self):
        print("Наименование: ", self.name)
        print("Цена: ", self.price)
        print("Географическое положение: ", self.country)
        print("Описание фонда: ", self.dicription)
        print("-------------------")


Fxus = fonds("FXUS", 19, "Америка", "FXUS – простой инструмент инвестирования в крупнейшие компании Америки разом.")
Etf = fonds("ETF", 25, "Америка", "ETF – индексный фонд на 500 крупнейших американских компаний.")
Imoex = fonds("IMOEX", 16, "Россия", "IMOEX – индексный фонд на компания из России с максимальной капитализацей.")


def get_cash():  # функция ввода средств
    while True:
        try:
            global ballanse
            ballanse = int(input("Введите денежные средства: "))
            if ballanse < 0:
                print("Сумма не может быть 0")
                cash = get_cash()
            else:
                return ballanse
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


cash = get_cash()
print(f"Сумма {cash} долларов. зарегистрировано!")
print("-------------------")


def getdop_cash():  # функция ввода дополнительный средств
    while True:
        try:
            global ballanse
            dop = int(input("Введите денежные средства: "))
            if dop < 0:
                print("Сумма не может быть 0")
                getdop = getdop_cash()
            else:
                ballanse = ballanse + dop
                print(f"Сумма {dop} долларов. зарегистрирована!")
                print("-------------------")
                return ballanse
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def out_cash():  # функция вывода средств
    global ballanse
    out = int(input("Введите денежные средства: "))
    if out > 0 and out < ballanse:
        ballanse = ballanse - out
        print(f"Сумма {out} долларов. зарегистрирована!")
        print("-------------------")
        return ballanse
    else:
        print("Некоректная сумма")
        out = out_cash()

def get_listakt():  # функция отображение активов
    chose = input("Выберете что хотите посмотреть: Акции,Облигации, Фонды:")
    print("-------------------")
    if chose == "Акции":
        Apple.showInfo()
        Nike.showInfo()
        Pfizer.showInfo()
        Google.showInfo()
        Fox.showInfo()
        Tesla.showInfo()
        Visa.showInfo()
        Walmart.showInfo()
        Uber.showInfo()
        FedEx.showInfo()
    elif chose == "Облигации":
        OFZ_1.showInfo()
        OFZ_2.showInfo()
        OFZ_3.showInfo()
        OFZ_4.showInfo()
        OFZ_5.showInfo()
    elif chose == "Фонды":
        Fxus.showInfo()
        Etf.showInfo()
        Imoex.showInfo()
    else:
        print("Вы ввели не слово. Повторите ввод")
        Getlist = get_listakt()

def predloz():  # функция предложения просмотра активов
    while True:
        try:
            chose = input("Желатете посмотреть предложения биржы?(Да\Нет) ")
            if chose == "Да":
                Getlist = get_listakt()
            elif chose == "Нет":
                break
        except ValueError:
            print("Вы ввели неправильный символ. Повторите ввод")


predlog = predloz()


def buy_funct():  # функция покупки активов
    chbuy = input("Выберете что хотите купить: Акции,Облигации, Фонды:")
    print("-------------------")
    global ballanse
    global artivy
    global komissi
    if chbuy == "Акции":
        Apple.showInfo()
        Nike.showInfo()
        Pfizer.showInfo()
        Google.showInfo()
        Fox.showInfo()
        Tesla.showInfo()
        Visa.showInfo()
        Walmart.showInfo()
        Uber.showInfo()
        FedEx.showInfo()
        buy = input("Сделайте выбор и напишите название: ")
        if buy == "Apple" and ballanse > Apple.price:
            ballanse = ballanse - Apple.price - (Apple.price * stavka)
            listakt.append("Apple")
            artivy = artivy + Apple.price
            komissi = komissi + Apple.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Apple.price * stavka)
            return komissi
        elif buy == "Nike" and ballanse > Nike.price:
            ballanse = ballanse - Nike.price - (Nike.price * stavka)
            listakt.append("Nike")
            artivy = artivy + Nike.price
            komissi = komissi + Nike.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Nike.price * stavka)
            return komissi
        elif buy == "Pfizer" and ballanse > Pfizer.price:
            ballanse = ballanse - Pfizer.price - (Pfizer.price * stavka)
            listakt.append("Pfizer")
            artivy = artivy + Pfizer.price
            komissi = komissi + Pfizer.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Pfizer.price * stavka)
            return komissi
        elif buy == "Google" and ballanse > Google.price:
            ballanse = ballanse - Google.price - (Google.price * stavka)
            listakt.append("Google")
            artivy = artivy + Google.price
            komissi = komissi + Google.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Google.price * stavka)
            return komissi
        elif buy == "Fox" and ballanse > Fox.price:
            ballanse = ballanse - Fox.price - (Fox.price * stavka)
            listakt.append("Fox")
            artivy = artivy + Fox.price
            komissi = komissi + Fox.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Fox.price * stavka)
            return komissi
        elif buy == "Tesla" and ballanse > Tesla.price:
            ballanse = ballanse - Tesla.price - (Tesla.price * stavka)
            listakt.append("Tesla")
            artivy = artivy + Tesla.price
            komissi = komissi + Tesla.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Tesla.price * stavka)
            return komissi
        elif buy == "Visa" and ballanse > Visa.price:
            ballanse = ballanse - Visa.price - (Visa.price * stavka)
            listakt.append("Visa")
            artivy = artivy + Visa.price
            komissi = komissi + Visa.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Visa.price * stavka)
            return komissi
        elif buy == "Walmart" and ballanse > Walmart.price:
            ballanse = ballanse - Walmart.price - (Walmart.price * stavka)
            listakt.append("Walmart")
            artivy = artivy + Walmart.price
            komissi = komissi + Walmart.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Walmart.price * stavka)
            return komissi
        elif buy == "Uber" and ballanse > Uber.price:
            ballanse = ballanse - Uber.price - (Uber.price * stavka)
            listakt.append("Uber")
            artivy = artivy + Uber.price
            komissi = komissi + Uber.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Uber.price * stavka)
            return komissi
        elif buy == "FedEx" and ballanse > FedEx.price:
            ballanse = ballanse - FedEx.price - (FedEx.price * stavka)
            listakt.append("FedEx")
            artivy = artivy + FedEx.price
            komissi = komissi + FedEx.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", FedEx.price * stavka)
            return komissi
        else:
            print("Вы неправильно ввели слово или у вас недостаточно средств на счете.")
            buyfunct = buy_funct()
    elif chbuy == "Облигации":
        OFZ_1.showInfo()
        OFZ_2.showInfo()
        OFZ_3.showInfo()
        OFZ_4.showInfo()
        OFZ_5.showInfo()
        buy = input("Сделайте выбор и напишите название: ")
        if buy == "ОФЗ-1" and ballanse > OFZ_1.price:
            ballanse = ballanse - OFZ_1.price - (OFZ_1.price * stavka)
            listakt.append("OFZ_1")
            artivy = artivy + OFZ_1.price
            komissi = komissi + OFZ_1.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", OFZ_1.price * stavka)
            return komissi
        elif buy == "ОФЗ-2" and ballanse > OFZ_2.price:
            ballanse = ballanse - OFZ_2.price - (OFZ_2.price * stavka)
            listakt.append("OFZ_2")
            artivy = artivy + OFZ_2.price
            komissi = komissi + OFZ_2.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", OFZ_2.price * stavka)
            return komissi
        elif buy == "ОФЗ-3" and ballanse > OFZ_3.price:
            ballanse = ballanse - OFZ_3.price - (OFZ_3.price * stavka)
            listakt.append("OFZ_3")
            artivy = artivy + OFZ_3.price
            komissi = komissi + OFZ_3.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", OFZ_3.price * stavka)
            return komissi
        elif buy == "ОФЗ-4" and ballanse > OFZ_4.price:
            ballanse = ballanse - OFZ_4.price - (OFZ_4.price * stavka)
            listakt.append("OFZ_4")
            artivy = artivy + OFZ_4.price
            komissi = komissi + OFZ_4.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", OFZ_4.price * stavka)
            return komissi
        elif buy == "ОФЗ-5" and ballanse > OFZ_5.price:
            ballanse = ballanse - OFZ_5.price - (OFZ_5.price * stavka)
            listakt.append("OFZ_5")
            artivy = artivy + OFZ_5.price
            komissi = komissi + OFZ_5.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", OFZ_5.price * stavka)
            return komissi
        else:
            print("Вы неправильно ввели слово или у вас недостаточно средств на счете.")
            buyfunct = buy_funct()
    elif chbuy == "Фонды":
        Fxus.showInfo()
        Etf.showInfo()
        Imoex.showInfo()
        buy = input("Сделайте выбор и напишите название: ")
        if buy == "FXUS" and ballanse > Fxus.price:
            ballanse = ballanse - Fxus.price - (Fxus.price * stavka)
            listakt.append("Fxus")
            artivy = artivy + Fxus.price
            komissi = komissi + Fxus.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Fxus.price * stavka)
            return komissi
        elif buy == "ETF" and ballanse > Etf.price:
            ballanse = ballanse - Etf.price - (Etf.price * stavka)
            listakt.append("Etf")
            artivy = artivy + Etf.price
            komissi = komissi + Etf.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Etf.price * stavka)
            return komissi
        elif buy == "IMOEX" and ballanse > Imoex.price:
            ballanse = ballanse - Imoex.price - (Imoex.price * stavka)
            listakt.append("Imoex")
            artivy = artivy + Imoex.price
            komissi = komissi + Imoex.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Imoex.price * stavka)
            return komissi
        else:
            print("Вы ввели не слово. Повторите ввод")
            buyfunct = buy_funct()


def sell_funct():  # функция продажи активов
    chsell = input("Выберете что хотите продать: Акции, Облигации, Фонды:")
    print("-------------------")
    global ballanse
    global artivy
    global listakt
    global komissi
    if chsell == "Акции":
        print("Ваши текущие активы:", listakt)
        sell = input("Сделайте выбор и напишите название: ")
        if sell == "Apple":
            ballanse = ballanse + Apple.price - (Apple.price * stavka)
            listakt.remove("Apple")
            artivy = artivy - Apple.price
            komissi = komissi + Apple.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "Apple")
            print("Комиссия брокера:", Apple.price * stavka)
            return komissi
        elif sell == "Nike":
            ballanse = ballanse + Nike.price - (Nike.price * stavka)
            listakt.remove("Nike")
            artivy = artivy - Nike.price
            komissi = komissi + Nike.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "Nike")
            print("Комиссия брокера:", Nike.price * stavka)
            return komissi
        elif sell == "Pfizer":
            ballanse = ballanse + Pfizer.price - (Pfizer.price * stavka)
            listakt.remove("Pfizer")
            artivy = artivy - Pfizer.price
            komissi = komissi + Pfizer.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "Pfizer")
            print("Комиссия брокера:", Pfizer.price * stavka)
            return komissi
        elif sell == "Google":
            ballanse = ballanse + Google.price - (Google.price * stavka)
            listakt.remove("Google")
            artivy = artivy - Google.price
            komissi = komissi + Google.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "Google")
            print("Комиссия брокера:", Google.price * stavka)
            return komissi
        elif sell == "Fox":
            ballanse = ballanse + Fox.price - (Fox.price * stavka)
            listakt.remove("Fox")
            artivy = artivy - Fox.price
            komissi = komissi + Fox.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "Fox")
            print("Комиссия брокера:", Fox.price * stavka)
            return komissi
        elif sell == "Tesla":
            ballanse = ballanse + Tesla.price - (Tesla.price * stavka)
            listakt.remove("Tesla")
            artivy = artivy - Tesla.price
            komissi = komissi + Tesla.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Tesla.price * stavka)
            return komissi
        elif sell == "Visa":
            ballanse = ballanse + Visa.price - (Visa.price * stavka)
            listakt.remove("Visa")
            artivy = artivy - Visa.price
            komissi = komissi + Visa.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Visa.price * stavka)
            return komissi
        elif sell == "Walmart":
            ballanse = ballanse + Walmart.price - (Walmart.price * stavka)
            listakt.remove("Walmart")
            artivy = artivy - Walmart.price
            komissi = komissi + Walmart.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Walmart.price * stavka)
            return komissi
        elif sell == "Uber":
            ballanse = ballanse + Uber.price - (Uber.price * stavka)
            listakt.remove("Uber")
            artivy = artivy - Uber.price
            komissi = komissi + Uber.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", Uber.price * stavka)
            return komissi
        elif sell == "FedEx":
            ballanse = ballanse + FedEx.price - (FedEx.price * stavka)
            listakt.remove("FedEx")
            artivy = artivy - FedEx.price
            komissi = komissi + FedEx.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Приобретенный актив:", listakt)
            print("Комиссия брокера:", FedEx.price * stavka)
            return komissi
        else:
            print("Вы неправильно ввели слово или у вас недостаточно средств на счете.")
            sellfunct = sell_funct()
    elif chsell == "Облигации":
        print("Ваши текущие активы:", listakt)
        sell = input("Сделайте выбор и напишите название: ")
        if sell == "ОФЗ-1":
            ballanse = ballanse + OFZ_1.price - (OFZ_1.price * stavka)
            listakt.remove("OFZ_1")
            artivy = artivy - OFZ_1.price
            komissi = komissi + OFZ_1.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "OFZ_1")
            print("Комиссия брокера:", OFZ_1.price * stavka)
            return komissi
        elif sell == "ОФЗ-2":
            ballanse = ballanse + OFZ_2.price - (OFZ_2.price * stavka)
            listakt.remove("OFZ_2")
            artivy = artivy - OFZ_2.price
            komissi = komissi + OFZ_2.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "OFZ_2")
            print("Комиссия брокера:", OFZ_2.price * stavka)
            return komissi
        elif sell == "ОФЗ-3":
            ballanse = ballanse + OFZ_3.price - (OFZ_3.price * stavka)
            listakt.remove("OFZ_3")
            artivy = artivy - OFZ_3.price
            komissi = komissi + OFZ_3.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "OFZ_3")
            print("Комиссия брокера:", OFZ_3.price * stavka)
            return komissi
        elif sell == "ОФЗ-4":
            ballanse = ballanse + OFZ_4.price - (OFZ_4.price * stavka)
            listakt.remove("OFZ_4")
            artivy = artivy - OFZ_4.price
            komissi = komissi + OFZ_4.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "OFZ_4")
            print("Комиссия брокера:", OFZ_4.price * stavka)
            return komissi
        elif sell == "ОФЗ-5":
            ballanse = ballanse + OFZ_5.price - (OFZ_5.price * stavka)
            listakt.remove("OFZ_5")
            artivy = artivy - OFZ_5.price
            komissi = komissi + OFZ_5.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", "OFZ_5")
            print("Комиссия брокера:", OFZ_5.price * stavka)
            return komissi
        else:
            print("Вы неправильно ввели слово или у вас недостаточно средств на счете.")
            sellfunct = sell_funct()
    elif chsell == "Фонды":
        print("Ваши текущие активы:", listakt)
        sell = input("Сделайте выбор и напишите название: ")
        if sell == "Fxus":
            ballanse = ballanse + Fxus.price - (Fxus.price * stavka)
            listakt.remove("Fxus")
            artivy = artivy - Fxus.price
            komissi = komissi + Fxus.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", listakt)
            print("Комиссия брокера:", Fxus.price * stavka)
            return komissi
        elif sell == "Etf":
            ballanse = ballanse + Etf.price - (Etf.price * stavka)
            listakt.remove("Etf")
            artivy = artivy - Etf.price
            komissi = komissi + Etf.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", listakt)
            print("Комиссия брокера:", Etf.price * stavka)
            return komissi
        elif sell == "Imoex":
            ballanse = ballanse + Imoex.price - (Imoex.price * stavka)
            listakt.remove("Imoex")
            artivy = artivy - Imoex.price
            komissi = komissi + Imoex.price * stavka
            print("Остаток денежных средств:", round(ballanse, 2))
            print("Проданные актив:", listakt)
            print("Комиссия брокера:", Imoex.price * stavka)
            return komissi
        else:
            print("Вы ввели не слово. Повторите ввод")
            sellfunct = sell_funct()


def study_funct():  # функция обучения(урок первый)
    print("Добро пожалость в Атом-инвест!")
    print("Кратко о курсе: данный курс состоит из 5 основных уроков, в конце которых,будет тест")
    print("-------------------")
    print("Урок первый. Почему каждому важно начать инвестировать")
    print("-------------------")
    print("Все просто. Биржа - это рынок. как овощной но только вместо овощей на нем продаются ценные бумаги. \n",
          ",Биржа следит, кто сколько чего купил и сколько осталось, смотрим чтобы все продавалось по закону.",
          "Чтобы получить доступ к бирже,обычному человеку нужен посредник - брокер \n .Брокер - это компания, которая получила лицензию для работы на бирже.",
          "Частные инвесторы покупают и продают бумаги на бирже через брокера. Конечно за комиссию. Но что можно купить на бирже?\n В первую очередь, это облигации. Облигации - ",
          "это долговые расписки.Когда инвестор покупает облигацию,он дает государству в долг, под проценты. \n Еще одним инструментов могут быть акции. Акции - это доля в компании.",
          "Владелец акции претендует на прибыль компании которую она получает. \n ETF также можно купить на бирже.ETF - это доля в фонде который купил кучу других акций и облигаций. ")
    print("-------------------")
    chose = (input("Желаете продолжить? Да/нет "))
    if chose == "Да":
        study2 = study2_funct()
    elif chose == "Нет":
        exeit = exeit_funct
    else:
        print("Ошибка ввода")
        studyfunct = study_funct()


def study2_funct():  # функция обучения(урок второй)
    print("Урок второй.  ИИС")
    print("-------------------")
    print(
        "ИИС - это особый брокерский счет, суть такая же как и обынчый счет, но преемущемтво это налоги, раз какое то время вы можете уменьшить себе базу налога. \n ",
        "Но есть серьезные ограничения деньги нельзя выводить со счета как минимум в течении трех лет после открытия счета. ИИС с типоп А поможет вернуть 13% от вложенного. \n ",
        "С вычетом Б, не платить налог с дохода на инвестиции. Открыть можно только один ИИС. Выбирать между обвчным счетом и ИИС не нужно, вы можете открыть сразу два.",
        "На ИИС можно заработать двумя способами: получать налоговые вычеты от государства, а также торговать на бирже, как и с обычным брокерским счетом.",
        "С помощью налогового вычета можно гарантированно получать до 52 000 ₽ в год, если вы платите НДФЛ и пополняете ИИС каждый год на 400 000 ₽ и больше.",
        "Другой вариант: можно освободить ваш доход по сделкам от налога в 13% — это выгодно, когда выбранная вами инвестиционная стратегия приносит больше 52 000 ₽ в год.")
    print("-------------------")
    chose = (input("Желаете продолжить? Да/нет "))
    if chose == "Да":
        study3 = study3_funct()
    elif chose == "Нет":
        exeit = exeit_funct()
    else:
        print("Ошибка ввода")
        study2 = study2_funct()


def study3_funct():  # функция обучения(урок третий)
    print("Урок третий. Облигации ")
    print(
        "Облигация — это долговая ценная бумага, почти как обычная расписка о том, что кто-то взял у вас деньги и обязуется вернуть их в определенную дату. \n",
        "Выпуская облигации, компании или государство тоже берут деньги в долг и затем возвращает их с процентами — в случае с облигациями их называют купонами. \n",
        "Облигации федерального займа (ОФЗ) — это государственные облигации, которые выпускает Министерство финансов России. Их еще называют суверенными. \n ",
        "Муниципальные (субфедеральные) — это еще один вид государственных облигаций, эмитентом которых являются администрации субъектов Российской Федерации. \n",
        "Корпоративные — это облигации, которые выпускают частные компании. По степени надежности они делятся на несколько категорий в соответствии с оценкой \n",
        "Еврооблигации — это облигации российских эмитентов, выпущенные в иностранной валюте, обычно в долларах или евро", )
    print("-------------------")
    chose = (input("Желаете продолжить? Да/нет "))
    if chose == "Да":
        study4 = study4_funct()
    elif chose == "Нет":
        exeit = exeit_funct()
    else:
        print("Ошибка ввода")
        study3 = study3_funct()


def study4_funct():  # функция обучения(урок четвертый)
    print("Урок четвертый. Фонды")
    print(
        "Exchange Traded Fund, или ETF, — это биржевой инвестиционный фонд, зарегистрированный вне пределов России, но акции которого можно приобрести на российском фондовом рынке. \n",
        " состав ETF входит определенное имущество — например, нефть, золото или даже кофе. Но чаще всего такие фонды состоят из набора акций и облигаций различных компаний \n",
        "Это могут быть акции крупнейших компаний одной отдельно взятой страны, или компаний определенного сектора экономики сразу группы стран, или компаний, представляющих целые регионы \n",
        "— например, развивающиеся экономики Юго-Восточной Азии. \n ",
        "Покупая акции такого фонда, вы становитесь совладельцем всех ценных бумаг, которые в него входят.Важной особенностью инвестирования в ETF является уплата комиссии за управление \n",
        "Биржевой паевой инвестиционный фонд, или БПИФ, — это практически полный аналог ETF с той лишь разницей, что зарегистрирован он на территории России \n",
        "Имуществом под управлением БПИФ тоже чаще всего выступают акции и облигации крупнейших компаний из одной или нескольких стран")
    print("-------------------")
    chose = (input("Желаете продолжить? Да/нет "))
    if chose == "Да":
        study5 = study5_funct()
    elif chose == "Нет":
        exeit = exeit_funct()
    else:
        print("Ошибка ввода")
        study4 = study4_funct()


def study5_funct():  # функция обучения(урок пятый)
    print("Урок пятый. Акции ")
    print(
        "Говоря просто, акция — это доля в бизнесе. После покупки акции инвестор становится одним из совладельцев компании и получает права на часть ее прибыли, а также \n",
        "на участие в управлении компанией через голосование на общих собраниях акционеров, о если акций у инвестора не много, его роль в управлении будет незначительной. \n",
        "В то же время даже владение очень маленькой долей в компании никак не мешает получать доход по ее акциям — для этого есть два способа:Получать часть прибыли компании в виде дивидендов \n",
        "Дождаться роста цен на акции компании и выгодно их продать.При этом один способ получения дохода не исключает другого: можно получать дивиденды, пока ждете роста стоимости акций \n",
        "а потом продать их, когда наступит подходящий момент/Привилегированные акции — это вид ценных бумаг, которые дают своим держателям дополнительные преимущества, но также накладывают и некоторые ограничения \n ",
        "Что выгоднее: акции или облигации?Всё зависит от вашей инвестиционной стратегии, целей и горизонта планирования, а также от готовности к риску. \n",
        "В исторической перспективе акции оказываются доходнее облигаций, но на коротких отрезках времени они могут значительно терять в цене \n",
        "Поэтому этот инструмент инвестирования считается более рискованным.")
    print("-------------------")
    chose = (input("Желаете пройти тест? Да/нет "))
    if chose == "Да":
        studytest = studytest_funct()
    elif chose == "Нет":
        exeit = exeit_funct()
    else:
        print("Ошибка ввода")
        study5 = study5_funct()


def studytest_funct():  # функция обучения(тестирование и результаты)
    global score
    print("Сейчас вас ждет итоговый тест из 5 вопросов.Напишите цифру при ответе. ")
    print("Вопрос номер 1. Кто такой брокер? \n",
          "1.Это компания, которая получила лицензию для работы на бирже \n",
          "2.Это группа людей, которые работают на бирже \n",
          "3.Это обычный бизнесмен \n", )
    first = (int(input("Введите 1,2 или 3: ")))
    if first == 1:
        print("правильный ответ!")
        print("-------------------")
    else:
        print("Неправильный ответ, почитайте обучения еще раз!")
        print("-------------------")
    print("Вопрос номер 2. Что такое ИИС? \n",
          "1.Иностранный инвестиционный счет \n",
          "2.Индвидуальный инвестиционный счет \n",
          "3.Искусственный инвестиционный счет \n", )
    second = (int(input("Введите 1,2 или 3: ")))
    if second == 2:
        print("правильный ответ!")
        print("-------------------")
    else:
        print("Неправильный ответ, почитайте обучения еще раз!")
        print("-------------------")
    print("Вопрос номер 3. Облигации - это ? \n",
          "1. это иностранная ценная бумага \n",
          "2. это государственный документ \n",
          "3.это долговая ценная бумага \n", )
    thrid = (int(input("Введите 1,2 или 3: ")))
    if thrid == 3:
        print("правильный ответ!")
        print("-------------------")
    else:
        print("Неправильный ответ, почитайте обучения еще раз!")
        print("-------------------")
    print("Вопрос номер 4. Как можно купить паи фонда?  \n",
          "1. через брокера \n",
          "2. придти самому \n",
          "3. невозможно купить\n", )
    four = (int(input("Введите 1,2 или 3:  ")))
    if four == 4:
        print("правильный ответ!")
        print("-------------------")
    else:
        print("Неправильный ответ, почитайте обучения еще раз!")
        print("-------------------")
    print("Вопрос номер 5. Акция - это  \n",
          "1. это доля в бизнесе  \n",
          "2. это депозит в банке  \n",
          "3. это инструмент махинация \n", )
    five = (int(input("Введите 1,2 или 3:  ")))
    if five == 2:
        print("правильный ответ!")
        print("-------------------")
    else:
        print("Неправильный ответ, почитайте обучения еще раз!")
        print("-------------------")
    print("Вы прошли наш тест! ")
    exeit = exeit_funct


def changeprice_funct():  # функция принудительного измнения цены
    global Apple
    change = input("Название актива для изменения: ")
    price = int(input("Напишите изменение актива: "))
    if change == "Apple":
        Apple.price = Apple.price + price
        print("Новая цена: ", Apple.price)
    elif change == "Nike":
        Nike.price = Nike.price + price
        print("Новая цена: ", Nike.price)
    elif change == "Pfizer":
        Pfizer.price = Pfizer.price + price
        print("Новая цена: ", Pfizer.price)
    elif change == "Google":
        Google.price = Google.price + price
        print("Новая цена: ", Google.price)
    elif change == "Fox":
        Fox.price = Fox.price + price
        print("Новая цена: ", Fox.price)
    elif change == "Tesla":
        Tesla.price = Tesla.price + price
        print("Новая цена: ", Tesla.price)
    elif change == "Visa":
        Visa.price = Visa.price + price
        print("Новая цена: ", Visa.price)
    elif change == "Walmart":
        Walmart.price = Walmart.price + price
        print("Новая цена: ", Walmart.price)
    elif change == "Uber":
        Uber.price = Uber.price + price
        print("Новая цена: ", Uber.price)
    elif change == "FedEx":
        FedEx.price = FedEx.price + price
        print("Новая цена: ", FedEx.price)
    elif change == "OFZ_1":
        OFZ_1.price = OFZ_1.price + price
        print("Новая цена: ", OFZ_1.price)
    elif change == "OFZ_2":
        OFZ_2.price = OFZ_2.price + price
        print("Новая цена: ", OFZ_2.price)
    elif change == "OFZ_3":
        OFZ_3.price = OFZ_3.price + price
        print("Новая цена: ", OFZ_3.price)
    elif change == "OFZ_4":
        OFZ_4.price = OFZ_4.price + price
        print("Новая цена: ", OFZ_4.price)
    elif change == "OFZ_5":
        OFZ_5.price = OFZ_5.price + price
        print("Новая цена: ", OFZ_5.price)
    elif change == "Fxus":
        Fxus.price = Fxus.price + price
        print("Новая цена: ", Fxus.price)
    elif change == "Etf":
        Etf.price = Etf.price + price
        print("Новая цена: ", Etf.price)
    elif change == "Imoex":
        Imoex.price = Imoex.price + price
        print("Новая цена: ", Imoex.price)
    else:
        print("ошибка ввода ")
        exeit = exeit_funct


def randomprice_funct():  # функция моделирования рыночной цены
    randomA1 = random.randint(-12, 15)  # случайная переменная для Apple
    randomA2 = random.randint(-8, 7)  # случайная переменная для Nike, Fed
    randomA3 = random.randint(-6, 8)  # случайная переменная для Pfizer
    randomA4 = random.randint(-14, 16)  # случайная переменная для Google
    randomA5 = random.randint(-3, 2)  # случайная переменная для Fox , Uber
    randomA6 = random.randint(-20, 20)  # случайная переменная для Tesla
    randomA7 = random.randint(-5, 7)  # случайная переменная для Visa
    randomA8 = random.randint(-11, 12)  # случайная переменная для Walmart
    randomO1 = random.randint(-4, 4)  # случайная переменная для облигаций
    randomO2 = random.randint(-1, 2)
    randomF = random.randint(-2, 5)  # случайная переменная для фондов
    Apple.price = Apple.price + randomA1
    Nike.price = Nike.price + randomA2
    Pfizer.price = Pfizer.price + randomA3
    Google.price = Google.price + randomA4
    Fox.price = Fox.price + randomA5
    Tesla.price = Tesla.price + randomA6
    Visa.price = Visa.price + randomA7
    Walmart.price = Walmart.price + randomA8
    Uber.price = Uber.price + randomA5
    FedEx.price = FedEx.price + randomA2
    OFZ_1.price = OFZ_1.price + randomO2
    OFZ_2.price = OFZ_2.price + randomO1
    OFZ_3.price = OFZ_3.price + randomO2
    OFZ_4.price = OFZ_4.price + randomO1
    OFZ_5.price = OFZ_5.price + randomO2
    Fxus.price = Fxus.price + randomF
    Etf.price = Etf.price + randomF
    Imoex.price = Imoex.price + randomF
    print("-------------------")
    print("обновление цен произведено")
    print("-------------------")

def menu_funct():  # функция основного меню
    while True:
        try:
            print("Основные функции приложения")
            print("-------------------")
            print("1.Пройти обучение")
            print("2.Посмотреть торгующиеся ценные бумаги")
            print("3.Купить ценные бумаги")
            print("4.Продать ценные бумаги")
            print("5.Посмотреть собственные активы")
            print("6.Пополнить счет")
            print("7.Обновление цены активов")
            print("8.Вывод денежных средств")
            print("9.Выход")
            print("-------------------")
            print("Функции разработчика")
            print("10.Изменение цены активов")
            print("-------------------")
            menu = input("Выберете пункт меню(введите номер пункта): ")
            if menu == "1":
                studyfunct = study_funct()  # функция обучения
            elif menu == "2":
                print("-------------------")
                Getlist = get_listakt()  # функция просмотра биржи
                print("-------------------")
            elif menu == "3":
                print("-------------------")
                buyfunct = buy_funct()  # функция покупки активов
                print("-------------------")
            elif menu == "4":
                print("-------------------")
                sellfunct = sell_funct()  # функция продажи активов
                print("-------------------")
            elif menu == "5":
                print("-------------------")
                print("Ваши активы")
                print("Наименование компаний которыми вы владете:", listakt)
                print("Общая сумма ваших активов", round(artivy, 2))
                print("Ваш баланс:", round(ballanse, 2))
                print("Общая сумма комисии:", round(komissi, 2))
                print("-------------------")
            elif menu == "6":  # функция дополнительного пополнения
                print("-------------------")
                getdop = getdop_cash()
            elif menu == "7":  # функция обновления цены
                randomprice = randomprice_funct()
            elif menu == "8":  # функция вывода средств
                out = out_cash()
            elif menu == "Выход" or menu == "9":
                print("Желаем хорошего дня!")
                break
            elif menu == "10":  # функция изменение цены актива
                changeprice = changeprice_funct()
                print("-------------------")
        except ValueError:
            print("Вы ввели неправильный символ. Повторите ввод")

def exeit_funct():  # функция обучения(выход из обучения!)
    print("-------------------")
menufun = menu_funct()
