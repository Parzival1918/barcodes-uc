from fastapi import FastAPI

# from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
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
    return {"test": message}