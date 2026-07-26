from pathlib import Path

from scif.decoder import ScifDecoder
from scif.encoder import ScifEncoder
from scif.imageutils import ImageUtils
from scif.inspector import ScifInspector
from scif.simcard import SimCard

PROJECT_ROOT = Path(__file__).parent

input_image = PROJECT_ROOT / "images" / "input" / "test.png"
output_image = PROJECT_ROOT / "images" / "output" / "decoded.png"

# Load image
width, height, original_pixels = ImageUtils.load_scif_pixels(input_image)

# Create virtual SIM
sim = SimCard()

# Encode image into SIM contacts
encoder = ScifEncoder(sim)
encoder.encode(width, height, original_pixels)

# Decode image back
decoder = ScifDecoder(sim)
decoder.decode(output_image)

# Verify pixel data
decoded_pixels = decoder.decode_pixels()

print()

if original_pixels == decoded_pixels:
    print("✓ Verification Passed")
else:
    print("✗ Verification Failed")

# This will stop the program if verification fails
assert original_pixels == decoded_pixels

print("\nDecoded image saved to:")
print(output_image)

print()

# Display SCIF information
ScifInspector.inspect(sim)