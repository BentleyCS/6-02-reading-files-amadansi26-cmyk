import os

def toString(fileName):
    # This function returns the text from a given file.
    # Any new lines are written as \n
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, fileName)

    with open(file_path, "r") as f:
        return f.read()


def longestLine(fileName):
    # Given a file return the longest line from within that file
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, fileName)

    longest = ""

    with open(file_path, "r") as f:
        for line in f:
            cleanLine = line.rstrip("\n")
            if len(cleanLine) > len(longest):
                longest = cleanLine

    return longest


def toBinary(fileName):
    # Given a file that is only 0's and 1's return a list
    # broken into groups of 8 (bytes)
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, fileName)

    data = ""

    with open(file_path, "r") as f:
        for line in f:
            data += line.strip()

    bytesList = []
    for i in range(0, len(data), 8):
        bytesList.append(data[i:i+8])

    return bytesList
