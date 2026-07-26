from pathlib import Path

from scif.decoder import ScifDecoder
from scif.encoder import ScifEncoder
from scif.fileio import ScifFile
from scif.imageutils import ImageUtils
from scif.inspector import ScifInspector
from scif.simcard import SimCard

PROJECT_ROOT = Path(__file__).parent

input_image = PROJECT_ROOT / "images" / "input" / "test.png"
output_image = PROJECT_ROOT / "images" / "output" / "decoded.png"

scif_file = PROJECT_ROOT / "images" / "scif" / "test.scif"

# -----------------------
# Load original image
# -----------------------

width, height, original_pixels = ImageUtils.load_scif_pixels(input_image)

# -----------------------
# Encode into SIM
# -----------------------

sim = SimCard()

encoder = ScifEncoder(sim)

encoder.encode(width, height, original_pixels)

# -----------------------
# Save as .scif
# -----------------------

ScifFile.save(sim, scif_file)

print(f"SCIF file saved to:\n{scif_file}\n")

# -----------------------
# Load .scif
# -----------------------

loaded_sim = ScifFile.load(scif_file)

# -----------------------
# Decode from .scif
# -----------------------

decoder = ScifDecoder(loaded_sim)

decoder.decode(output_image)

decoded_pixels = decoder.decode_pixels()

# -----------------------
# Verification
# -----------------------

print()

if original_pixels == decoded_pixels:
    print("✓ Verification Passed")
else:
    print("✗ Verification Failed")

assert original_pixels == decoded_pixels

print("\nDecoded image saved to:")
print(output_image)

print()

ScifInspector.inspect(loaded_sim)