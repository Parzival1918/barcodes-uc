from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from typing import Union

# from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from barcodes_uc.qrcodes.qrgenerator import get_encoding, get_min_version, smallest_qr, QRGenerator
from barcodes_uc.qrcodes.qrutils import QREncoding, QRVersion, QRErrorCorrectionLevels
from enum import Enum
from PIL import Image
import numpy as np
import base64

tags_metadata = [
    {
        "name": "QR Data",
        "description": "Obtain the data of the QR code.",
    },
    {
        "name": "QR Image",
        "description": "Obtain the information of the QR code and the image in base64.",
    },
]

description = """
**Generate QR codes** from text, obtain the data or also the QR image formatted in base64.

This API is based on the [barcodes_uc](https://pypi.org/project/barcodes-uc/) python package.

Find alternative documentation in [alt-docs](/alt-docs).
"""

app = FastAPI(
    title="qrgenerator-api",
    description=description,
    version="0.1.0",
    contact={
        "name": "Pedro Juan Royo",
        "url": "https://github.com/Parzival1918?tab=repositories",
        "email": "pedro.juan.royo@gmail.com",
    },
    openapi_tags=tags_metadata,
    docs_url="/",
    redoc_url="/alt-docs",
    )

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

def generateQRforAPI(message: str, encoding: Union[Encoding, None], qr_version: Union[int, None], qr_error_correction: Union[ErrorCorrection, None],
                     getMasks: bool = False, mask: Union[int, None] = None):
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

    if getMasks:
        qr, allMasks, penaltyScores = QRGenerator(msg=message, encoding=encoding, version=version, error_correction=error_correction).generate(returnALL=True)
        qr.matrix = allMasks[mask]
        penaltyScore = penaltyScores[mask]
    else:
        qr = QRGenerator(msg=message, encoding=encoding, version=version, error_correction=error_correction).generate()
        penaltyScore = None
        
    return qr, version, error_correction, encoding, penaltyScore

    # # Add quiet zone
    # qrQuieZone = [[0 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    # for i in range(qr.size):
    #     for j in range(qr.size):
    #         qrQuieZone[i + 4][j + 4] = qr.matrix[i][j]

@app.get("/qrdata/{message}/{mask}", tags=["QR Data"])
def qr_data_from_message_and_mask(message: str, mask: int, encoding: Union[Encoding, None] = None, qr_version: Union[int, None] = None, qr_error_correction: Union[ErrorCorrection, None] = None):
    if mask < 0 or mask > 7:
        raise HTTPException(status_code=402, detail="Mask must be in range [0-7]")
    
    qr, version, error_correction, encoding, penalty = generateQRforAPI(message, encoding, qr_version, qr_error_correction, getMasks=True, mask=mask)

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
        "mask": mask,
        "penalty_score": penalty,
        "qr": qrQuieZone
        }

@app.get("/qrdata/{message}", tags=["QR Data"])
def qr_data_from_message(message: str, encoding: Union[Encoding, None] = None, qr_version: Union[int, None] = None, qr_error_correction: Union[ErrorCorrection, None] = None):
    qr, version, error_correction, encoding, _ = generateQRforAPI(message, encoding, qr_version, qr_error_correction)

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

@app.get("/qrimg/{message}/{mask}", tags=["QR Image"])
def qr_img_from_message_and_mask(message: str, mask: int, encoding: Union[Encoding, None] = None, qr_version: Union[int, None] = None, qr_error_correction: Union[ErrorCorrection, None] = None, imgSize: Union[int, None] = None):
    if mask < 0 or mask > 7:
        raise HTTPException(status_code=402, detail="Mask must be in range [0-7]")

    qr, version, error_correction, encoding, penalty = generateQRforAPI(message, encoding, qr_version, qr_error_correction, getMasks=True, mask=mask)

    # Add quiet zone
    qrQuieZone = [[1 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    for i in range(qr.size):
        for j in range(qr.size):
            qrQuieZone[i + 4][j + 4] = 1 if qr.matrix[i][j] == 0 else 0

    # Convert to image
    pixels = np.array(qrQuieZone, dtype=np.uint8)*255
    image = Image.fromarray(pixels)
    if not imgSize:
        imgSize = 500

    if imgSize < qr.size:
        raise HTTPException(status_code=401, detail="Image size must be greater than QR size")

    image = image.resize((imgSize, imgSize), Image.NEAREST)

    # Convert to base64
    imgBase64 = base64.b64encode(image.tobytes())
    
    return {
        "message": message,
        "encoding": encoding.name,
        "qr_version": version.value,
        "qr_error_correction": error_correction,
        "mask": mask,
        "penalty_score": penalty,
        "img": {
            "size": imgSize,
            "base64": imgBase64.decode("utf-8") # Decode to string
        }
    }

@app.get("/qrimg/{message}", tags=["QR Image"])
def qr_img_from_message(message: str, encoding: Union[Encoding, None] = None, qr_version: Union[int, None] = None, qr_error_correction: Union[ErrorCorrection, None] = None, imgSize: Union[int, None] = None):
    qr, version, error_correction, encoding, _ = generateQRforAPI(message, encoding, qr_version, qr_error_correction)

    # Add quiet zone
    qrQuieZone = [[1 for _ in range(qr.size + 8)] for _ in range(qr.size + 8)]
    for i in range(qr.size):
        for j in range(qr.size):
            qrQuieZone[i + 4][j + 4] = 1 if qr.matrix[i][j] == 0 else 0

    # Convert to image
    pixels = np.array(qrQuieZone, dtype=np.uint8)*255
    image = Image.fromarray(pixels)
    if not imgSize:
        imgSize = 500

    if imgSize < qr.size:
        raise HTTPException(status_code=401, detail="Image size must be greater than QR size")

    image = image.resize((imgSize, imgSize), Image.NEAREST)

    # Convert to base64
    imgBase64 = base64.b64encode(image.tobytes())
    
    return {
        "message": message,
        "encoding": encoding.name,
        "qr_version": version.value,
        "qr_error_correction": error_correction,
        "img": {
            "size": imgSize,
            "base64": imgBase64.decode("utf-8") # Decode to string
        }
    }