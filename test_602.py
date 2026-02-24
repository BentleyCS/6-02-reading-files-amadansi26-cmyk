from CSP_6_02_reading_files import toString, longestLine, toBinary


def test_toString():
    assert toString("ExampleText.txt") == "Here is the text\ni am another line\nshort\n"


def test_longestLine():
    assert longestLine("ExampleText.txt") == "i am another line"


def test_toBinary():
    assert toBinary("BinaryExample.txt") == ['01101001', '00101010', '1010']
