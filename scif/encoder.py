from .contact import SimContact
from .simcard import SimCard
from .constants import MAGIC


class ScifEncoder:

    def __init__(self, sim: SimCard):
        self.sim = sim


    @staticmethod
    def pixels_to_hex(pixels: list[int]) -> str:

        return "".join(format(pixel, "X") for pixel in pixels)

    @staticmethod
    def chunk_string(data: str, size: int = 20):

        return [
            data[i:i + size]
            for i in range(0, len(data), size)
        ]

    @staticmethod
    def create_header(width: int, height: int):

        return SimContact(
            name=MAGIC,
            number=f"{width:04}{height:04}"
        )

    def encode(
            self,
            width: int,
            height: int,
            pixels: list[int]
    ):

        self.sim.clear()

        self.sim.add_contact(
            self.create_header(width, height)
        )

        hex_data = self.pixels_to_hex(pixels)

        chunks = self.chunk_string(hex_data)

        for chunk in chunks:

            self.sim.add_contact(
                SimContact(
                    name=chunk.ljust(20, "0"),
                    number="0" * 20
                )
            )