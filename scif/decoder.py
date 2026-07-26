from pathlib import Path

from PIL import Image

from .constants import MAGIC
from .simcard import SimCard


class ScifDecoder:
    """
    Decodes a SCIF image stored in a virtual SIM card.
    """

    def __init__(self, sim: SimCard):
        self.sim = sim

    def read_header(self) -> tuple[int, int]:
        """
        Reads and validates the SCIF header.

        Returns:
            (width, height)
        """

        header = self.sim.get_contact(0)

        if header.name != MAGIC:
            raise ValueError(
                f"Invalid SCIF file. Expected '{MAGIC}', got '{header.name}'."
            )

        width = int(header.number[:4])
        height = int(header.number[4:8])

        return width, height

    def read_hex_data(self) -> str:
        """
        Reads all hexadecimal image data stored in the SIM contacts.
        """

        return "".join(
            contact.name
            for contact in self.sim.contacts[1:]
        )

    @staticmethod
    def hex_to_pixels(hex_string: str) -> list[int]:
        """
        Converts hexadecimal characters back into
        4-bit pixel values (0-15).
        """

        return [
            int(character, 16)
            for character in hex_string
        ]

    @staticmethod
    def expand_pixels(pixels: list[int]) -> list[int]:
        """
        Converts 4-bit grayscale values (0-15)
        back into 8-bit grayscale (0-255).
        """

        return [
            pixel * 17
            for pixel in pixels
        ]

    @staticmethod
    def save_image(
        width: int,
        height: int,
        pixels: list[int],
        output_path: Path,
    ) -> None:
        """
        Saves the reconstructed image.
        """

        output_path.parent.mkdir(parents=True, exist_ok=True)

        image = Image.new("L", (width, height))
        image.putdata(pixels)
        image.save(output_path)

    def decode_pixels(self) -> list[int]:
        """
        Decodes the SCIF file into its original
        4-bit pixel values (0-15).

        Used for verification.
        """

        width, height = self.read_header()

        hex_string = self.read_hex_data()

        hex_string = hex_string[: width * height]

        return self.hex_to_pixels(hex_string)

    def decode(self, output_path: Path) -> None:
        """
        Fully decodes the SCIF image and saves it.
        """

        width, height = self.read_header()

        pixels = self.decode_pixels()

        expanded_pixels = self.expand_pixels(pixels)

        self.save_image(
            width,
            height,
            expanded_pixels,
            output_path,
        )