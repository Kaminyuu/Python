import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def load(file_name):
        date = None
        try:
            date = json.load(open(file_name))
        except FileNotFoundError:
            date = {}
        finally:
            return date

    @staticmethod
    def add_country(file_name):
        country_name = input("Введите название страны: ")
        capital_name = input("Введите название столицы: ")

        # try:
        #     date = json.load(open(file_name))
        # except FileNotFoundError:
        #     date = {}

        date = CountryCapital.load(file_name)

        date[country_name] = capital_name

        with open(file_name, 'w') as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def delete_county(file_name):

        with open(file_name, 'r') as f:
            date = json.load(f)

        delete_country = input("Введите страну которую хотите удалить: ")

        if delete_country in date:
            del date[delete_country]
            with open(file_name, 'w') as f:
                json.dump(date, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_country(file_name):
        search_country = input("Введите страну которую хотите найти: ")

        with open(file_name, 'r') as f:
            date = json.load(f)

        for country, capital in date.items():
            if country == search_country:
                dic = {}
                dic[country] = capital
                print(dic)

        if search_country in date:
            print(f"Страна {search_country} столица {date[search_country]} есть в словаре")
        else:
            print(f"Страны {search_country} нет в словаре")

    @staticmethod
    def editing_country(file_name):
        editing_country = input("Введите страну которую хотите отредактировать: ")
        editing_capital = input("Введите измененное имя города: ")

        with open(file_name, 'r') as f:
            date = json.load(f)

        date[editing_country] = editing_capital

        with open(file_name, 'w') as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as f:
            print(json.load(f))


file = 'list_capital.json'
index = ''
while True:
    index = input(
        "Действие:\n1 - добавление данных\n2 - удаленние данных\n3 - поиск данных\n"
        "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
    if index == '1':
        CountryCapital.add_country(file)
    elif index == '2':
        CountryCapital.delete_county(file)
    elif index == '3':
        CountryCapital.search_country(file)
    elif index == '4':
        CountryCapital.editing_country(file)
    elif index == '5':
        CountryCapital.load_from_file(file)
    elif index == '6':
        break
    else:
        print("Введен некорректный номер")

