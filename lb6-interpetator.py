from abc import ABC, abstractmethod

# Абстрактний клас виразу
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# Конкретний вираз - термінальний вираз, що представляє число
class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# Конкретний вираз - бінарний вираз додавання
class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Конкретний вираз - бінарний вираз віднімання
class SubtractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)

# Контекст
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable(self, variable):
        return self.variables.get(variable, 0)

def main():
    # Створення контексту
    context = Context()

    # Встановлення значень змінних
    context.set_variable('x', 10)
    context.set_variable('y', 5)

    # Створення виразів
    expression1 = AddExpression(NumberExpression(context.get_variable('x')), NumberExpression(context.get_variable('y')))
    expression2 = SubtractExpression(NumberExpression(context.get_variable('x')), NumberExpression(context.get_variable('y')))

    # Інтерпретація виразів
    result1 = expression1.interpret(context)
    result2 = expression2.interpret(context)

    # Виведення результатів
    print("Результат додавання:", result1)
    print("Результат віднімання:", result2)

if __name__ == "__main__":
    main()
