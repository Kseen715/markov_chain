import numpy as np


def read_file(filepath):
    """
    Возвращает текст из файла

    Parameters
    ----------
        filepath (str): Путь к файлу

    Returns
    -------
        str: Текст из файла
    """
    if filepath is None:
        return None
    data = open(filepath, 'r', encoding='utf-8').read()
    return data


def split_words(text):
    """
    Возвращает список слов из текста

    Parameters
    ----------
        text (str): Текст
    Returns
    -------
        list: Cписок слов
    """
    if text is None:
        return None
    return text.split()


def make_word_pair(words):
    """
    Возвращает пары слов

    Parameters
    ----------
        words (list): Список слов

    Returns
    -------
        tuple: Пара слов
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

    Parameters
    ----------
        words (list): Список слов

    Returns
    -------
        dict: Словарь пар слов
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

    Parameters
    ----------
        n (int): Количество слов в генерируемом тексте
        spacer (str): Разделитель слов
        source_text (str): Исходный текст

    Returns
    -------
        str: Сгенерированный текст
    """
    if not isinstance(n, int) or n < 2 or not isinstance(spacer, str) or \
            not isinstance(source_text, str):
        raise TypeError('n must be int and n > 1')
    try:
        ind_words = split_words(source_text)
        word_dict = get_dict(ind_words)
        first_word = np.random.choice(ind_words)
        chain = [first_word]
        n_words = n - 1
        first_word = np.random.choice(ind_words)

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        res = spacer.join(chain)
        if type(res) == str and len(res.split()) == n:
            return res
        else:
            return generator_text(n, spacer, source_text)
    except:
        return generator_text(n, spacer, source_text)


def split_by_single_symbols(text, ignore_symbols=' '):
    """
    Разбивает строку на список символов

    Parameters
    ----------
        text (str): Строка
        ignore_symbols (str): Символы, которые не будут включены в список

    Returns
    -------
        list: Список символов
    """
    if not isinstance(text, str) or not isinstance(ignore_symbols, str):
        raise TypeError('text and ignore_symbols must be str')
    if len(ignore_symbols) == 0:
        return list(text)
    return [i for i in text if i not in ignore_symbols]


def generator_symbol(n, spacer='',
                     source_symbols=\
                        split_by_single_symbols(read_file('source/gkrf.txt'))):
    """
    Возвращает строку из n символов, сгенерированную на основе исходного текста
    с использованием марковской цепи

    Parameters
    ----------
        n (int): Количество символов в генерируемой строке
        spacer (str): Разделитель символов
        source_symbols (list): Исходные символы

    Returns
    -------
        str: Сгенерированная строка
    """
    if not isinstance(n, int) or n < 2 or not isinstance(spacer, str) or \
            not isinstance(source_symbols, list):
        raise TypeError('n must be int and n > 1')
    try:
        ind_words = source_symbols
        word_dict = get_dict(ind_words)
        first_word = np.random.choice(ind_words)
        chain = [first_word]
        n_words = n - 1
        first_word = np.random.choice(ind_words)
        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        res = spacer.join(chain)
        if type(res) == str and len(res) == n:
            return res
        else:
            return generator_symbol(n, spacer, source_symbols)
    except:
        return generator_symbol(n, spacer, source_symbols)


def glue_list_of_strings(list_of_strings, spacer=' '):
    """
    Склеивает список строк в одну строку

    Parameters
    ----------
        list_of_strings (list): Список строк
        spacer (str): Разделитель строк

    Returns
    -------
        str: Склеенная строка
    """
    if not isinstance(list_of_strings, list) or \
            not isinstance(spacer, str):
        raise TypeError('list_of_strings must be list and spacer must be str')
    return spacer.join(list_of_strings)

def split_string_to_list(string, spacer=' '):
    """
    Разбивает строку на список строк

    Parameters
    ----------
        string (str): Строка
        spacer (str): Разделитель строк

    Returns
    -------
        list: Список строк
    """
    if not isinstance(string, str) or \
            not isinstance(spacer, str):
        raise TypeError('string and spacer must be str')
    return string.split(spacer)