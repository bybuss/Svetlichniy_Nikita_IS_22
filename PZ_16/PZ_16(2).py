"""
Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
"кличка" и "порода".
"""


class Animal:
    def __init__(self, vid: str, amount_of_paws: int, cool_of_wool: str):
        self.vid = vid
        self.amount_of_paws = amount_of_paws
        self.cool_of_wool = cool_of_wool

    def __str__(self) -> str:
        return f"Вид: {self.vid},\nЛап: {self.amount_of_paws}шт,\nШерсть: {self.cool_of_wool}"


class Dog(Animal):
    def __init__(self, vid: str, amount_of_paws: int, cool_of_wool: str, nickname: str, breed: str):
        super().__init__(vid, amount_of_paws, cool_of_wool)
        self.nickname = nickname
        self.breed = breed

    def __str__(self) -> str:
        return f"\n{super().__str__()},\nКличка: {self.nickname},\nПорода: {self.breed}"


animal = Animal(vid="Животное", amount_of_paws=0, cool_of_wool="😶‍🌫️")
print(animal)
dog = Dog(vid="Собака", amount_of_paws=4, cool_of_wool="Белая", nickname="Собака", breed="Собака")
print(dog)
