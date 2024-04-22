from abc import ABC, abstractmethod

# Абстрактний клас для створення звуків
class Sound(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

# Конкретний клас для звуку собаки
class DogSound(Sound):
    def make_sound(self) -> str:
        return "Woof! Woof!"

# Конкретний клас для звуку кота
class CatSound(Sound):
    def make_sound(self) -> str:
        return "Meow! Meow!"

# Конкретний клас для звуку птаха
class BirdSound(Sound):
    def make_sound(self) -> str:
        return "Tweet! Tweet!"

# Фабричний метод для створення звуків собаки
def dog_sound_factory() -> Sound:
    return DogSound()

# Фабричний метод для створення звуків кота
def cat_sound_factory() -> Sound:
    return CatSound()

# Фабричний метод для створення звуків птаха
def bird_sound_factory() -> Sound:
    return BirdSound()

def main():
    print("Виберіть звук:")
    print("1. Собака")
    print("2. Кіт")
    print("3. Птах")
    choice = input("Введіть номер звуку: ")

    sound_factory = None
    if choice == '1':
        sound_factory = dog_sound_factory
    elif choice == '2':
        sound_factory = cat_sound_factory
    elif choice == '3':
        sound_factory = bird_sound_factory
    else:
        print("Некоректний вибір.")
        return

    sound = sound_factory()
    print("Отриманий звук:", sound.make_sound())

if __name__ == "__main__":
    main()