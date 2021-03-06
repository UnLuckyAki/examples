"""
Реализуете механизмы работы с заметками в этом модуле.
Примеры функции описаны ниже.
Вы спокойно можете изменять их, добавлять новые.
Главное - чтобы модуль работал так, как необходимо вашей программе.
"""
from typing import Union, Optional


def create_new_note(note_name: str, note_data: bytes) -> bool:
    """
    Создание новой заметки.

    note_name: название заметки.
    note_data: содержимое заметки.
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог создать новую заметку.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    raise Exception('not implemented')
    return False


def read_note(note_name: str) -> Optional[bytes]:
    """
    Получить содержимое заметки

    note_name: название заметки.
    Возвращает:
        содержимое заметки.
        None - если не смог прочитать заметку.

        Можно реализовать генерацию исключений для проверок.
    """
    raise Exception('not implemented')
    return None


def update_note(note_name: str, note_data: bytes) -> bool:
    """
    Обновить содержимое заметки.
    Можно реализовать с нуля, либо сделать как обертку над create_new_note.

    note_name: название заметки.
    note_data: содержимое заметки.
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог обновить содежимое заметки.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    raise Exception('not implemented')
    return False


def delete_note(note_name: str) -> bool:
    """
    Удалить существующую заметку

    note_name: название заметки.
    Возвращает:
        true - если операция была выполнена успешно;
        false - если не смог удалить заметку.

        Можно так же реализовать возвращение не true/false,
        а кода результата/ошибки.

        Или реализовать их через исключения.
    """
    raise Exception('not implemented')
    return False
