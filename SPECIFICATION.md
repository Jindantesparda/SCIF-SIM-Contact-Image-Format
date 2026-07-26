# SCIF File Specification v1.0

## Header

The first contact stores metadata.

Name

```
SCIFV1
```

Number

```
WWWWHHHH
```

Example

```
00600064
```

means

```
Width = 60
Height = 64
```

---

## Image Data

Each remaining contact stores

Name

```
20 hexadecimal characters
```

Number

```
20 digits
```

Currently reserved.

---

## Pixel Encoding

```
0  -> 0
1  -> 1
...
9  -> 9
10 -> A
11 -> B
12 -> C
13 -> D
14 -> E
15 -> F
```

---

## Image Pipeline

PNG

↓

Grayscale

↓

16-level Quantization

↓

Hexadecimal Stream

↓

SIM Contacts

↓

SCIF File

---

## Version

Current Version

```
SCIFV1
```