class Tourist:
    next_id = 1

    def __init__(self, first_name, surname, date_of_birth, address, phone_number):
        self.id = Tourist.next_id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.all_tours = {}
        Tourist.next_id += 1


class Tour:
    def __init__(self, date_of_tour, country, operator_name, flight_number, hotel_name, price):
        self.date_of_tour = date_of_tour
        self.country = country
        self.operator_name = operator_name
        self.flight_number = flight_number
        self.hotel_name = hotel_name
        self.price = price


class TouristDb:

    tourist = {}

    @staticmethod
    def add_tourist(args):
        TouristDb.tourist.update({args.id: args})

    def get_tourist(self):
        return list(self.tourist.values())

    while True:
        print("Список команд:")
        print("Добавить туриста")
        print("Удалить туриста")
        command = input("Введите команду: ")
        if command == "Добавить туриста":
            print('Добавление данных туриста')
            first_name = input("Введите имя туриста: ")
            surname = input("Введите фамилию туриста: ")
            date_of_birth = input("Введите дату рождения туриста в формате 'ДД/ММ/ГГГГ': ")
            address = input("Введите адрес проживания туриста: ")
            phone_number = input("Введите телефонный номер туриста: ")
            add_tourist(Tourist(first_name=first_name, surname=surname, date_of_birth=date_of_birth, address=address, phone_number=phone_number))




