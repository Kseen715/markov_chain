from ..source.markovsky_gen import *
from pytest import raises


def test_read_file():
    assert read_file(None) == None


def test_split_words():
    assert split_words('Hello World!') == ['Hello', 'World!']
    assert split_words('') == []
    assert split_words(None) == None


def test_make_word_pair():
    assert list(make_word_pair(['Hello', 'World!'])) == [
        ('Hello', 'World!')]
    assert list(make_word_pair(['Hello', 'World!', 'Hello'])) == [
        ('Hello', 'World!'), ('World!', 'Hello')]
    assert list(make_word_pair([])) == []
    assert list(make_word_pair(None)) == []


def test_get_dict():
    assert get_dict(['Hello', 'World!']) == {'Hello': ['World!']}
    assert get_dict(['Hello', 'World!', 'Hello']) == \
        {'Hello': ['World!'], 'World!': ['Hello']}
    assert get_dict(['Hello', 'World!', 'Hello', 'World!']) == \
        {'Hello': ['World!', 'World!'], 'World!': ['Hello']}
    assert get_dict([]) == {}
    assert get_dict(None) == None


def test_generator_text_input_type():
    with raises(TypeError):
        generator_text('10')


def test_generator_text_output_length():
    assert len(generator_text(n=10).split()) == 10


def test_generator_text_input_length():
    with raises(TypeError):
        generator_text(-1)


def test_generator_symbol_input_type():
    with raises(TypeError):
        generator_symbol(10, 10)


def test_generator_symbol_input_length():
    with raises(TypeError):
        generator_symbol(-1)


def test_generator_symbol_output_length():
    assert len(generator_symbol(n=10, spacer=' ').split()) == 10
