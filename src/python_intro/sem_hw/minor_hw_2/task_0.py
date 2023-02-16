def detect_language():
    s = input()
    strings = []
    while len(s) != 0:
        strings += [s]
        s = input()

    even_chars = set()
    odd_chars = set()
    for string in strings:
        string_len = len(string)
        for char in string:
            if string_len % 2 == 0:
                even_chars.add(char)
            else:
                odd_chars.add(char)

    if len(even_chars) > len(odd_chars):
        return len(strings[0]) % 2 == 0 and "Mumbo" or "Jumbo"

    return len(strings[0]) % 2 == 0 and "Jumbo" or "Mumbo"

if __name__ == '__main__':
    result = detect_language()
    print(result)
