# Клас Memento зберігає стан об'єкта
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

# Клас Originator створює об'єкти Memento для збереження свого стану і використовує їх для відновлення стану
class Originator:
    def __init__(self, state: str):
        self._state = state

    def set_state(self, state: str):
        print(f"Setting state to {state}")
        self._state = state

    def get_state(self) -> str:
        return self._state

    def save_state_to_memento(self) -> Memento:
        print("Saving state to Memento")
        return Memento(self._state)

    def restore_state_from_memento(self, memento: Memento):
        self._state = memento.get_state()
        print(f"State restored from Memento: {self._state}")

# Клас Caretaker зберігає об'єкти Memento і керує їхнім збереженням та відновленням
class Caretaker:
    def __init__(self):
        self._memento_list = []

    def add(self, memento: Memento):
        self._memento_list.append(memento)

    def get(self, index: int) -> Memento:
        return self._memento_list[index]

def main():
    originator = Originator("State1")
    caretaker = Caretaker()

    # Зберігаємо стан
    caretaker.add(originator.save_state_to_memento())

    originator.set_state("State2")
    caretaker.add(originator.save_state_to_memento())

    originator.set_state("State3")
    caretaker.add(originator.save_state_to_memento())

    # Відновлюємо стан
    originator.restore_state_from_memento(caretaker.get(0))
    originator.restore_state_from_memento(caretaker.get(1))
    originator.restore_state_from_memento(caretaker.get(2))

if __name__ == "__main__":
    main()
