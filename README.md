# SCIF (SIM Contact Image Format)

> A custom image file format that stores image data inside SIM card contacts.

SCIF is an experimental file format that explores an unusual storage medium: the contact storage available on a SIM card.

Instead of saving an image as a PNG or JPEG, SCIF encodes image data into SIM contact records and reconstructs the original image by decoding those contacts.

This project investigates custom file format design, data serialization, constrained storage systems, and compression techniques.

---

## Why?

Traditional image formats assume access to a filesystem.

SCIF asks a different question:

> Can a SIM card's contact storage be used as an image storage medium?

The goal is to design a complete image format around the limitations of SIM contacts.

---

## Version Roadmap

### SCIF v1
- Grayscale images
- 16 grayscale levels
- Virtual SIM card
- Custom encoder
- Custom decoder
- Metadata contact
- Exact reconstruction

### SCIF v2
- Utilize phone number fields for additional storage
- Improved metadata
- Error detection

### SCIF v3
- Custom compression
- Reduced storage requirements
- Improved encoding efficiency

### SCIF v4
- Color image support

### SCIF v5
- Optimized mixed-alphabet encoding
- Maximum storage efficiency

---

## Project Structure

```
SCIF/
│
├── images/
│   ├── input/
│   └── output/
│
├── scif/
│   ├── contact.py
│   ├── simcard.py
│   ├── encoder.py
│   ├── decoder.py
│   ├── imageutils.py
│   └── constants.py
│
├── tests/
│
├── main.py
└── README.md
```

---

## Example Pipeline

```
Image
   │
   ▼
Load Image
   │
   ▼
Convert to Grayscale
   │
   ▼
Reduce to 16 Shades
   │
   ▼
Encode
   │
   ▼
Virtual SIM Contacts
   │
   ▼
Decode
   │
   ▼
Recovered Image
```

---

## Current Status

🚧 Under Development

The current focus is implementing SCIF Version 1.

---

## Technologies

- Python
- Pillow
- Object-Oriented Programming
- Custom File Format Design

---

## License

MIT License
