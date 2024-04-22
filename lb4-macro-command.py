from abc import ABC, abstractmethod

# Абстрактний клас для команди
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретна команда №1
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Конкретна команда №2
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Клас світла
class Light:
    def turn_on(self):
        print("Світло ввімкнено")

    def turn_off(self):
        print("Світло вимкнено")

# Клас Макрокоманди
class MacroCommand(Command):
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

# Функція main для демонстрації використання
def main():
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Створюємо макрокоманду і додаємо до неї окремі команди
    macro_command = MacroCommand()
    macro_command.add_command(light_on)
    macro_command.add_command(light_off)

    # Виконуємо макрокоманду
    macro_command.execute()

if __name__ == "__main__":
    main()
