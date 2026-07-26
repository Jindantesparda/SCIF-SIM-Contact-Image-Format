class ScifVerifier:

    @staticmethod
    def verify(
        original_pixels: list[int],
        decoded_pixels: list[int],
    ) -> bool:

        return original_pixels == decoded_pixels