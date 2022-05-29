# Реализуйте модуль word_utils.py, позволяющий:
# - очистить предложение от знаков препинания;
# - получить список слов из предложения;
# - получить самое длинное слово в предложении;

import word_utils

source_string = 'Напишите программу, которая; будет считывать. содержимое файла, добавлять; к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.'
print(f'Source string: {source_string}')
print(f'String without punctuation: {word_utils.clear_string(source_string)}')
print(f'List of words from a sentence: {word_utils.split_string(source_string)}')
print(f'Longest word in a sentence: {word_utils.who_is_longest(source_string)}')
