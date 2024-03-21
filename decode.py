def is_end_of_row(index):
    """
    Determines if a given index marks the end of a row in a triangular sequence.

    Parameters:
    index (int): The current index.

    Returns:
    bool: True if the index marks the end of a row, False otherwise.
    """

    n = 0
    row_end = False

    while not row_end:
        triangular_number = n * (n + 1) // 2

        if index == triangular_number:
            row_end = True
        elif triangular_number > index:
            break

        n += 1

    return row_end


def decode(message_file):
    """
    Decodes a message file containing pairs of numbers and words.

    Parameters:
    message_file (str): The path to the message file.

    Returns:
    str: The decoded message.
    """

    with open(message_file) as file:
        lines = file.readlines()

    # Sort lines based on the first number in each line
    lines.sort(key=lambda x: int(x.split()[0]))

    decoded_words = []

    for line in lines:
        num, word = line.strip().split(" ")

        # Check if the current index marks the end of a row
        if is_end_of_row(int(num)):
            decoded_words.append(word)

    # Join the decoded words back into a single string
    return " ".join(decoded_words)


decoded_message = decode("encoded_message.txt")
print(decoded_message)
