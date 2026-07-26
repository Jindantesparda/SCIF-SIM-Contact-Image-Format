from scif.imageutils import ImageUtils

width, height, pixels = ImageUtils.load_scif_pixels(
    "images/input/test.png"
)

print(f"Width  : {width}")
print(f"Height : {height}")

print()
print("First 100 pixels")
print(pixels[:100])