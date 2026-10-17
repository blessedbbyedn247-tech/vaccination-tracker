"""
Vaccination Tracker - PROG211 Object-Oriented Programming 1
Real-world problem: health clinics need a simple way to record which
vaccines a recipient has received, and to see who is due for a dose.

Digital Public Goods (DPG) alignment:
- Open-source: shared on GitHub under an open licence.
- Inclusive and accessible: plain text menu, simple language, no special hardware.
- Privacy-respecting: stores ONLY an anonymous ID and age group (no names,
  phone numbers, addresses or national ID numbers).
- Modular and reusable: each class has one job and can be reused in other projects.
"""

from datetime import date

# Tuple (optional bonus): fixed schedule of (vaccine name, total doses required).
VACCINE_SCHEDULE = (
    ("BCG", 1),
    ("Polio", 4),
    ("Measles", 2),
    ("Yellow Fever", 1),
    ("COVID-19", 2),
)


class VaccinationRecord:
    """One vaccination event (a single dose given on a date)."""

    def __init__(self, vaccine, dose_number, date_given=None):
        self.vaccine = vaccine
        self.dose_number = dose_number
        self.date_given = date_given or date.today().isoformat()

    def display_info(self):
        print(f"   - {self.vaccine} | Dose {self.dose_number} | {self.date_given}")


class Recipient:
    """A vaccine recipient identified ONLY by an anonymous ID (privacy-respecting)."""

    total_recipients = 0  # class attribute shared by all objects

    def __init__(self, recipient_id, age_group):
        self.recipient_id = recipient_id
        self.age_group = age_group
        self.records = []  # holds VaccinationRecord objects
        Recipient.total_recipients += 1

    # ---------- Instance methods ----------
    def add_vaccination(self, vaccine, date_given=None):
        """Create a VaccinationRecord object and link it to this recipient."""
        vaccine = Recipient.normalise_vaccine(vaccine)
        doses_so_far = self.count_doses(vaccine)
        required = self.required_doses(vaccine)
        if required is None:
            print(f"  '{vaccine}' is not in the vaccine schedule.")
            return False
        if doses_so_far >= required:
            print(f"  {vaccine} is already complete ({required}/{required} doses).")
            return False
        record = VaccinationRecord(vaccine, doses_so_far + 1, date_given)
        self.records.append(record)
        print(f"  Recorded {vaccine} dose {record.dose_number}/{required}.")
        return True

    def count_doses(self, vaccine):
        return sum(1 for r in self.records if r.vaccine == vaccine)

    def pending_vaccines(self):
        """Return a list of (vaccine, doses_remaining) still needed."""
        pending = []
        for name, required in VACCINE_SCHEDULE:
            remaining = required - self.count_doses(name)
            if remaining > 0:
                pending.append((name, remaining))
        return pending

    def display_info(self):
        print(f"\nRecipient ID: {self.recipient_id} | Age group: {self.age_group}")
        if not self.records:
            print("   No vaccinations recorded yet.")
        for record in self.records:
            record.display_info()
        pending = self.pending_vaccines()
        if pending:
            text = ", ".join(f"{n} ({d} left)" for n, d in pending)
            print(f"   Still due: {text}")
        else:
            print("   Fully vaccinated according to the schedule.")

    # ---------- Class method ----------
    @classmethod
    def get_total_recipients(cls):
        return cls.total_recipients

    # ---------- Static method ----------
    @staticmethod
    def normalise_vaccine(vaccine):
        """Match user input (any capitalisation) to the official vaccine name."""
        for name, _ in VACCINE_SCHEDULE:
            if name.lower() == vaccine.strip().lower():
                return name
        return vaccine

    @staticmethod
    def required_doses(vaccine):
        for name, doses in VACCINE_SCHEDULE:
            if name.lower() == vaccine.lower():
                return doses
        return None


# ---------- Data structure: dictionary (ID -> Recipient object) ----------
registry = {}


def add_recipient(recipient_id, age_group):
    """Add a new Recipient to the dictionary."""
    if recipient_id in registry:
        print(f"  ID {recipient_id} already exists.")
        return None
    registry[recipient_id] = Recipient(recipient_id, age_group)
    print(f"  Recipient {recipient_id} added.")
    return registry[recipient_id]


def display_all():
    """Loop through the dictionary and display every recipient."""
    if not registry:
        print("\nNo recipients registered yet.")
        return
    for recipient in registry.values():
        recipient.display_info()
    print(f"\nTotal recipients: {Recipient.get_total_recipients()}")


# ---------- Menu ----------
def show_menu():
    print("\n===== VACCINATION TRACKER =====")
    print("1. Add recipient")
    print("2. Record a vaccination")
    print("3. View one recipient")
    print("4. View all recipients")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            rid = input("Enter anonymous ID (e.g. R001): ").strip().upper()
            age = input("Enter age group (Infant / Child / Adult): ").strip().title()
            add_recipient(rid, age)

        elif choice == "2":
            rid = input("Enter recipient ID: ").strip().upper()
            if rid in registry:
                print("Available vaccines:", ", ".join(n for n, _ in VACCINE_SCHEDULE))
                vaccine = input("Vaccine given: ").strip()
                registry[rid].add_vaccination(vaccine)
            else:
                print("  Recipient not found.")

        elif choice == "3":
            rid = input("Enter recipient ID: ").strip().upper()
            if rid in registry:
                registry[rid].display_info()
            else:
                print("  Recipient not found.")

        elif choice == "4":
            display_all()

        elif choice == "5":
            print("Goodbye. Stay healthy!")
            break

        else:
            print("  Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
