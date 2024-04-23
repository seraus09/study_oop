import copy

# Клас, який визначає загальний інтерфейс тварин
class Animal:
    def __init__(self, name):
        self.name = name

    def clone(self):
        # Використовуємо глибоке копіювання для створення копії об'єкта
        return copy.deepcopy(self)

    def make_sound(self):
        pass

# Конкретний клас для собаки
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Конкретний клас для кота
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Конкретний клас для птаха
class Bird(Animal):
    def make_sound(self):
        return "Tweet! Tweet!"

if __name__ == "__main__":
    # Створюємо об'єкти різних типів тварин
    dog = Dog("Барбос")
    cat = Cat("Мурзик")
    bird = Bird("Чічка")

    # Клонуємо тварини
    cloned_dog = dog.clone()
    cloned_cat = cat.clone()
    cloned_bird = bird.clone()

    # Перевіряємо чи копія рівна оригіналу
    print(dog.name, "гавкає:", dog.make_sound())
    print(cloned_dog.name, "гавкає:", cloned_dog.make_sound())
    print()

    print(cat.name, "муркоче:", cat.make_sound())
    print(cloned_cat.name, "муркоче:", cloned_cat.make_sound())
    print()

    print(bird.name, "співає:", bird.make_sound())
    print(cloned_bird.name, "співає:", cloned_bird.make_sound())
