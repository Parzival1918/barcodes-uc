from barcodes_uc.qrcodes import qrutils
from barcodes_uc.qrcodes import qrgenerator
import importlib
importlib.reload(qrutils)
importlib.reload(qrgenerator)

# generator = qrgenerator.QRGenerator(msg="https://github.com/Parzival1918", encoding=qrutils.QREncoding.byte, version=qrutils.QRVersion.v5, error_correction=qrutils.QRErrorCorrectionLevels.Q)
generator = qrgenerator.QRGenerator(msg="HELLO WORLD", encoding=qrutils.QREncoding.alphanumeric, version=qrutils.QRVersion.v1, error_correction=qrutils.QRErrorCorrectionLevels.Q)

qr = generator.generate()
qr.show()

generator = qrgenerator.QRGenerator(msg="HELLO WORLD", encoding=qrutils.QREncoding.alphanumeric, version=qrutils.QRVersion.v2, error_correction=qrutils.QRErrorCorrectionLevels.H)

qr = generator.generate()
qr.show()