def encode(l: list[str]) -> str:
    res = ""
    for val in l:
        num = str(len(val))
        delimiter = "/"
        encoded_val = num + delimiter + val
        res += encoded_val
    return res


def decode(s: str) -> list[str]:
    local_array: list[str] = []
    i = 0
    while i < len(s):
        idx = i
        while idx < len(s) and s[idx] != '/':
            idx += 1
        length_of_word = int(s[i:idx])
        word = s[idx + 1: idx + 1 + length_of_word]
        i = idx + 1 + length_of_word
        local_array.append(word)

    return local_array


def main() -> None:
    list_of_strings = ["lint", "code", "love", "you"]
    val = encode(list_of_strings)
    print(val)  # 4/lint4/code4/love3/you

    back_to_list_of_strings = decode(val)
    print(back_to_list_of_strings)  # ['lint', 'code', 'love', 'you']


if __name__ == '__main__':
    main()
