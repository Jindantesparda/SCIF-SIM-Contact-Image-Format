from pathlib import Path

from .contact import SimContact
from .simcard import SimCard


class ScifFile:
    """
    Handles saving and loading SCIF files.
    """

    @staticmethod
    def save(sim: SimCard, output_path: Path) -> None:
        """
        Saves a virtual SIM card to a .scif file.
        """

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as file:

            for contact in sim.contacts:
                file.write(f"{contact.name},{contact.number}\n")

    @staticmethod
    def load(input_path: Path) -> SimCard:
        """
        Loads a .scif file into a virtual SIM card.
        """

        sim = SimCard()

        with input_path.open("r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                name, number = line.split(",", 1)

                sim.add_contact(
                    SimContact(
                        name=name,
                        number=number
                    )
                )

        return sim