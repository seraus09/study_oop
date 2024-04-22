from abc import ABC, abstractmethod

# Абстрактний клас для стратегії
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

# Конкретна стратегія №1
class ConcreteStrategyAdd(Strategy):
    def execute(self, data):
        return sum(data)

# Конкретна стратегія №2
class ConcreteStrategyMultiply(Strategy):
    def execute(self, data):
        result = 1
        for num in data:
            result *= num
        return result

# Контекст, який використовує стратегію
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy.execute(data)

def main():
    data = [1, 2, 3, 4, 5]

    # Використання стратегії додавання
    add_strategy = ConcreteStrategyAdd()
    context = Context(add_strategy)
    result = context.execute_strategy(data)
    print("Результат використання стратегії додавання:", result)

    # Використання стратегії множення
    multiply_strategy = ConcreteStrategyMultiply()
    context = Context(multiply_strategy)
    result = context.execute_strategy(data)
    print("Результат використання стратегії множення:", result)

if __name__ == "__main__":
    main()
