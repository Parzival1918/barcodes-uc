
#imports
from . import qrinfo

class QR:
    def __init__(self, size: int = 21) -> None:
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)]

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
        print(rawData)

        #interleave data blocks and error correction blocks if necessary
        interleavedData = qrinfo.interleave_blocks(rawData['dataBytes'], rawData['ErrorCorrection'])

        #Place the modules and function patterns in the matrix
        qr = QR(size=qrinfo.qr_size(self.version))
        print(qr.matrix)
        print(qr)


        return interleavedData



            