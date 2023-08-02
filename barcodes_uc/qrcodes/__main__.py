# CLI for creating QR codes

#imports
import argparse
from . import qrgenerator, qrutils

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Create QR codes', prog='qrcode', epilog='Made by Pedro Juan Royo, @UnstrayCato')

    # Add the arguments
    parser.add_argument('message', metavar='message', type=str, help='Message to encode')
    parser.add_argument('-e', '--encoding', type=str, help='Encoding of the message', choices=['byte', 'numeric', 'alphanumeric', 'kanji'], required=True)
    parser.add_argument('-V', '--qr-version', type=int, help='QR version, 1-40')
    parser.add_argument('-E', '--qr-error-correction', help='QR error correction', choices=['L', 'M', 'Q', 'H'])

    # Execute the parse_args() method
    args = parser.parse_args()
    
    encoding = qrutils.QREncoding[args.encoding]

    if args.qr_version and args.qr_error_correction:
        version = qrutils.QRVersion[args.qr_version]
        error_correction = qrutils.QRErrorCorrectionLevels[args.qr_error_correction]
        generator = qrgenerator.QRGenerator(args.message, encoding, version, error_correction)
    else:
        version, error_correction = qrgenerator.get_min_version(args.message, encoding, qrutils.QRErrorCorrectionLevels.Q)
        generator = qrgenerator.QRGenerator(args.message, encoding, version, error_correction)

    qr = generator.generate()
    qr.show()

if __name__ == '__main__':
    main()