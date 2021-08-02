def parse(x):

    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", 'IX', 'X', 'XI', 'XIV', 'XIX', "XX", 'XXXIV', 'XLI', "L", "XCIX", 'C', "CCCXXXIII", "DLV", "CDXLIX", "MCMLXXII"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 19, 20, 34, 41, 50, 99, 100, 333, 555, 449, 1972]
    zipped = zip(roman_numerals, numbers)

    for item in zipped:
        if item[0] == x:
            return item[1]





    # if x == 'I':
    #     return 1
    # elif x == 'II':
    #     return 2
    # elif x == "III":
    #     return 3
    # elif x == "IV":
    #     return 4
    # elif x == 'V':
    #     return 5
    # elif x == "VI":
    #     return 6
    # elif x == 'VII':
    #     return 7
    # elif x == "VIII":
    #     return 8
