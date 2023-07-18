
#imports
from . import qrinfo

finderPattern = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]

alignmentPattern = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

class QR:
    def __init__(self, version: qrinfo.QRVersion = qrinfo.QRVersion.v1) -> None:
        self.size = qrinfo.qr_size(version)
        self.version = version
        self.matrix = [['X' for i in range(self.size)] for j in range(self.size)]

    # def set_size(self, size: int):
    #     self.size = size
    #     self.matrix = [[0 for i in range(size)] for j in range(size)]

    def __str__(self): #TODO: Make this look better
        buildString = ""
        for row in self.matrix:
            for col in row:
                buildString += str(col)
            buildString += "\n"

        return buildString

class QRGenerator:
    def __init__(self, msg: str = "Hello World", encoding: qrinfo.QREncoding = qrinfo.QREncoding.byte, version: qrinfo.QRVersion = qrinfo.QRVersion.v1, error_correction: qrinfo.QRErrorCorrectionLevels = qrinfo.QRErrorCorrectionLevels.L):
        self.msg = msg
        self.encoding = encoding
        self.version = version
        self.error_correction = error_correction

    def __str__(self):
        return f"QR(msg={self.msg}, encoding={self.encoding}, version={self.version}, error_correction={self.error_correction})"
    
    def __repr__(self):
        return f"QR(msg={self.msg}, encoding={self.encoding}, version={self.version}, error_correction={self.error_correction})"
    
    def check(self):
        max_character_count = qrinfo.MAX_CHARACTERS[qrinfo.QREncoding(self.encoding).name][self.error_correction][self.version]

        if len(self.msg) >= max_character_count:
            return False
        else:
            return True
        
    def generate(self):
        # if not self.check():
        #     raise ValueError("Message is too long for the specified encoding, version and error correction level.")
        rawData = qrinfo.qr_encode_data(self.version, self.encoding, self.error_correction, self.msg)
        # print(rawData)

        #interleave data blocks and error correction blocks if necessary
        interleavedData = qrinfo.interleave_blocks(rawData['dataBytes'], rawData['ErrorCorrection'])

        #Place the modules and function patterns in the matrix
        qr = QR(version=self.version)
        # print(qr)

        #1 - Place the finder patterns, at (0,0), (0, qr.size - 7), (qr.size - 7, 0)
        #(0,0)
        for posx,row in enumerate(finderPattern):
            for posy,col in enumerate(row):
                qr.matrix[posx][posy] = col

        #(0, qr.size - 7)
        for posx,row in enumerate(finderPattern):
            for posy,col in enumerate(row):
                qr.matrix[posx][qr.size - 7 + posy] = col

        #(qr.size - 7, 0)
        for posx,row in enumerate(finderPattern):
            for posy,col in enumerate(row):
                qr.matrix[qr.size - 7 + posx][posy] = col

        #2 - Add the separators
        #2.1 - Top left
        for i in range(8):
            qr.matrix[i][7] = 0
        for i in range(8):
            qr.matrix[7][i] = 0

        #2.2 - Top right
        for i in range(8):
            qr.matrix[i][qr.size - 8] = 0
        for i in range(8):
            qr.matrix[7][qr.size - 1 - i] = 0

        #2.3 - Bottom left
        for i in range(8):
            qr.matrix[qr.size - 8 + i][7] = 0
        for i in range(8):
            qr.matrix[qr.size - 8][i] = 0

        #3 - Add timing patterns
        #Horizontal
        value = 1
        for i in range(8, qr.size - 8):
            qr.matrix[6][i] = value%2
            value += 1

        #Vertical
        value = 1
        for i in range(8, qr.size - 8):
            qr.matrix[i][6] = value%2
            value += 1

        #4 - Add alignment patterns
        patternLocations = qrinfo.alignment_pattern_locations(self.version)

        for patternLocation in patternLocations:
            posx = patternLocation[0]
            posy = patternLocation[1]
            #Put pattern at center posx, posy
            offset = [-2, -1, 0, 1, 2]
            for i in range(5):
                for j in range(5):
                    qr.matrix[posx + offset[i]][posy + offset[j]] = alignmentPattern[i][j]

        #5 - Add dark module
        qr.matrix[qr.size - 8][8] = 1

        #6 - Reserve format information area
        #Top-left
        for i in range(9):
            if i != 6:
                qr.matrix[i][8] = 'x'
        for i in range(9):
            if i != 6:
                qr.matrix[8][i] = 'x'
        
        #Top-right
        for i in range(1,9):
            qr.matrix[8][qr.size - i] = 'x'

        #Bottom-left
        for i in range(1,8):
            qr.matrix[qr.size - i][8] = 'x'

        #7 - Reserve version information area

        #8 - Add data

        print(qr)

        return interleavedData



            