#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    # Given a file return the longest line from within that file
    f = open(fileName)
    longest = ""

    for line in f:
        # remove the newline for fair comparison
        cleanLine = line.strip("\n")

        if len(cleanLine) > len(longest):
            longest = cleanLine

    f.close()
    return longest


def toBinary(fileName):
    # Given a file that is only 0's and 1's return a list
    # broken into groups of 8 (bytes)
    f = open(fileName)
    data = ""

    for line in f:
        data += line.strip()  # remove spaces and newlines

    f.close()

    bytesList = []
    currentByte = ""

    for char in data:
        currentByte += char

        if len(currentByte) == 8:
            bytesList.append(currentByte)
            currentByte = ""

    # if leftover bits (not full 8)
    if currentByte != "":
        bytesList.append(currentByte)

    return bytesList
