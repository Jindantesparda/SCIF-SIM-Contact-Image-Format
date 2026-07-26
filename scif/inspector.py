from .constants import MAX_CONTACTS
from .simcard import SimCard


class ScifInspector:

    @staticmethod
    def inspect(sim: SimCard) -> None:

        header = sim.get_contact(0)

        width = int(header.number[:4])
        height = int(header.number[4:8])

        contacts_used = sim.total_contacts()

        pixels = width * height

        pixels_per_contact = 20

        storage_used = contacts_used / MAX_CONTACTS * 100

        print("=" * 40)
        print("SCIF IMAGE INFORMATION")
        print("=" * 40)
        print(f"Version            : {header.name}")
        print(f"Width              : {width}")
        print(f"Height             : {height}")
        print(f"Pixels             : {pixels}")
        print(f"Contacts Used      : {contacts_used}/{MAX_CONTACTS}")
        print(f"Pixels per Contact : {pixels_per_contact}")
        print(f"SIM Usage          : {storage_used:.2f}%")
        print("=" * 40)