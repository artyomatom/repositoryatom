import itertools

def solve_codes():
    """
    Подсчитывает количество допустимых 5-буквенных кодов из букв 'ТИМОФЕЙ'
    с ограничениями на букву 'Й':
      - не более одного раза,
      - не на позициях 0 или 4,
      - не соседствует с 'И'.

    Returns:
        int: количество допустимых кодов.
    """
    letters = "ТИМОФЕЙ"
    valid_count = 0

    for combo in itertools.product(letters, repeat=5):
        word = ''.join(combo)
        y_count = word.count('Й')

        if y_count > 1:
            continue

        if y_count == 1:
            idx = word.index('Й')
            if idx == 0 or idx == 4:
                continue
            if (idx > 0 and word[idx - 1] == 'И') or (idx < 4 and word[idx + 1] == 'И'):
                continue

        valid_count += 1

    return valid_count