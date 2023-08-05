from fastapi import FastAPI, HTTPException

# from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from barcodes_uc.qrcodes.qrgenerator import get_encoding, get_min_version, smallest_qr, QRGenerator
from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from enum import Enum

app = FastAPI()

class Encoding(str, Enum):
    byte = "byte"
    numeric = "numeric"
    alphanumeric = "alphanumeric"
    kanji = "kanji"

class ErrorCorrection(str, Enum):
    L = "L"
    M = "M"
    Q = "Q"
    H = "H"

@app.get("/qr-from-message/{message}")
def qr_from_message(message: str, encoding: Encoding | None = None, qr_version: int | None = None, qr_error_correction: ErrorCorrection | None = None):
    if encoding:
        encoding = QREncoding[encoding]
    else:
        encoding = get_encoding(message)

    print(message, encoding)

    if qr_version:
        if qr_version < 1 or qr_version > 40:
            raise HTTPException(status_code=400, detail="Version must be in range [1-40]")
        
        version = QRVersion(qr_version)
    
    if qr_error_correction:
        error_correction = QRErrorCorrectionLevels[qr_error_correction]
    else:
        error_correction = QRErrorCorrectionLevels.Q

    if not qr_version:
        version, error_correction = get_min_version(message, encoding, error_correction)

    qr = QRGenerator(msg=message, encoding=encoding, version=version, error_correction=error_correction).generate()
        
    return {
        "message": message,
        "encoding": encoding.name,
        "qr_version": version.value,
        "qr_error_correction": error_correction,
        "qr": qr.matrix
        }