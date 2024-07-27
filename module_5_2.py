class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor = int(input('Введите номер этажа: '))):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название:{self.name}, кол-во этажей: {self.number_of_floors}')



house = House('ЖК Эльбрус', 30)
house.go_to()

print(house)
print(len(house))


