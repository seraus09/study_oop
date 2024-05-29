from abc import ABC, abstractmethod

# Патерн Декоратор

# Базовий інтерфейс компонентів
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретний компонент
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

# Базовий клас декораторів
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()

# Конкретний декоратор A
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"

# Конкретний декоратор B
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"

# Патерн Адаптер

# Цільовий інтерфейс
class Target(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

# Адаптований клас
class Adaptee:
    def specific_request(self) -> str:
        return "SpecificRequest"

# Адаптер, що забезпечує сумісність з цільовим інтерфейсом
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self) -> str:
        return self._adaptee.specific_request()

def main():
    # Використання Декоратора
    component = ConcreteComponent()
    print("Original:", component.operation())
    
    decorator1 = ConcreteDecoratorA(component)
    print("Decorated with A:", decorator1.operation())
    
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Decorated with A and B:", decorator2.operation())

    # Використання Адаптера
    adaptee = Adaptee()
    print("Adaptee:", adaptee.specific_request())
    
    adapter = Adapter(adaptee)
    print("Adapter:", adapter.request())

if __name__ == "__main__":
    main()
