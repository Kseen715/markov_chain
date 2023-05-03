import numpy as np


def read_file(filepath):
    """
    Возвращает текст из файла
    Parameters:
        filepath (str): путь к файлу
    Returns:
        str: текст из файла
    """
    if filepath is None:
        return None
    data = open(filepath, 'r', encoding='utf-8').read()
    return data


def split_words(text):
    """
    Возвращает список слов из текста
    Parameters:
        text (str): текст
    Returns:
        list: список слов
    """
    if text is None:
        return None
    return text.split()


def make_word_pair(words):
    """
    Возвращает пары слов
    Parameters:
        words (list): список слов
    Returns:
        generator: генератор пар слов
    """
    if words is None:
        return None
    if len(words) < 2:
        return None
    for i in range(len(words) - 1):
        yield (words[i], words[i + 1])


def get_dict(words):
    """
    Возвращает словарь пар слов
    Parameters:
        words (list): список слов
    Returns:
        dict: словарь пар слов
    """
    if words is None:
        return None
    word_dict = {}
    for word_1, word_2 in make_word_pair(words):
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    return word_dict


def generator_text(n, spacer=' ',
                   source_text=read_file('source/gkrf.txt')):
    """
    Возвращает текст из n слов, сгенерированный на основе исходного текста
    с использованием марковской цепи
    Parameters:
        n (int): количество слов в генерируемом тексте
        spacer (str): разделитель слов
        source_text (str): исходный текст
    Returns:
        str: сгенерированный текст
    """
    if not isinstance(n, int) or n < 2 or not isinstance(spacer, str) or \
            not isinstance(source_text, str):
        raise TypeError('n must be int and n > 1')
    ind_words = split_words(source_text)
    word_dict = get_dict(ind_words)
    first_word = np.random.choice(ind_words)
    while first_word.islower():
        chain = [first_word]
        n_words = n - 1
        first_word = np.random.choice(ind_words)

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        return spacer.join(chain)


def generator_symbol(n, spacer='',
                     source_text=read_file('source/gkrf.txt')):
    """
    Возвращает строку из n символов, сгенерированную на основе исходного текста
    с использованием марковской цепи
    Parameters:
        n (int): количество символов в генерируемой строке
        spacer (str): разделитель символов
        source_text (str): исходный текст
    Returns:
        str: сгенерированная строка
    """
    if not isinstance(n, int) or n < 2 or not isinstance(spacer, str) or \
            not isinstance(source_text, str):
        raise TypeError('n must be int and n > 1')
    ind_words = split_words(source_text)
    word_dict = get_dict(ind_words)
    first_word = np.random.choice(ind_words)
    chain = [first_word]
    n_words = n - 1
    first_word = np.random.choice(ind_words)
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    return spacer.join(chain)
