class CodeGenerator:
    """
    Класс для генерации и подсчёта допустимых 5-буквенных кодов
    из заданного набора букв с ограничениями на определённые символы.
    """

    def __init__(self, alphabet="ТИМОФЕЙ", forbidden_letter='Й', neighbor_forbidden='И'):
        """
        Инициализация генератора кодов.

        Args:
            alphabet (str): набор доступных букв.
            forbidden_letter (str): буква с ограничениями (по умолчанию 'Й').
            neighbor_forbidden (str): буква, рядом с которой нельзя ставить forbidden_letter.
        """
        self.alphabet = alphabet
        self.forbidden_letter = forbidden_letter
        self.neighbor_forbidden = neighbor_forbidden

    def is_valid_code(self, word: str) -> bool:
        """
        Проверяет, является ли код допустимым согласно правилам.

        Args:
            word (str): проверяемый код длиной 5 символов.

        Returns:
            bool: True если код допустим, False иначе.
        """
        y_count = word.count(self.forbidden_letter)

        if y_count > 1:
            return False

        if y_count == 1:
            idx = word.index(self.forbidden_letter)
            # Не на краях
            if idx == 0 or idx == len(word) - 1:
                return False
            # Не рядом с запрещённым соседом
            if (idx > 0 and word[idx - 1] == self.neighbor_forbidden) or \
               (idx < len(word) - 1 and word[idx + 1] == self.neighbor_forbidden):
                return False

        return True

    def count_valid_codes(self, length=5) -> int:
        """
        Подсчитывает количество допустимых кодов заданной длины.

        Args:
            length (int): длина кода (по умолчанию 5).

        Returns:
            int: количество допустимых кодов.
        """
        valid_count = 0
        for combo in itertools.product(self.alphabet, repeat=length):
            word = ''.join(combo)
            if self.is_valid_code(word):
                valid_count += 1
        return valid_count