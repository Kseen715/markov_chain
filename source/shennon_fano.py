from pprint import pprint
import markov_gen as mg

text = 'dsfkashdlkghXUC YFGJSPOCIQWJPIUHDEJXOUAHOIUHidughxvfuygxucb'
bytes_ = '01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001'


def to_binary_from_str(text):
    """
    Returns binary representation of text, separated by spaces

    Parameters
    ----------
        text (str): Text

    Returns
    -------
        str: Binary representation of text, separated by spaces
    """
    return ' '.join(format(ord(i), 'b') for i in text)


def from_binary_to_str(text):
    """
    Returns text from binary representation

    Parameters
    ----------
        text (str): Binary representation of text, separated by spaces

    Returns
    -------
        str: Text
    """
    return ''.join(chr(int(i, 2)) for i in text.split())


# Shennon-Fano algorithm of encoding and decoding text

def get_probability_dict(words):
    """
    Returns dict with probabilities of words

    Parameters
    ----------
        words (list): List of words

    Returns
    -------
        dict: Dict of probabilities of words
    """
    if words is None:
        return None
    if len(words) < 1:
        return None
    word_dict = {}
    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for word in word_dict.keys():
        word_dict[word] /= len(words)
    return word_dict


def sort_probability_dict(prob_dict):
    """
    Returns sorted dict of probabilities

    Parameters
    ----------
        prob_dict (dict): Dict of probabilities

    Returns
    -------
        list of tuple: Sorted list of probabilities
    """
    if prob_dict is None:
        return None
    return sorted(prob_dict.items(), key=lambda item: item[1], reverse=True)


def split_list(lst, prob=0.5):
    """
    Returns two lists, splitted by probability

    Parameters
    ----------
        lst (list): List to split
        prob (float): Probability of splitting

    Returns
    -------
        tuple of list of tuple: Two lists, splitted by probability
    """
    if lst is None:
        return None
    if len(lst) < 1:
        return None
    if prob < 0 or prob > 1:
        return None
    first = []
    second = []
    for i in range(len(lst)):
        if i < len(lst) * prob:
            first.append(lst[i])
        else:
            second.append(lst[i])
    return first, second


def split_half_by_probability(prob_dict):
    """
    Returns two dicts, splitted by probability

    Parameters
    ----------
        prob_dict (list of tuple): List of probabilities, sorted by probability
        decreasing

    Returns
    -------
        tuple of list of tuple: Two lists of tuples, splitted by probability
    """
    if prob_dict is None:
        return None
    if len(prob_dict) < 1:
        return None
    first = []
    second = []
    # split by sum of probabilities
    prob_sum = 0
    for i in range(len(prob_dict)):
        prob_sum += prob_dict[i][1]
    prob_sum /= 2
    # split by probability
    for i in range(len(prob_dict)):
        if prob_sum > 0:
            first.append(prob_dict[i])
            prob_sum -= prob_dict[i][1]
        else:
            second.append(prob_dict[i])
    return first, second


def append_to_tuples(lst, str):
    """
    Returns list of tuples with appended value

    Parameters
    ----------
        lst (list of tuple): List of tuples
        str (str): Value to append

    Returns
    -------
        list of tuple: List of tuples with appended value
    """
    if lst is None:
        return None
    if len(lst) < 1:
        return None
    for i in range(len(lst)):
        if len(lst[i]) == 2:
            lst[i] = (lst[i][0], lst[i][1], str)
        else:
            lst[i] = (lst[i][0], lst[i][1], lst[i][2] + str)
    return lst


def shennon_fano_encode(text):
    """
    Returns encoded text using Shennon-Fano algorithm

    Parameters
    ----------
        text (str): Text

    Returns
    -------
        str: Encoded text
    """
    raise NotImplementedError(
        'Я не успел это доделать и пошел спать :)')
    # TODO: finish this

    wrd_list = [sort_probability_dict(
        get_probability_dict(mg.split_words(text)))]
    pprint(wrd_list)
    # while every tuple has more than one element
    while len(wrd_list[0]) > 2:
        # split by probability
        for i in range(len(wrd_list)):
            wrd_list[i] = split_half_by_probability(wrd_list[i])
        # append '0' to first half and '1' to second
        for i in range(len(wrd_list)):
            wrd_list[i][0] = append_to_tuples(wrd_list[i][0], '0')
            wrd_list[i][1] = append_to_tuples(wrd_list[i][1], '1')
        # join lists
        wrd_list = wrd_list[0] + wrd_list[1]
        pprint(wrd_list)

    return wrd_list


print(shennon_fano_encode(bytes_))

# f, s = split_half_by_probability(sort_probability_dict(
#     get_probability_dict(mg.split_words(bytes_))))

# f = append_to_tuples(f, '0')
# s = append_to_tuples(s, '1')
# pprint(f)
# pprint(s)

# f2, s2 = split_half_by_probability(f)
# pprint(f2)
# pprint(s2)
# f2 = append_to_tuples(f2, '0')
# s2 = append_to_tuples(s2, '1')
# pprint(f2)
# pprint(s2)


def shennon_fano_encode(text):
    """
    Returns encoded text using Shennon-Fano algorithm

    Parameters
    ----------
        text (str): Text

    Returns
    -------
        str: Encoded text
    """
    raise NotImplementedError
