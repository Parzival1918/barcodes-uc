
#imports
from . import qrinfo

class QR:
    def __init__(self, msg: str = "Hello World", encoding: qrinfo.QREncoding = qrinfo.QREncoding.byte, version: qrinfo.QRVersion = qrinfo.QRVersion.version1, error_correction: qrinfo.QRErrorCorrectionLevels = qrinfo.QRErrorCorrectionLevels.L):
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
        if not self.check():
            raise ValueError("Message is too long for the specified encoding, version and error correction level.")
            