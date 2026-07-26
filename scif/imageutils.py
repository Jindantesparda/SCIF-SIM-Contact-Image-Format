from pathlib import Path

from PIL import Image


class ImageUtils:
    """
    Utility functions for loading and preparing images for SCIF.
    """

    @staticmethod
    def load_image(path: str | Path) -> Image.Image:
        return Image.open(path)

    @staticmethod
    def to_grayscale(image: Image.Image) -> Image.Image:
        return image.convert("L")

    @staticmethod
    def quantize_16_levels(image: Image.Image) -> list[int]:
        """
        Convert 0-255 grayscale values into 0-15.
        """

        pixels = list(image.getdata())

        return [pixel // 16 for pixel in pixels]

    @staticmethod
    def load_scif_pixels(path: str | Path) -> tuple[int, int, list[int]]:

        image = ImageUtils.load_image(path)

        grayscale = ImageUtils.to_grayscale(image)

        pixels = ImageUtils.quantize_16_levels(grayscale)

        return grayscale.width, grayscale.height, pixels