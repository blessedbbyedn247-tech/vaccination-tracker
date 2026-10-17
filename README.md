# Vaccination Tracker

**Module:** PROG211 Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Institution:** Limkokwing University of Creative Technology, Sierra Leone
**Student:** Edwina Nicol | **Student ID:** 905005799
**Lecturer:** Mr. Alusine Lavalie

## Overview

Vaccination Tracker is a simple Python program that helps a health clinic record which vaccines a recipient has received and see which doses are still due. It is built with Object-Oriented Programming (OOP) and follows Digital Public Goods (DPG) principles.

## Real-World Problem

Clinics often track vaccinations on paper, which makes it hard to see who still needs a dose. This program gives a clear, simple record of each recipient’s vaccinations and what remains on the schedule.

## How the Program Meets the Assignment Tasks

|Task                                           |Where it is in the code                                                     |
|-----------------------------------------------|----------------------------------------------------------------------------|
|Two or more classes with attributes and methods|`Recipient` and `VaccinationRecord`                                         |
|Object creation and interaction                |A `Recipient` creates `VaccinationRecord` objects in `add_vaccination()`    |
|One data structure (dictionary)                |`registry` stores Recipient objects using the recipient ID as the key       |
|Function to add and display records            |`add_recipient()` and `display_all()`                                       |
|Instance methods                               |`add_vaccination()`, `count_doses()`, `pending_vaccines()`, `display_info()`|
|Class method (`@classmethod`)                  |`Recipient.get_total_recipients()`                                          |
|Static methods                                 |`required_doses()` and `normalise_vaccine()`                                |
|Tuple (optional bonus)                         |`VACCINE_SCHEDULE` is a tuple of (vaccine, doses required)                  |

## DPG Standards Alignment

1. **Open-source:** The full source code is published on GitHub under the MIT Licence, so anyone can use, study, and improve it.
1. **Inclusive and accessible design:** It uses a plain text menu with simple language. It needs no internet connection, special hardware, or paid software, only Python.
1. **Privacy-respecting:** No sensitive personal data is stored. Recipients are identified only by an anonymous ID (for example `R001`) and an age group. There are no names, phone numbers, addresses, or national ID numbers.
1. **Modular and reusable:** Each class has one job. `VaccinationRecord` stores a single dose, and `Recipient` manages one person’s records. The vaccine schedule is kept in one place, so other clinics can reuse the code and change the vaccines easily.

## Requirements

- Python 3.8 or newer (tested on Python 3.14)
- No extra libraries are needed

## How to Run

1. Download or clone this repository.
1. Open a terminal in the project folder.
1. Run:

```
python vaccination_tracker.py
```

## Example Usage (Sample Input and Output)

```
===== VACCINATION TRACKER =====
1. Add recipient
2. Record a vaccination
3. View one recipient
4. View all recipients
5. Exit
Choose an option (1-5): 1
Enter anonymous ID (e.g. R001): R001
Enter age group (Infant / Child / Adult): Child
  Recipient R001 added.

Choose an option (1-5): 2
Enter recipient ID: R001
Available vaccines: BCG, Polio, Measles, Yellow Fever, COVID-19
Vaccine given: Polio
  Recorded Polio dose 1/4.

Choose an option (1-5): 2
Enter recipient ID: R001
Vaccine given: BCG
  Recorded BCG dose 1/1.

Choose an option (1-5): 3
Enter recipient ID: R001

Recipient ID: R001 | Age group: Child
   - Polio | Dose 1 | 2026-10-17
   - BCG | Dose 1 | 2026-10-17
   Still due: Polio (3 left), Measles (2 left), Yellow Fever (1 left), COVID-19 (2 left)
```

The dates shown are the day each dose is recorded.

## Project Structure

```
vaccination-tracker/
├── vaccination_tracker.py   # Python source code
├── README.md                # Documentation (this file)
└── LICENSE                  # MIT Licence
```

## Licence

Released under the MIT Licence. See the `LICENSE` file.