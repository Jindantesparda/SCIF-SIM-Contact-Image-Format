from .contact import SimContact
from .constants import MAX_CONTACTS


class SimCard:
    def __init__(self):
        self._contacts: list[SimContact] = []

    def remove_contact(self, index: int) -> None:
        del self._contacts[index]


    @property
    def contacts(self) -> list[SimContact]:
        return self._contacts

    def add_contact(self, contact: SimContact) -> None:
        if len(self._contacts) >= MAX_CONTACTS:
            raise ValueError("SIM card is full.")

        self._contacts.append(contact)

    def get_contact(self, index: int) -> SimContact:
        return self._contacts[index]

    def total_contacts(self) -> int:
        return len(self._contacts)

    def clear(self) -> None:
        self._contacts.clear()

    def print_contacts(self) -> None:
        print("=" * 60)

        for i, contact in enumerate(self._contacts):
            print(f"[{i:03}]")
            print(f"Name   : {contact.name}")
            print(f"Number : {contact.number}")
            print()