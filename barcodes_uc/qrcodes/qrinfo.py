#Enumerators, Classes and functions that define the basic information of a qr code

#Enum class for qr encoding modes
class QREncoding:
    numeric = '0001'
    alphanumeric = '0010'
    byte = '0100'
    kanji = '1000'

#Enum class for qr version
class QRVersion:
    v1 = 1
    v2 = 2
    v3 = 3
    v4 = 4
    v5 = 5
    v6 = 6
    v7 = 7
    v8 = 8
    v9 = 9
    v10 = 10
    v11 = 11
    v12 = 12
    v13 = 13
    v14 = 14
    v15 = 15
    v16 = 16
    v17 = 17
    v18 = 18
    v19 = 19
    v20 = 20
    v21 = 21
    v22 = 22
    v23 = 23
    v24 = 24
    v25 = 25
    v26 = 26
    v27 = 27
    v28 = 28
    v29 = 29
    v30 = 30
    v31 = 31
    v32 = 32
    v33 = 33
    v34 = 34
    v35 = 35
    v36 = 36
    v37 = 37
    v38 = 38
    v39 = 39
    v40 = 40

#Dict with the alphanumeric characters
AlphanumericVals = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 36,
    '$': 37,
    '%': 38,
    '*': 39,
    '+': 40,
    '-': 41,
    '.': 42,
    '/': 43,
    ':': 44
}

#Class error correction levels
class QRErrorCorrectionLevels:
    L = 'L'
    M = 'M'
    Q = 'Q'
    H = 'H'

#Dict with the maximum number of characters for each version and error correction level
MaxCharacters = {
    QREncoding.numeric: {
        QRErrorCorrectionLevels.L: {
            QRVersion.v1: 41,
            QRVersion.v2: 77,
            QRVersion.v3: 127,
            QRVersion.v4: 187,
            QRVersion.v5: 255,
            QRVersion.v6: 322,
            QRVersion.v7: 370,
            QRVersion.v8: 461,
            QRVersion.v9: 552,
            QRVersion.v10: 652,
            QRVersion.v11: 772,
            QRVersion.v12: 883,
            QRVersion.v13: 1022,
            QRVersion.v14: 1101,
            QRVersion.v15: 1250,
            QRVersion.v16: 1408,
            QRVersion.v17: 1548,
            QRVersion.v18: 1725,
            QRVersion.v19: 1903,
            QRVersion.v20: 2061,
            QRVersion.v21: 2232,
            QRVersion.v22: 2409,
            QRVersion.v23: 2620,
            QRVersion.v24: 2812,
            QRVersion.v25: 3057,
            QRVersion.v26: 3283,
            QRVersion.v27: 3517,
            QRVersion.v28: 3669,
            QRVersion.v29: 3909,
            QRVersion.v30: 4158,
            QRVersion.v31: 4417,
            QRVersion.v32: 4686,
            QRVersion.v33: 4965,
            QRVersion.v34: 5253,
            QRVersion.v35: 5529,
            QRVersion.v36: 5836,
            QRVersion.v37: 6153,
            QRVersion.v38: 6479,
            QRVersion.v39: 6743,
            QRVersion.v40: 7089,
        },
        QRErrorCorrectionLevels.M: {
            QRVersion.v1: 34,
            QRVersion.v2: 63,
            QRVersion.v3: 101,
            QRVersion.v4: 149,
            QRVersion.v5: 202,
            QRVersion.v6: 255,
            QRVersion.v7: 293,
            QRVersion.v8: 365,
            QRVersion.v9: 432,
            QRVersion.v10: 513,
            QRVersion.v11: 604,
            QRVersion.v12: 691,
            QRVersion.v13: 796,
            QRVersion.v14: 871,
            QRVersion.v15: 991,
            QRVersion.v16: 1082,
            QRVersion.v17: 1212,
            QRVersion.v18: 1346,
            QRVersion.v19: 1500,
            QRVersion.v20: 1600,
            QRVersion.v21: 1708,
            QRVersion.v22: 1872,
            QRVersion.v23: 2059,
            QRVersion.v24: 2188,
            QRVersion.v25: 2395,
            QRVersion.v26: 2544,
            QRVersion.v27: 2701,
            QRVersion.v28: 2857,
            QRVersion.v29: 3035,
            QRVersion.v30: 3289,
            QRVersion.v31: 3486,
            QRVersion.v32: 3693,
            QRVersion.v33: 3909,
            QRVersion.v34: 4134,
            QRVersion.v35: 4343,
            QRVersion.v36: 4588,
            QRVersion.v37: 4775,
            QRVersion.v38: 5039,
            QRVersion.v39: 5313,
            QRVersion.v40: 5596,
        },
        QRErrorCorrectionLevels.Q: {
            QRVersion.v1: 27,
            QRVersion.v2: 48,
            QRVersion.v3: 77,
            QRVersion.v4: 111,
            QRVersion.v5: 144,
            QRVersion.v6: 178,
            QRVersion.v7: 207,
            QRVersion.v8: 259,
            QRVersion.v9: 312,
            QRVersion.v10: 364,
            QRVersion.v11: 427,
            QRVersion.v12: 489,
            QRVersion.v13: 580,
            QRVersion.v14: 621,
            QRVersion.v15: 703,
            QRVersion.v16: 775,
            QRVersion.v17: 876,
            QRVersion.v18: 948,
            QRVersion.v19: 1063,
            QRVersion.v20: 1159,
            QRVersion.v21: 1224,
            QRVersion.v22: 1358,
            QRVersion.v23: 1468,
            QRVersion.v24: 1588,
            QRVersion.v25: 1718,
            QRVersion.v26: 1804,
            QRVersion.v27: 1933,
            QRVersion.v28: 2085,
            QRVersion.v29: 2181,
            QRVersion.v30: 2358,
            QRVersion.v31: 2473,
            QRVersion.v32: 2670,
            QRVersion.v33: 2805,
            QRVersion.v34: 2949,
            QRVersion.v35: 3081,
            QRVersion.v36: 3244,
            QRVersion.v37: 3417,
            QRVersion.v38: 3599,
            QRVersion.v39: 3791,
            QRVersion.v40: 3993,
        },
        QRErrorCorrectionLevels.H: {
            QRVersion.v1: 17,
            QRVersion.v2: 34,
            QRVersion.v3: 58,
            QRVersion.v4: 82,
            QRVersion.v5: 106,
            QRVersion.v6: 139,
            QRVersion.v7: 154,
            QRVersion.v8: 202,
            QRVersion.v9: 235,
            QRVersion.v10: 288,
            QRVersion.v11: 331,
            QRVersion.v12: 374,
            QRVersion.v13: 427,
            QRVersion.v14: 468,
            QRVersion.v15: 530,
            QRVersion.v16: 602,
            QRVersion.v17: 674,
            QRVersion.v18: 746,
            QRVersion.v19: 813,
            QRVersion.v20: 919,
            QRVersion.v21: 969,
            QRVersion.v22: 1056,
            QRVersion.v23: 1108,
            QRVersion.v24: 1228,
            QRVersion.v25: 1286,
            QRVersion.v26: 1425,
            QRVersion.v27: 1501,
            QRVersion.v28: 1581,
            QRVersion.v29: 1677,
            QRVersion.v30: 1782,
            QRVersion.v31: 1897,
            QRVersion.v32: 2022,
            QRVersion.v33: 2157,
            QRVersion.v34: 2301,
            QRVersion.v35: 2361,
            QRVersion.v36: 2524,
            QRVersion.v37: 2625,
            QRVersion.v38: 2735,
            QRVersion.v39: 2927,
            QRVersion.v40: 3057,
        },
    },
    QREncoding.alphanumeric: {
        QRErrorCorrectionLevels.L: {
            QRVersion.v1: 25,
            QRVersion.v2: 47,
            QRVersion.v3: 77,
            QRVersion.v4: 114,
            QRVersion.v5: 154,
            QRVersion.v6: 195,
            QRVersion.v7: 224,
            QRVersion.v8: 279,
            QRVersion.v9: 335,
            QRVersion.v10: 395,
            QRVersion.v11: 468,
            QRVersion.v12: 535,
            QRVersion.v13: 619,
            QRVersion.v14: 667,
            QRVersion.v15: 758,
            QRVersion.v16: 854,
            QRVersion.v17: 938,
            QRVersion.v18: 1046,
            QRVersion.v19: 1153,
            QRVersion.v20: 1249,
            QRVersion.v21: 1352,
            QRVersion.v22: 1460,
            QRVersion.v23: 1588,
            QRVersion.v24: 1704,
            QRVersion.v25: 1853,
            QRVersion.v26: 1990,
            QRVersion.v27: 2132,
            QRVersion.v28: 2223,
            QRVersion.v29: 2369,
            QRVersion.v30: 2520,
            QRVersion.v31: 2677,
            QRVersion.v32: 2840,
            QRVersion.v33: 3009,
            QRVersion.v34: 3183,
            QRVersion.v35: 3351,
            QRVersion.v36: 3537,
            QRVersion.v37: 3729,
            QRVersion.v38: 3927,
            QRVersion.v39: 4087,
            QRVersion.v40: 4296,
        },
        QRErrorCorrectionLevels.M: {
            QRVersion.v1: 20,
            QRVersion.v2: 38,
            QRVersion.v3: 61,
            QRVersion.v4: 90,
            QRVersion.v5: 122,
            QRVersion.v6: 154,
            QRVersion.v7: 178,
            QRVersion.v8: 221,
            QRVersion.v9: 262,
            QRVersion.v10: 311,
            QRVersion.v11: 366,
            QRVersion.v12: 419,
            QRVersion.v13: 483,
            QRVersion.v14: 528,
            QRVersion.v15: 600,
            QRVersion.v16: 656,
            QRVersion.v17: 734,
            QRVersion.v18: 816,
            QRVersion.v19: 909,
            QRVersion.v20: 970,
            QRVersion.v21: 1035,
            QRVersion.v22: 1134,
            QRVersion.v23: 1248,
            QRVersion.v24: 1326,
            QRVersion.v25: 1451,
            QRVersion.v26: 1542,
            QRVersion.v27: 1637,
            QRVersion.v28: 1732,
            QRVersion.v29: 1839,
            QRVersion.v30: 1994,
            QRVersion.v31: 2113,
            QRVersion.v32: 2238,
            QRVersion.v33: 2369,
            QRVersion.v34: 2506,
            QRVersion.v35: 2632,
            QRVersion.v36: 2780,
            QRVersion.v37: 2894,
            QRVersion.v38: 3054,
            QRVersion.v39: 3220,
            QRVersion.v40: 3391,  
        },
        QRErrorCorrectionLevels.Q: {
            QRVersion.v1: 16,
            QRVersion.v2: 29,
            QRVersion.v3: 47,
            QRVersion.v4: 67,
            QRVersion.v5: 87,
            QRVersion.v6: 108,
            QRVersion.v7: 125,
            QRVersion.v8: 157,
            QRVersion.v9: 189,
            QRVersion.v10: 221,
            QRVersion.v11: 259,
            QRVersion.v12: 296,
            QRVersion.v13: 352,
            QRVersion.v14: 376,
            QRVersion.v15: 426,
            QRVersion.v16: 470,
            QRVersion.v17: 531,
            QRVersion.v18: 574,
            QRVersion.v19: 644,
            QRVersion.v20: 702,
            QRVersion.v21: 742,
            QRVersion.v22: 823,
            QRVersion.v23: 890,
            QRVersion.v24: 963,
            QRVersion.v25: 1041,
            QRVersion.v26: 1094,
            QRVersion.v27: 1172,
            QRVersion.v28: 1263,
            QRVersion.v29: 1322,
            QRVersion.v30: 1429,
            QRVersion.v31: 1499,
            QRVersion.v32: 1618,
            QRVersion.v33: 1700,
            QRVersion.v34: 1787,
            QRVersion.v35: 1867,
            QRVersion.v36: 1966,
            QRVersion.v37: 2071,
            QRVersion.v38: 2191,
            QRVersion.v39: 2306,
            QRVersion.v40: 2434,
        },
        QRErrorCorrectionLevels.H: {
            QRVersion.v1: 10,
            QRVersion.v2: 20,
            QRVersion.v3: 35,
            QRVersion.v4: 50,
            QRVersion.v5: 64,
            QRVersion.v6: 84,
            QRVersion.v7: 93,
            QRVersion.v8: 122,
            QRVersion.v9: 143,
            QRVersion.v10: 174,
            QRVersion.v11: 200,
            QRVersion.v12: 227,
            QRVersion.v13: 259,
            QRVersion.v14: 283,
            QRVersion.v15: 321,
            QRVersion.v16: 365,
            QRVersion.v17: 408,
            QRVersion.v18: 452,
            QRVersion.v19: 493,
            QRVersion.v20: 557,
            QRVersion.v21: 587,
            QRVersion.v22: 640,
            QRVersion.v23: 672,
            QRVersion.v24: 744,
            QRVersion.v25: 779,
            QRVersion.v26: 864,
            QRVersion.v27: 910,
            QRVersion.v28: 958,
            QRVersion.v29: 1016,
            QRVersion.v30: 1080,
            QRVersion.v31: 1150,
            QRVersion.v32: 1226,
            QRVersion.v33: 1307,
            QRVersion.v34: 1394,
            QRVersion.v35: 1431,
            QRVersion.v36: 1530,
            QRVersion.v37: 1591,
            QRVersion.v38: 1658,
            QRVersion.v39: 1774,
            QRVersion.v40: 1852,
        },
    },
    QREncoding.byte: {
        QRErrorCorrectionLevels.L: {
            QRVersion.v1: 17,
            QRVersion.v2: 32,
            QRVersion.v3: 53,
            QRVersion.v4: 78,
            QRVersion.v5: 106,
            QRVersion.v6: 134,
            QRVersion.v7: 154,
            QRVersion.v8: 192,
            QRVersion.v9: 230,
            QRVersion.v10: 271,
            QRVersion.v11: 321,
            QRVersion.v12: 367,
            QRVersion.v13: 425,
            QRVersion.v14: 458,
            QRVersion.v15: 520,
            QRVersion.v16: 586,
            QRVersion.v17: 644,
            QRVersion.v18: 718,
            QRVersion.v19: 792,
            QRVersion.v20: 858,
            QRVersion.v21: 929,
            QRVersion.v22: 1003,
            QRVersion.v23: 1091,
            QRVersion.v24: 1171,
            QRVersion.v25: 1273,
            QRVersion.v26: 1367,
            QRVersion.v27: 1465,
            QRVersion.v28: 1528,
            QRVersion.v29: 1628,
            QRVersion.v30: 1732,
            QRVersion.v31: 1840,
            QRVersion.v32: 1952,
            QRVersion.v33: 2068,
            QRVersion.v34: 2188,
            QRVersion.v35: 2303,
            QRVersion.v36: 2431,
            QRVersion.v37: 2563,
            QRVersion.v38: 2699,
            QRVersion.v39: 2809,
            QRVersion.v40: 2953,
        },
        QRErrorCorrectionLevels.M: {
            QRVersion.v1: 14,
            QRVersion.v2: 26,
            QRVersion.v3: 42,
            QRVersion.v4: 62,
            QRVersion.v5: 84,
            QRVersion.v6: 106,
            QRVersion.v7: 122,
            QRVersion.v8: 152,
            QRVersion.v9: 180,
            QRVersion.v10: 213,
            QRVersion.v11: 251,
            QRVersion.v12: 287,
            QRVersion.v13: 331,
            QRVersion.v14: 362,
            QRVersion.v15: 412,
            QRVersion.v16: 450,
            QRVersion.v17: 504,
            QRVersion.v18: 560,
            QRVersion.v19: 624,
            QRVersion.v20: 666,
            QRVersion.v21: 711,
            QRVersion.v22: 779,
            QRVersion.v23: 857,
            QRVersion.v24: 911,
            QRVersion.v25: 997,
            QRVersion.v26: 1059,
            QRVersion.v27: 1125,
            QRVersion.v28: 1190,
            QRVersion.v29: 1264,
            QRVersion.v30: 1370,
            QRVersion.v31: 1452,
            QRVersion.v32: 1538,
            QRVersion.v33: 1628,
            QRVersion.v34: 1722,
            QRVersion.v35: 1809,
            QRVersion.v36: 1911,
            QRVersion.v37: 1989,
            QRVersion.v38: 2099,
            QRVersion.v39: 2213,
            QRVersion.v40: 2331,
        },
        QRErrorCorrectionLevels.Q: {
            QRVersion.v1: 11,
            QRVersion.v2: 20,
            QRVersion.v3: 32,
            QRVersion.v4: 46,
            QRVersion.v5: 60,
            QRVersion.v6: 74,
            QRVersion.v7: 86,
            QRVersion.v8: 108,
            QRVersion.v9: 130,
            QRVersion.v10: 151,
            QRVersion.v11: 177,
            QRVersion.v12: 203,
            QRVersion.v13: 241,
            QRVersion.v14: 258,
            QRVersion.v15: 292,
            QRVersion.v16: 322,
            QRVersion.v17: 364,
            QRVersion.v18: 394,
            QRVersion.v19: 442,
            QRVersion.v20: 482,
            QRVersion.v21: 509,
            QRVersion.v22: 565,
            QRVersion.v23: 611,
            QRVersion.v24: 661,
            QRVersion.v25: 715,
            QRVersion.v26: 751,
            QRVersion.v27: 805,
            QRVersion.v28: 868,
            QRVersion.v29: 908,
            QRVersion.v30: 982,
            QRVersion.v31: 1030,
            QRVersion.v32: 1112,
            QRVersion.v33: 1168,
            QRVersion.v34: 1228,
            QRVersion.v35: 1283,
            QRVersion.v36: 1351,
            QRVersion.v37: 1423,
            QRVersion.v38: 1499,
            QRVersion.v39: 1579,
            QRVersion.v40: 1663,
        },
        QRErrorCorrectionLevels.H: {
            QRVersion.v1: 7,
            QRVersion.v2: 14,
            QRVersion.v3: 24,
            QRVersion.v4: 34,
            QRVersion.v5: 44,
            QRVersion.v6: 58,
            QRVersion.v7: 64,
            QRVersion.v8: 84,
            QRVersion.v9: 98,
            QRVersion.v10: 119,
            QRVersion.v11: 137,
            QRVersion.v12: 155,
            QRVersion.v13: 177,
            QRVersion.v14: 194,
            QRVersion.v15: 220,
            QRVersion.v16: 250,
            QRVersion.v17: 280,
            QRVersion.v18: 310,
            QRVersion.v19: 338,
            QRVersion.v20: 382,
            QRVersion.v21: 403,
            QRVersion.v22: 439,
            QRVersion.v23: 461,
            QRVersion.v24: 511,
            QRVersion.v25: 535,
            QRVersion.v26: 593,
            QRVersion.v27: 625,
            QRVersion.v28: 658,
            QRVersion.v29: 698,
            QRVersion.v30: 742,
            QRVersion.v31: 790,
            QRVersion.v32: 842,
            QRVersion.v33: 898,
            QRVersion.v34: 958,
            QRVersion.v35: 983,
            QRVersion.v36: 1051,
            QRVersion.v37: 1093,
            QRVersion.v38: 1139,
            QRVersion.v39: 1219,
            QRVersion.v40: 1273,
        },
    },
}

#Function that calculates the size of the qr code
def qr_size(version: QRVersion) -> int:
    return 4 * (version - 1) + 21

#Function that returns the character count indicator size for the qr code
def qr_count_indicator_size(version: QRVersion, encoding: QREncoding) -> int:
    if version <= 9:
        if encoding == QREncoding.numeric:
            return 10
        elif encoding == QREncoding.alphanumeric:
            return 9
        elif encoding == QREncoding.byte:
            return 8
        elif encoding == QREncoding.kanji:
            return 8
        else:
            return 0
    elif version <= 26:
        if encoding == QREncoding.numeric:
            return 12
        elif encoding == QREncoding.alphanumeric:
            return 11
        elif encoding == QREncoding.byte:
            return 16
        elif encoding == QREncoding.kanji:
            return 10
        else:
            return 0
    elif version <= 40:
        if encoding == QREncoding.numeric:
            return 14
        elif encoding == QREncoding.alphanumeric:
            return 13
        elif encoding == QREncoding.byte:
            return 16
        elif encoding == QREncoding.kanji:
            return 12
        
#Function that returns the character count indicator for the qr code
def qr_count_indicator(version: QRVersion, encoding: QREncoding, data: str) -> str:
    size = qr_count_indicator_size(version, encoding)
    count = len(data)
    if encoding == QREncoding.numeric or encoding == QREncoding.alphanumeric:
        return '{0:0{1}b}'.format(count, size)
    elif encoding == QREncoding.byte or encoding == QREncoding.kanji:
        return '{0:0{1}b}'.format(count, size)
    
def qr_encode_data_numeric(version: QRVersion, data: str) -> dict:
    blocks = {
        'Mode': '',
        'CharacterCount': '',
        'Data': []
    }
    count_indicator = qr_count_indicator(version, QREncoding.numeric, data)

    blocks['Mode'] = QREncoding.numeric
    blocks['CharacterCount'] = count_indicator

    # print(len(data))
    for i in range(0, len(data), 3):
        if i + 3 <= len(data):
            number = int(data[i:i+3])
            # print(number)
            if number > 99:
                formatted = '{0:010b}'.format(number)
            elif number > 9:
                formatted = '{0:07b}'.format(number)
            else:
                formatted = '{0:04b}'.format(number)

            blocks['Data'].append(formatted)
        else:
            number = int(data[i:])
            # print(number)
            if number > 99:
                formatted = '{0:010b}'.format(number)
            elif number > 9:
                formatted = '{0:07b}'.format(number)
            else:
                formatted = '{0:04b}'.format(number)

            blocks['Data'].append(formatted)

    return blocks

def qr_encode_data_alphanumeric(version: QRVersion, data: str) -> dict:
    blocks = {
        'Mode': '',
        'CharacterCount': '',
        'Data': []
    }
    count_indicator = qr_count_indicator(version, QREncoding.alphanumeric, data)

    blocks['Mode'] = QREncoding.alphanumeric
    blocks['CharacterCount'] = count_indicator

    for i in range(0, len(data), 2):
        if i + 2 <= len(data):
            number = AlphanumericVals[data[i]] * 45 + AlphanumericVals[data[i+1]]
            formatted = '{0:011b}'.format(number)

            blocks['Data'].append(formatted)
        else:
            number = AlphanumericVals[data[i]]
            formatted = '{0:06b}'.format(number)

            blocks['Data'].append(formatted)

    return blocks

def qr_encode_data_byte(version: QRVersion, data: str) -> list:
    blocks = {
        'Mode': '',
        'CharacterCount': '',
        'Data': []
    }
    count_indicator = qr_count_indicator(version, QREncoding.byte, data)

    blocks['Mode'] = QREncoding.byte
    blocks['CharacterCount'] = count_indicator

    #split the data in bytes
    for i in range(0, len(data)):
        byte = ord(data[i])
        # print(byte)
        formatted = '{0:08b}'.format(byte)

        blocks['Data'].append(formatted)

    return blocks
    
#Function that encodes the data in the qr code and returns every block of data
def qr_encode_data(version: QRVersion, encoding: QREncoding, data: str) -> list:
    if encoding == QREncoding.numeric:
        return qr_encode_data_numeric(version, data)
    elif encoding == QREncoding.alphanumeric:
        return qr_encode_data_alphanumeric(version, data)
    elif encoding == QREncoding.byte:
        return qr_encode_data_byte(version, data)
    elif encoding == QREncoding.kanji:
        return None
