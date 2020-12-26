def kmp_algorithm(text: str, subtext: str):
    if (type(text) is not str) or (type(subtext) is not str) or \
            (len(text) <= 0) or (len(subtext) <= 0) or (len(subtext) > len(text)):
        raise ValueError("Invalid input")

    subtext_len = len(subtext)
    text_len = len(text)
    indexes = []
    text_iterator = 0
    subtext_iterator = 0
    prefix = prefix_function(subtext)

    while text_iterator < text_len and subtext_iterator < subtext_len:

        if text[text_iterator] == subtext[subtext_iterator]:
            subtext_iterator += 1
            text_iterator += 1

        if subtext_iterator == subtext_len:
            indexes.append((text_iterator - subtext_len, text_iterator - 1))
            subtext_iterator = prefix[subtext_iterator - 1]


        elif text[text_iterator] != subtext[subtext_iterator] and text_iterator < text_len:

            if subtext_iterator == 0:
                text_iterator += 1


            else:
                subtext_iterator = prefix[subtext_iterator - 1]

    return indexes


def prefix_function(subtext: str):
    string_len = len(subtext)
    prefix_func = [0 for _ in range(string_len)]
    first_iterator = 0
    second_iterator = 1

    while second_iterator < string_len:

        if subtext[first_iterator] == subtext[second_iterator]:
            prefix_func[second_iterator] = first_iterator + 1
            first_iterator += 1
            second_iterator += 1

        elif first_iterator > 0:
            first_iterator = prefix_func[first_iterator - 1]

        else:
            prefix_func[second_iterator] = 0
            second_iterator += 1

    return prefix_func
