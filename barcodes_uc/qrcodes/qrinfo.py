#Enumerators, Classes and functions that define the basic information of a qr code

#TODO: Change all classes to enums

#imports

import pandas as pd
from pathlib import Path
from enum import Enum

FILE_PATH = Path(__file__).parent / "../../data"

#From ../../data import the csv files with the qr code information
__CAPABILITIES = pd.read_csv(FILE_PATH / 'capabilities.csv')
__ERR_CORR = pd.read_csv(FILE_PATH / 'error_correction_table.csv')

#Dict with max number of characters for each version and error correction level from CAPABILITIES
MAX_CHARACTERS = {}
for mode in pd.unique(__CAPABILITIES['Encoding Mode']):
    MAX_CHARACTERS[mode] = {}
    for error in pd.unique(__CAPABILITIES['Error Correction Level']):
        MAX_CHARACTERS[mode][error] = {}
        for version in pd.unique(__CAPABILITIES['Version']):
            MAX_CHARACTERS[mode][error][version] = 0

for index, row in __CAPABILITIES.iterrows():
    MAX_CHARACTERS[row['Encoding Mode']][row['Error Correction Level']][row['Version']] = row['Maximum Number of Characters']

DATA_CODEWORDS = {}
for version in pd.unique(__ERR_CORR['Version']):
    DATA_CODEWORDS[version] = {}
    for error in pd.unique(__ERR_CORR['Error Correction Level']):
        DATA_CODEWORDS[version][error] = 0

for index, row in __ERR_CORR.iterrows():
    DATA_CODEWORDS[row['Version']][row['Error Correction Level']] = row['Number of Data Codewords']

#Delete the CAPABILITIES and ERR_CORR dataframes
del __CAPABILITIES
del __ERR_CORR

#Padding bytes
PAD_BYTES = ['11101100', '00010001']
    
#Enum class for qr encoding modes
class QREncoding(Enum):
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
    L = 'L' #7%
    M = 'M' #15%
    Q = 'Q' #25%
    H = 'H' #30%

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

def qr_encode_data_alphanumeric(version: QRVersion, correction: QRErrorCorrectionLevels, data: str) -> dict:
    blocks = {
        'Mode': '',
        'CharacterCount': '',
        'Data': [],
        'ExtraPadding': {
            'TerminatorZeros': '',
            'MultipleOf8': '',
            'PadBytes': []
        },
        'TotalLength': 0
    }
    totalLength = 0

    count_indicator = qr_count_indicator(version, QREncoding.alphanumeric, data)

    blocks['Mode'] = QREncoding.alphanumeric
    blocks['CharacterCount'] = count_indicator
    totalLength += len(count_indicator)
    totalLength += len(QREncoding.alphanumeric.value)

    for i in range(0, len(data), 2):
        if i + 2 <= len(data):
            number = AlphanumericVals[data[i]] * 45 + AlphanumericVals[data[i+1]]
            formatted = '{0:011b}'.format(number)

            blocks['Data'].append(formatted)
        else:
            number = AlphanumericVals[data[i]]
            formatted = '{0:06b}'.format(number)

            blocks['Data'].append(formatted)

        totalLength += len(formatted)

    dataBits = DATA_CODEWORDS[version][correction]*8
    remainderLength = dataBits - totalLength
    print(remainderLength)
    print(dataBits)

    #Extra padding

    #Terminator zeros (4 bits max)
    if remainderLength >= 4:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*4
        remainderLength -= 4
        totalLength += 4
    else:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*remainderLength
        remainderLength = 0
        totalLength += remainderLength

    #Add 0 until the length is a multiple of 8
    if remainderLength != 0 and remainderLength%8 != 0:
        blocks['ExtraPadding']['PadBytes'].append('0'*(remainderLength%8))
        totalLength += remainderLength%8
        remainderLength -= remainderLength%8

    #Padding bytes (8 bits per byte)
    if remainderLength != 8:
        padBytePos = 0
        while remainderLength >= 8:
            blocks['ExtraPadding']['PadBytes'].append(PAD_BYTES[padBytePos%2])
            remainderLength -= 8
            padBytePos += 1
            totalLength += 8

    blocks['TotalLength'] = totalLength

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
def qr_encode_data(version: QRVersion, encoding: QREncoding, correction: QRErrorCorrectionLevels, data: str) -> list:
    max_character_count = MAX_CHARACTERS[QREncoding(encoding).name][correction][version]

    if len(data) >= max_character_count:
        raise Exception('The data is too long for the version and error correction level chosen.')

    if encoding == QREncoding.numeric:
        return qr_encode_data_numeric(version, data)
    elif encoding == QREncoding.alphanumeric:
        return qr_encode_data_alphanumeric(version, correction, data)
    elif encoding == QREncoding.byte:
        return qr_encode_data_byte(version, data)
    elif encoding == QREncoding.kanji:
        return None
