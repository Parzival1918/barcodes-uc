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

msg = "I AM PEDRO"
version, err = qrgenerator.get_min_version(msg, qrutils.QREncoding.alphanumeric, qrutils.QRErrorCorrectionLevels.Q)
print(version, err)
qr = qrgenerator.QRGenerator(msg=msg, encoding=qrutils.QREncoding.alphanumeric, version=version, error_correction=err)
ans = qr.generate()
ans.show()