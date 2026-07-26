# SCIF
### SIM Contact Image Format

A custom image file format that stores grayscale image data inside SIM card contact records.

SCIF demonstrates how image data can be serialized into fixed-length contact entries, reconstructed later, and transported as a portable `.scif` file.

---

## Features

- Custom image encoder
- Custom image decoder
- Portable `.scif` file format
- Virtual SIM card simulation
- Verification system
- Storage statistics
- Human-readable file format

---

## Architecture

```
PNG Image
     │
     ▼
Grayscale Conversion
     │
     ▼
4-bit Quantization
     │
     ▼
SCIF Encoder
     │
     ▼
SIM Contacts
     │
     ▼
.scif File
     │
     ▼
SCIF Loader
     │
     ▼
SCIF Decoder
     │
     ▼
PNG Image
```

---

## Example Output

```
✓ Verification Passed

Version            : SCIFV1
Width              : 60
Height             : 64
Pixels             : 3840
Contacts Used      : 193/250
SIM Usage          : 77.20%
```

---

## Example SCIF File

```
SCIFV1,00600064
FFFFFFFFFFFFFFFFFFFF,00000000000000000000
FFFFFFFFFFFEEECCCAA,00000000000000000000
...
```

---

## Project Structure

```
scif/
├── contact.py
├── simcard.py
├── encoder.py
├── decoder.py
├── imageutils.py
├── inspector.py
├── verifier.py
└── fileio.py
```

---

## Future Work

- Binary SCIF format
- Compression
- RGB support
- Error correction
- Phone number storage
- Metadata expansion
- Encryption

---

## License

MIT