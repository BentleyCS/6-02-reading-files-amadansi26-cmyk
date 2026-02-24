from CSP_6_02_reading_files (1).py import toString, longestLine, toBinary


def test_toString():
    # ExampleText.txt contains:
    # Here is the text
    # i am another line
    # short
    assert toString("ExampleText.txt") == "Here is the text\ni am another line\nshort\n"


def test_longestLine():
    # Longest line in ExampleText.txt is:
    # i am another line
    assert longestLine("ExampleText.txt") == "i am another line"


def test_toBinary():
    # BinaryExample.txt contains:
    # 01101001001010101010
    assert toBinary("BinaryExample.txt") == ['01101001', '00101010', '1010']
