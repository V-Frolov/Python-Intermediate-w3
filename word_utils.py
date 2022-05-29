def clear_string(source_string):
    source_string = source_string.replace(".", '')
    source_string = source_string.replace(",", '')
    source_string = source_string.replace(";", '')
    source_string = source_string.replace("-", '')
    return source_string


def split_string(source_string):
    splitted_text = clear_string(source_string).split()
    return splitted_text


def who_is_longest(source_string):
    source_string = split_string(source_string)
    candidate = source_string[0]
    for i in source_string:
        if len(candidate) < len(i):
            candidate = i
    return candidate
