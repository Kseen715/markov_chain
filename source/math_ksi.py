def mean(x):
    """
    Returns mean of list of numbers
    Parameters:
        x (list): list of numbers
    Returns:
        float: mean of list of numbers
    """
    if x == [] or x is None:
        return None
    return sum(x)/len(x)


def make_unique(input_list):
    """
    Parameters:
        input_list (list): list of elements
    Returns:
        list: list of unique elements
    """
    return list(set(input_list))


def get_binary(number):
    """
    Returns binary representation of number
    Parameters:
        number (int): number
    Returns:
        str: binary representation of number
    """
    if number is None:
        return None
    return bin(number).replace('0b', '')


def variance(x):
    """
    Returns variance of list of numbers
    Parameters:
        x (list): list of numbers
    Returns:
        float: variance of list of numbers
    """
    if x == [] or x is None:
        return None
    return mean(list(map(lambda t: t**2, x))) - mean(x)**2


def splitter(n, text):
    return [text[i:i+n] for i in range(0, len(text), n)]


def generate_text(prob_list):
    text = ""
    for element in prob_list:
        for i in range(element[2]):
            text += element[3]
    return text


def rebuild_text(list_of_elements):
    text = ""
    for element in list_of_elements:
        text += element
    return text


def get_numbers_after_point_as_int(float):
    return int(str(float).split('.')[1])


def get_H(df):
    h = 0
    for i in df['Probabilities']:
        h += i * log2(i)
    return -h


def get_K(df):
    h = get_H(df)
    mean_length = 0
    for i in range(len(df)):
        mean_length += len(df['Code word'][i])
    mean_length /= len(df['Code word'])
    return h / mean_length
