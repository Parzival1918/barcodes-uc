from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

# from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from barcodes_uc.qrcodes.qrgenerator import get_encoding, get_min_version, smallest_qr, QRGenerator
from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from enum import Enum
from PIL import Image
import numpy as np

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

def generateQRforAPI(message: str, encoding: Encoding | None, qr_version: int | None, qr_error_correction: ErrorCorrection | None):
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

    # # Add quiet zone
    # qrQuieZone = [[0 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    # for i in range(qr.size):
    #     for j in range(qr.size):
    #         qrQuieZone[i + 4][j + 4] = qr.matrix[i][j]

    return qr, version, error_correction, encoding


@app.get("/qrdata-from-message/{message}")
def qr_from_message(message: str, encoding: Encoding | None = None, qr_version: int | None = None, qr_error_correction: ErrorCorrection | None = None):
    qr, version, error_correction, encoding = generateQRforAPI(message, encoding, qr_version, qr_error_correction)

    # Add quiet zone
    qrQuieZone = [[0 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    for i in range(qr.size):
        for j in range(qr.size):
            qrQuieZone[i + 4][j + 4] = qr.matrix[i][j]
        
    return {
        "message": message,
        "encoding": encoding.name,
        "qr_version": version.value,
        "qr_error_correction": error_correction,
        "qr": qrQuieZone
        }

@app.get("/qrimg-from-message/{message}")
def qr_img_from_message(message: str, encoding: Encoding | None = None, qr_version: int | None = None, qr_error_correction: ErrorCorrection | None = None, imgSize: int | None = None):
    qr, version, error_correction, encoding = generateQRforAPI(message, encoding, qr_version, qr_error_correction)

    # Add quiet zone
    qrQuieZone = [[0 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    for i in range(qr.size):
        for j in range(qr.size):
            qrQuieZone[i + 4][j + 4] = qr.matrix[i][j]

    # Convert to image
    pixels = np.array(qrQuieZone, dtype=np.uint8)*255
    image = Image.fromarray(pixels)
    if not imgSize:
        imgSize = 500
    image = image.resize((imgSize, imgSize), Image.NEAREST)
    
    return FileResponse(image.tobytes(), media_type="image/png")
