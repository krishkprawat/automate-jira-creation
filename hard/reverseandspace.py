def reverse_letters_keep_positions(text: str) -> str:
    """Reverse only the alphabetic characters in the string while keeping
    spaces and any non-letter characters in their original positions.

    Examples:
    - "a,b$c" -> "c,b$a"
    - "ab c!" -> "cb a!"
    """
    characters = list(text)
    left_index = 0
    right_index = len(characters) - 1

    while left_index < right_index:
        if not characters[left_index].isalpha():
            left_index += 1
        elif not characters[right_index].isalpha():
            right_index -= 1
        else:
            characters[left_index], characters[right_index] = (
                characters[right_index],
                characters[left_index],
            )
            left_index += 1
            right_index -= 1

    return "".join(characters)


if __name__ == "__main__":
    samples = [
        "a,b$c",
        "ab c!",
        "kr!sh na@ 123",
        "Hello, World!",
        "  a-bC-dEf=ghlj!!  ",
    ]

    for s in samples:
        print(f"input : {s}")
        print(f"output: {reverse_letters_keep_positions(s)}\n")
