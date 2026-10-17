"""Инвентарь персонажа: предметы и их количество.

Допишите методы класса Inventory. Сейчас все методы заглушки:
они выбрасывают NotImplementedError, и тесты падают.
"""

import json


class Inventory:
    def __init__(self):
        # Словарь: название предмета -> количество.
        self.items = {}

    def add(self, name, count=1):
        """Добавляет count предметов name. count должен быть больше 0, иначе ValueError."""
        raise NotImplementedError

    def remove(self, name, count=1):
        """Убирает count предметов name.

        Если предмета нет или его меньше, чем count, выбрасывает ValueError.
        Если количество стало 0, предмет удаляется из инвентаря.
        """
        raise NotImplementedError

    def count(self, name):
        """Возвращает количество предмета name. Если предмета нет, возвращает 0."""
        raise NotImplementedError

    def total(self):
        """Возвращает общее количество всех предметов."""
        raise NotImplementedError

    def to_dict(self):
        """Возвращает копию словаря предметов."""
        raise NotImplementedError

    def save(self, path):
        """Записывает инвентарь в JSON-файл по пути path."""
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        """Читает инвентарь из JSON-файла и возвращает новый объект Inventory."""
        raise NotImplementedError
