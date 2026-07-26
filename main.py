from scif.contact import SimContact
from scif.simcard import SimCard

sim = SimCard()

sim.add_contact(
    SimContact(
        "SCIFV1",
        "00000000000000000000"
    )
)

sim.add_contact(
    SimContact(
        "0123456789ABCDEF0123",
        "12345678901234567890"
    )
)

sim.print_contacts()