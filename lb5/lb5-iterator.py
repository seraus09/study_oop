from typing import List, Any

# Абстрактний клас ітератора
class Iterator:
    def __init__(self, collection: 'Collection'):
        self._collection = collection
        self._index = 0

    def next(self) -> Any:
        pass

    def has_next(self) -> bool:
        pass

# Клас колекції
class Collection:
    def __init__(self):
        self._data: List[Any] = []

    def add_item(self, item: Any):
        self._data.append(item)

    def create_iterator(self) -> Iterator:
        pass

# Конкретний ітератор
class ConcreteIterator(Iterator):
    def next(self) -> Any:
        if self.has_next():
            value = self._collection._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

    def has_next(self) -> bool:
        return self._index < len(self._collection._data)

# Конкретна колекція
class ConcreteCollection(Collection):
    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)

def main():
    collection = ConcreteCollection()
    collection.add_item("Елемент 1")
    collection.add_item("Елемент 2")
    collection.add_item("Елемент 3")

    iterator = collection.create_iterator()

    while iterator.has_next():
        print(iterator.next())

if __name__ == "__main__":
    main()
