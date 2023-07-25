#Enumerators, Classes and functions that define the basic information of a qr code

#TODO: Change all classes to enums

#imports

from pathlib import Path
from enum import Enum
import numpy as np
import pandas as pd

FILE_PATH = Path(__file__).parent / "../../data"

#From ../../data import the csv files with the qr code information
__CAPABILITIES = pd.read_csv(FILE_PATH / 'capabilities.csv')
__ERR_CORR = pd.read_csv(FILE_PATH / 'error_correction_table.csv')
__ERR_CORR = __ERR_CORR.replace(np.nan, 0)
__GF = pd.read_csv(FILE_PATH / 'GF256.csv')
__ALIGNMENT = pd.read_csv(FILE_PATH / 'alignment_locations.csv', sep=' ')

#List with the GF256 values, idx is exponent of 2^n
GF256 = []
for index, row in __GF.iterrows():
    GF256.append(row['Value'])

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

#Error correction code words per block
ERR_CORR_CODEWORDS_BLOCK = {}
for version in pd.unique(__ERR_CORR['Version']):
    ERR_CORR_CODEWORDS_BLOCK[version] = {}
    for error in pd.unique(__ERR_CORR['Error Correction Level']):
        ERR_CORR_CODEWORDS_BLOCK[version][error] = 0

for index, row in __ERR_CORR.iterrows():
    ERR_CORR_CODEWORDS_BLOCK[row['Version']][row['Error Correction Level']] = row['Error Correction Codewords Per Block']

#Groups, blocks per group and data code words per block
GROUPS = {}
for version in pd.unique(__ERR_CORR['Version']):
    GROUPS[version] = {}
    for error in pd.unique(__ERR_CORR['Error Correction Level']):
        GROUPS[version][error] = 0

for index, row in __ERR_CORR.iterrows():
    GROUPS[row['Version']][row['Error Correction Level']] = {
        'GroupOne': {
            'Blocks': int(row['Group One Number of Blocks']),
            'CodewordsPerBlock': int(row['Group One Number of Data Codewords Per Block'])
        },
        'GroupTwo': {
            'Blocks': int(row['Group Two Number of Blocks']),
            'CodewordsPerBlock': int(row['Group Two Number of Data Codewords Per Block'])
        }
    }

#Alignment patterns
ALIGNMENT_PATTERNS = {}
for version in pd.unique(__ALIGNMENT['Version']):
    ALIGNMENT_PATTERNS[version] = []

for index, row in __ALIGNMENT.iterrows():
    locationsArray = row['CenterLocations'].split(',')
    locationsArray = [int(i) for i in locationsArray]
    ALIGNMENT_PATTERNS[row['Version']] = locationsArray

#Delete the CAPABILITIES and ERR_CORR dataframes
del __CAPABILITIES
del __ERR_CORR
del __GF
del __ALIGNMENT

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

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def multiply_polynomials(poly1Vals: list, poly1Exponents: list, poly2Vals: list, poly2Exponents: list) -> list:
    #1 - Convert the polynomials to GF notation
    poly1GF = []
    poly2GF = []
    for i in range(0, len(poly1Vals)):
        if poly1Vals[i] > 255:
            poly1GF.append(GF256.index(poly1Vals[i]%255))
        else:
            try:
                poly1GF.append(GF256.index(poly1Vals[i]))
            except:
                poly1GF.append(poly1Vals[i])

    for i in range(0, len(poly2Vals)):
        if poly2Vals[i] > 255:
            poly2GF.append(GF256.index(poly2Vals[i]%255))
        else:
            try:
                poly2GF.append(GF256.index(poly2Vals[i]))
            except:
                poly2GF.append(poly2Vals[i])

    #2 - Multiply the polynomials
    multResult = []
    multExpX = []
    for i in range(0, len(poly1GF)):
        for j in range(0, len(poly2GF)):
            multResult.append((poly1GF[i] + poly2GF[j])%255)
            multExpX.append(poly1Exponents[i] + poly2Exponents[j])

    # print(f"Mult GF terms: {multResult}")
    # print(f"Exponents: {multExpX}")

    #3 - Convert the result to integer notation
    intResult = []
    for i in multResult:
        intResult.append(GF256[i])

    #4 - Add the terms with the same exponent
    sumResult = []
    sumExpX = []
    for i in range(0, max(multExpX)+1):
        Idxs = find_indices(multExpX, i)

        #Skip if there list is empty
        if not Idxs:
            continue

        values = []
        for j in Idxs:
            values.append(intResult[j])

        if len(values) == 1:
            sumExp = values[0]
        else:
            sumExp = values[0] ^ values[1]

        sumResult.append(sumExp)
        sumExpX.append(i)
        # print(f"{i}: {Idxs}")

    return sumResult, sumExpX

#Function to generate the generator polynomial
def generator_polynomial(version: QRVersion, correction: QRErrorCorrectionLevels) -> list:
    n = ERR_CORR_CODEWORDS_BLOCK[version][correction]
    prevResult = [1, 1]  # Start with x + 1
    for N in range(1, n):
        termGF = [N, 0]  # Multiply previous term by (x - 2^N)

        #Convert prevResult to alpha notation
        prevGF = [0]*len(prevResult)
        for i in range(0, len(prevResult)):
            if prevResult[i] > 255:
                prevGF[i] = GF256.index(prevResult[i]%255)
            else:
                prevGF[i] = GF256.index(prevResult[i])

        # print(f"PrevGF: {prevGF}. TermGF: {termGF}")

        #Multiply the terms
        result = []
        expX = []
        pos0 = 0
        for i in termGF:
            for pos,j in enumerate(prevGF):
                result.append((i+j)%255)
                if pos0 == 0:
                    expX.append(pos)
                else:
                    expX.append(pos+1)

            pos0 += 1

        # print(f"Mult GF terms: {result}")
        # print(f"Exponents: {expX}")

        #Convert result to polynomial notation
        resultPoly = []
        for i in result:
            resultPoly.append(GF256[i])

        # print(f"Length of result: {len(result)}")
        # print(resultPoly)

        #Add all the terms with the same exponent
        sumTerms = []
        for i in range(0, len(resultPoly)):
            Idxs = find_indices(expX, i)
            # print(f"{i}: {Idxs}")

            #Skip if there list is empty
            if not Idxs:
                continue

            values = []
            for j in Idxs:
                values.append(resultPoly[j])

            if len(values) == 1:
                sumExp = values[0]
            else:
                sumExp = values[0] ^ values[1]

            sumTerms.append(sumExp)

        # print(f"Sum terms: {sumTerms}")

        prevResult = sumTerms

    return prevResult

#Function that returns number of remainder bits
def remainder_bits(version: QRVersion) -> int:
    if version > 1:
        if version <= 6:
            return 7
        elif version <= 13:
            return 0
        elif version <= 20:
            return 3
        elif version <= 27:
            return 4
        elif version <= 34:
            return 3
        elif version <= 40:
            return 0

def interleave_blocks(dataBlocks: list, errorCorrectionBlocks: list, version: QRVersion) -> list:
    interleavedData = []

    #Find max length of data blocks
    maxLength = 0
    for i in range(0, len(dataBlocks)):
        if len(dataBlocks[i]) > maxLength:
            maxLength = len(dataBlocks[i])

    #Interleave the data blocks
    for i in range(0, maxLength):
        for dataBlock in dataBlocks:
            if i < len(dataBlock):
                interleavedData.append(dataBlock[i])

    #Find max length of error correction blocks
    maxLength = 0
    for i in range(0, len(errorCorrectionBlocks)):
        if len(errorCorrectionBlocks[i]) > maxLength:
            maxLength = len(errorCorrectionBlocks[i])

    #Interleave the error correction blocks
    for i in range(0, maxLength):
        for errorBlock in errorCorrectionBlocks:
            if i < len(errorBlock):
                interleavedData.append(errorBlock[i])

    #Add remainder bits
    remainderBits = remainder_bits(version)
    if remainderBits:
        interleavedData.append('0'*remainderBits)

    return interleavedData

#Divide the polynomial by the generator polynomial
def divide_polynomials(message: list, generator: list, version: QRVersion, correction: QRErrorCorrectionLevels) -> list:
    divisions = []
    for messageDataBlock in message:
        dataCodewords = len(messageDataBlock)

        exponentsMessage = list(range(0, len(messageDataBlock)))
        exponentsGenerator = list(range(0, len(generator)))

        errCorrCodewords = ERR_CORR_CODEWORDS_BLOCK[version][correction]
        leadingExponentMessage = len(messageDataBlock) - 1

        # print(f"Message: {messageDataBlock}\nExponents: {exponentsMessage}")
        # print(f"Generator: {generator}\nExponents: {exponentsGenerator}")

        #Mult message poly by x^errCorrCodewords
        messageDataBlock, exponentsMessage = multiply_polynomials(messageDataBlock, exponentsMessage, [1], [errCorrCodewords])

        #Mult generator poly by x^leadingExponentMessage
        generator, exponentsGenerator = multiply_polynomials(generator, exponentsGenerator, [1], [leadingExponentMessage])

        # print(f"Message: [{len(messageDataBlock)}] {messageDataBlock}\nExponents: {exponentsMessage}")
        # print(f"Generator: [{len(generator)}] {generator}\nExponents: {exponentsGenerator}")

        prevResult = messageDataBlock
        prevExponents = exponentsMessage
        # print(f"Prev: [{len(messageDataBlock)}] {messageDataBlock}\nExponents: {exponentsMessage}")
        for i in range(dataCodewords):
            # print(f"Division {i+1}")
            #1 - Multiply the generator polynomial by the leading term of the message polynomial
            # print(prevResult)
            leadTerm = prevResult[-1]
            generatorMult, exponentsGenerator = multiply_polynomials(generator, exponentsGenerator, [leadTerm], [0])
            # print(f"  Lead term: {leadTerm}")
            # print(f"  Generator: [{len(generatorMult)}] {generatorMult}\n  Exponents: {exponentsGenerator}")

            #2 - XOR the result with the message polynomial
            XORResult = []
            XORExponents = []
            if len(generatorMult) > len(prevResult):
                for i in range(0, len(exponentsGenerator)):
                    if exponentsGenerator[i] in prevExponents:
                        idx = prevExponents.index(exponentsGenerator[i])
                        XORResult.append(generatorMult[i] ^ prevResult[idx])
                        XORExponents.append(exponentsGenerator[i])
                    else:
                        XORResult.append(generatorMult[i] ^ 0)
                        XORExponents.append(exponentsGenerator[i])
            else:
                for i in range(0, len(prevExponents)):
                    if prevExponents[i] in exponentsGenerator:
                        idx = exponentsGenerator.index(prevExponents[i])
                        XORResult.append(generatorMult[idx] ^ prevResult[i])
                        XORExponents.append(prevExponents[i])
                    else:
                        XORResult.append(prevResult[i] ^ 0)
                        XORExponents.append(prevExponents[i])

            # print(" After XOR")
            # print(f"  Generator: [{len(XORResult)}] {XORResult}\n  Exponents: {XORExponents}")

            #3 - Remove the leading 0 term
            XORResult.pop(-1)
            XORExponents.pop(-1)
            prevResult = XORResult
            prevExponents = XORExponents
            for i in range(0, len(exponentsGenerator)):
                exponentsGenerator[i] -= 1

        divisions.append(XORResult)

    return divisions
    
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
            'PadBytes': [],
        },
        'TotalLength': 0,
        'dataBytes': [],
        'ErrorCorrection': [],
    }
    totalLength = 0
    totalBits = ''

    count_indicator = qr_count_indicator(version, QREncoding.alphanumeric, data)

    blocks['Mode'] = QREncoding.alphanumeric.value
    blocks['CharacterCount'] = count_indicator
    totalLength += len(count_indicator)
    totalLength += len(QREncoding.alphanumeric.value)
    totalBits += QREncoding.alphanumeric.value
    totalBits += count_indicator

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
        totalBits += formatted

    dataBits = DATA_CODEWORDS[version][correction]*8
    remainderLength = dataBits - totalLength
    # print(remainderLength)
    # print(dataBits)

    #Extra padding

    #Terminator zeros (4 bits max)
    if remainderLength >= 4:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*4
        remainderLength -= 4
        totalLength += 4
        totalBits += '0'*4
    else:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*remainderLength
        remainderLength = 0
        totalLength += remainderLength
        totalBits += '0'*remainderLength

    #Add 0 until the length is a multiple of 8
    if remainderLength != 0 and remainderLength%8 != 0:
        blocks['ExtraPadding']['MultipleOf8'] = '0'*(remainderLength%8)
        totalBits += '0'*(remainderLength%8)

        totalLength += remainderLength%8
        remainderLength -= remainderLength%8

    #Padding bytes (8 bits per byte)
    if remainderLength != 8:
        padBytePos = 0
        while remainderLength >= 8:
            blocks['ExtraPadding']['PadBytes'].append(PAD_BYTES[padBytePos%2])
            remainderLength -= 8
            totalLength += 8
            totalBits += PAD_BYTES[padBytePos%2]
            
            padBytePos += 1

    blocks['TotalLength'] = totalLength

    blockInfo = GROUPS[version][correction]
    g1Blocks = blockInfo['GroupOne']['Blocks']
    g1CodewordsPerBlock = blockInfo['GroupOne']['CodewordsPerBlock']
    g2Blocks = blockInfo['GroupTwo']['Blocks']
    g2CodewordsPerBlock = blockInfo['GroupTwo']['CodewordsPerBlock']

    #Split the data in bytes
    pos = 0
    for i in range(0, g1Blocks):
        codewords = []
        for j in range(pos, pos+g1CodewordsPerBlock*8, 8):
            codewords.append(totalBits[j:j+8])

        blocks['dataBytes'].append(codewords)
        pos += g1CodewordsPerBlock*8

    if g2Blocks:
        for i in range(0, g2Blocks):
            codewords = []
            for j in range(pos, pos+g2CodewordsPerBlock*8, 8):
                codewords.append(totalBits[j:j+8])
            
            blocks['dataBytes'].append(codewords)
            pos += g2CodewordsPerBlock*8

    #Error correction using Reed-Solomon algorithm
    # print(blockInfo)

    singleListBytes = []
    for i in range(0, len(totalBits), 8):
        singleListBytes.append(totalBits[i:i+8])

    #Message polynomial
    messagePolynomial = []
    codewordIdx = 0
    for _ in range(0, blockInfo['GroupOne']['Blocks']):
        blockPolynomial = []
        for _ in range(0, blockInfo['GroupOne']['CodewordsPerBlock']):
            codeword = singleListBytes[codewordIdx]
            blockPolynomial.append(int(codeword, 2))

            codewordIdx += 1

        #Flip the block polynomial and append it to the message polynomial
        blockPolynomial.reverse()
        messagePolynomial.append(blockPolynomial)

    # blocks['ErrorCorrection']['GroupOne'] = messagePolynomial
    # messagePolynomial = []

    if blockInfo['GroupTwo']['Blocks']:
        for _ in range(0, blockInfo['GroupTwo']['Blocks']):
            blockPolynomial = []
            for _ in range(0, blockInfo['GroupTwo']['CodewordsPerBlock']):
                codeword = singleListBytes[codewordIdx]
                blockPolynomial.append(int(codeword, 2))

                codewordIdx += 1

            #Flip the block polynomial and append it to the message polynomial
            blockPolynomial.reverse()
            messagePolynomial.append(blockPolynomial)
            
    # blocks['ErrorCorrection']['GroupTwo'] = messagePolynomial

    #Generator polynomial
    generatorPolynomial = generator_polynomial(version, correction)

    #Divide the message polynomial by the generator polynomial
    remainder = divide_polynomials(messagePolynomial, generatorPolynomial, version, correction)

    #Turn remainder to list of 8 bit strings
    for i in range(0, len(remainder)):
        # print(len(remainder[i]))
        for j in range(0, len(remainder[i])):
            remainder[i][j] = '{0:08b}'.format(remainder[i][j])

        #Flip the remainder
        remainder[i].reverse()

    blocks['ErrorCorrection'] = remainder

    return blocks

def qr_encode_data_byte(version: QRVersion, correction: QRErrorCorrectionLevels, data: str) -> list:
    # blocks = {
    #     'Mode': '',
    #     'CharacterCount': '',
    #     'Data': []
    # }
    # count_indicator = qr_count_indicator(version, QREncoding.byte, data)

    # blocks['Mode'] = QREncoding.byte
    # blocks['CharacterCount'] = count_indicator

    # #split the data in bytes
    # for i in range(0, len(data)):
    #     byte = ord(data[i])
    #     # print(byte)
    #     formatted = '{0:08b}'.format(byte)

    #     blocks['Data'].append(formatted)

    # return blocks

    blocks = {
        'Mode': '',
        'CharacterCount': '',
        'Data': [],
        'ExtraPadding': {
            'TerminatorZeros': '',
            'MultipleOf8': '',
            'PadBytes': [],
        },
        'TotalLength': 0,
        'dataBytes': [],
        'ErrorCorrection': [],
    }
    totalLength = 0
    totalBits = ''

    count_indicator = qr_count_indicator(version, QREncoding.byte, data)

    blocks['Mode'] = QREncoding.byte.value
    blocks['CharacterCount'] = count_indicator
    totalLength += len(count_indicator)
    totalLength += len(QREncoding.byte.value)
    totalBits += QREncoding.byte.value
    totalBits += count_indicator
    
    for i in range(0, len(data)):
        byte = ord(data[i])
        # print(byte)
        formatted = '{0:08b}'.format(byte)

        blocks['Data'].append(formatted)
        totalLength += len(formatted)
        totalBits += formatted

    dataBits = DATA_CODEWORDS[version][correction]*8
    remainderLength = dataBits - totalLength
    # print(remainderLength)
    # print(dataBits)

    #Extra padding

    #Terminator zeros (4 bits max)
    if remainderLength >= 4:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*4
        remainderLength -= 4
        totalLength += 4
        totalBits += '0'*4
    else:
        blocks['ExtraPadding']['TerminatorZeros'] = '0'*remainderLength
        remainderLength = 0
        totalLength += remainderLength
        totalBits += '0'*remainderLength

    #Add 0 until the length is a multiple of 8
    if remainderLength != 0 and remainderLength%8 != 0:
        blocks['ExtraPadding']['MultipleOf8'] = '0'*(remainderLength%8)
        totalBits += '0'*(remainderLength%8)

        totalLength += remainderLength%8
        remainderLength -= remainderLength%8

    #Padding bytes (8 bits per byte)
    if remainderLength != 8:
        padBytePos = 0
        while remainderLength >= 8:
            blocks['ExtraPadding']['PadBytes'].append(PAD_BYTES[padBytePos%2])
            remainderLength -= 8
            totalLength += 8
            totalBits += PAD_BYTES[padBytePos%2]
            
            padBytePos += 1

    blocks['TotalLength'] = totalLength

    blockInfo = GROUPS[version][correction]
    g1Blocks = blockInfo['GroupOne']['Blocks']
    g1CodewordsPerBlock = blockInfo['GroupOne']['CodewordsPerBlock']
    g2Blocks = blockInfo['GroupTwo']['Blocks']
    g2CodewordsPerBlock = blockInfo['GroupTwo']['CodewordsPerBlock']

    #Split the data in bytes
    pos = 0
    for i in range(0, g1Blocks):
        codewords = []
        for j in range(pos, pos+g1CodewordsPerBlock*8, 8):
            codewords.append(totalBits[j:j+8])

        blocks['dataBytes'].append(codewords)
        pos += g1CodewordsPerBlock*8

    if g2Blocks:
        for i in range(0, g2Blocks):
            codewords = []
            for j in range(pos, pos+g2CodewordsPerBlock*8, 8):
                codewords.append(totalBits[j:j+8])
            
            blocks['dataBytes'].append(codewords)
            pos += g2CodewordsPerBlock*8

    #Error correction using Reed-Solomon algorithm
    # print(blockInfo)

    singleListBytes = []
    for i in range(0, len(totalBits), 8):
        singleListBytes.append(totalBits[i:i+8])

    #Message polynomial
    messagePolynomial = []
    codewordIdx = 0
    for _ in range(0, blockInfo['GroupOne']['Blocks']):
        blockPolynomial = []
        for _ in range(0, blockInfo['GroupOne']['CodewordsPerBlock']):
            codeword = singleListBytes[codewordIdx]
            blockPolynomial.append(int(codeword, 2))

            codewordIdx += 1

        #Flip the block polynomial and append it to the message polynomial
        blockPolynomial.reverse()
        messagePolynomial.append(blockPolynomial)

    # blocks['ErrorCorrection']['GroupOne'] = messagePolynomial
    # messagePolynomial = []

    if blockInfo['GroupTwo']['Blocks']:
        for _ in range(0, blockInfo['GroupTwo']['Blocks']):
            blockPolynomial = []
            for _ in range(0, blockInfo['GroupTwo']['CodewordsPerBlock']):
                codeword = singleListBytes[codewordIdx]
                blockPolynomial.append(int(codeword, 2))

                codewordIdx += 1

            #Flip the block polynomial and append it to the message polynomial
            blockPolynomial.reverse()
            messagePolynomial.append(blockPolynomial)

    # blocks['ErrorCorrection']['GroupTwo'] = messagePolynomial

    #Generator polynomial
    generatorPolynomial = generator_polynomial(version, correction)

    #Divide the message polynomial by the generator polynomial
    remainder = divide_polynomials(messagePolynomial, generatorPolynomial, version, correction)

    #Turn remainder to list of 8 bit strings
    for i in range(0, len(remainder)):
        # print(len(remainder[i]))
        for j in range(0, len(remainder[i])):
            remainder[i][j] = '{0:08b}'.format(remainder[i][j])

        #Flip the remainder
        remainder[i].reverse()

    blocks['ErrorCorrection'] = remainder

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
        return qr_encode_data_byte(version, correction, data)
    elif encoding == QREncoding.kanji:
        return None

def alignment_pattern_locations(version: QRVersion) -> list:
    if version != 1:
        positions = ALIGNMENT_PATTERNS[version]
    else:
        positions = []

    locations = []

    for i in positions:
        for j in positions:
            #Skip if position is on top of the finder patterns
            if (i == 6 and j == 6) or (i == 6 and j == (qr_size(version)-7)) or (i == (qr_size(version)-7) and j == 6):
                continue

            locations.append((i, j))

    return locations

def calculate_penalty_score(moduleMatrix: list) -> int:
    pass

def apply_mask(moduleMatrix: list, mask: int, reservedPositions: list) -> list:
    if mask > 7:
        raise Exception('The mask number must be between 0 and 7.')
    
    if mask == 0:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if (posRow + posCol)%2 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 1:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if posRow%2 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 2:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if posCol%3 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 3:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if (posRow + posCol)%3 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 4:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if (posRow//2 + posCol//3)%2 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 5:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if (posRow*posCol)%2 + (posRow*posCol)%3 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 6:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if ((posRow*posCol)%2 + (posRow*posCol)%3)%2 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
    elif mask == 7:
        for posRow, row in enumerate(moduleMatrix):
            for posCol, col in enumerate(row):
                if ((posRow + posCol)%2 + (posRow*posCol)%3)%2 == 0 and reservedPositions[posRow][posCol] == 0:
                    moduleMatrix[posRow][posCol] = 1 if col == 0 else 0
        
    return moduleMatrix


#Function to do the qr masking
def qr_masking(data: list, reservedPositions: list) -> list:
    if len(data) != len(reservedPositions):
        raise Exception('The data and reserved positions lists must have the same length.')
    
    #Apply all 8 masks and calculate the penalty score
    penaltyScores = []
    maskedPatterns = []

    for i in range(0, 8):
        maskedData = apply_mask(data, i, reservedPositions)
        maskedPatterns.append(maskedData)
        penaltyScores.append(calculate_penalty_score(maskedData))
