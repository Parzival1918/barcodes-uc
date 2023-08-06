from barcodes_uc.qrcodes import qrutils
from barcodes_uc.qrcodes import qrgenerator
import importlib
importlib.reload(qrutils)
importlib.reload(qrgenerator)

# # generator = qrgenerator.QRGenerator(msg="https://github.com/Parzival1918", encoding=qrutils.QREncoding.byte, version=qrutils.QRVersion.v5, error_correction=qrutils.QRErrorCorrectionLevels.Q)
# generator = qrgenerator.QRGenerator(msg="HELLO WORLD", encoding=qrutils.QREncoding.alphanumeric, version=qrutils.QRVersion.v1, error_correction=qrutils.QRErrorCorrectionLevels.Q)

# qr = generator.generate()
# qr.show()

# generator = qrgenerator.QRGenerator(msg="HELLO WORLD", encoding=qrutils.QREncoding.alphanumeric, version=qrutils.QRVersion.v2, error_correction=qrutils.QRErrorCorrectionLevels.H)

# qr = generator.generate()
# qr.show()

# msg = "I AM PEDRO"
# version, err = qrgenerator.get_min_version(msg, qrutils.QREncoding.alphanumeric, qrutils.QRErrorCorrectionLevels.Q)
# print(version, err)
# qr = qrgenerator.QRGenerator(msg=msg, encoding=qrutils.QREncoding.alphanumeric, version=version, error_correction=err)
# ans = qr.generate()
# ans.show()

# qr = qrgenerator.QRGenerator(msg="8675309", encoding=qrutils.QREncoding.numeric, version=qrutils.QRVersion.v1, error_correction=qrutils.QRErrorCorrectionLevels.Q)
# ans = qr.generate()
# ans.show()

# msg = "Ah, this a TEST! 99% of the time, it works every time."
# version, err = qrgenerator.get_min_version(msg, qrutils.QREncoding.byte, qrutils.QRErrorCorrectionLevels.Q)
# print(version, err)
# qr = qrgenerator.QRGenerator(msg=msg, encoding=qrutils.QREncoding.byte, version=version, error_correction=err)
# ans = qr.generate()
# ans.show()

# msg = "私はペドロです。"
# version, err = qrgenerator.get_min_version(msg, qrutils.QREncoding.kanji, qrutils.QRErrorCorrectionLevels.Q)
# print(version, err)
# qr = qrgenerator.QRGenerator(msg=msg, encoding=qrutils.QREncoding.kanji, version=version, error_correction=err)
# ans = qr.generate()
# ans.show()

# msg = "ABC test"
# # msg = "1234567890"
# qr = qrgenerator.smallest_qr(msg, qrutils.QRErrorCorrectionLevels.Q)
# print(qr.version, qr.encoding, qr.error_correction)
# qr.show()

msg = "https://qrgeneratorapi-1-c9139268.deta.app/"
print(msg)
qr = qrgenerator.smallest_qr(msg, qrutils.QRErrorCorrectionLevels.Q)
print(qr.version, qr.encoding, qr.error_correction)
qr.show()
# qr.save()