# Water Bill Calculator

A simple **Python** program that takes a consumer's name and water usage, calculates the bill using a slab tariff, and shows the usage category with a water conservation tip.

> **Course:** Python Programming (25BCA3C03) | **Activity 2:** Python Package Development
> **Department:** CS and IT, JAIN (Deemed-to-be University) | **Semester:** 3rd
> **Submitted to:** Dr. Ramkumar Krishnamoorthy

---

Student Details

| S. No. | USN | Name |
|:------:|-----|------|
| 1 | 25BCAR0218 | Suman Srivatsa |

---

## Problem Statement

Calculate the water bill from the units consumed, classify the usage, and give a conservation tip.

## Features

- Takes the **consumer name** and **water usage (in units)**
- **Slab-wise billing:** higher usage is charged at a higher rate
- Classifies usage as **Low, Moderate or High Consumption**
- Shows a **conservation tip** based on the usage category
- Prints a neat bill with name, usage, total amount, category and tip
- **Input validation:** letters instead of numbers and negative usage are handled

### Tariff

| Units consumed | Rate per unit |
|----------------|--------------:|
| First 10 units (1 - 10) | Rs. 5 |
| Next 10 units (11 - 20) | Rs. 8 |
| Next 10 units (21 - 30) | Rs. 10 |
| Above 30 units | Rs. 15 |

### Usage Category and Tip

| Units consumed | Category | Tip |
|----------------|----------|-----|
| 10 or less | Low Consumption | Good! Continue saving water. |
| 11 - 20 | Moderate Consumption | Avoid unnecessary water usage. |
| Above 20 | High Consumption | High usage! Fix leaking taps and reduce water wastage. |

**Example:** 25 units -> 10 x 5 + 10 x 8 + 5 x 10 = 50 + 80 + 50 = **Rs. 180**

---

## Project Structure

```
WaterBilling/
├── water_pkg/              # user-defined Python package
│   ├── __init__.py         # makes the folder a package, exposes the functions
│   └── ActualTask.py       # function definitions
├── main.py                 # executable program (run this file)
├── sample_output.txt       # sample runs of the program
└── README.md
```

### Functions in `water_pkg/ActualTask.py`

| Function | Purpose |
|----------|---------|
| `calculate_charge(units)` | Returns the bill amount using the slab tariff |
| `usage_category(units)` | Returns Low, Moderate or High Consumption |
| `conservation_tip(category)` | Returns a tip for the given category |

---

## How to Run

**Requirements:** Python 3 installed. No extra libraries are needed.

```bash
# 1. Clone the repository
git clone <YOUR-GITHUB-REPO-URL>

# 2. Go into the project folder
cd WaterBilling

# 3. Run the program
python main.py


(On some systems use `python3 main.py` instead.)

How to use the program

1. Type the **consumer name** and press Enter.
2. Type the **water usage in units** and press Enter.
3. The bill, usage category and conservation tip are printed.



Sample Output

     WATER BILL CALCULATOR
Enter Consumer Name: Ravi
Enter Water Usage (in units): 25

 WATER BILL 
Consumer Name: Ravi
Water Usage: 25.0 units
Total Water Bill: Rs. 180.0
Usage Category: High Consumption
Conservation Tip: High usage! Fix leaking taps and reduce water wastage.
```

More runs (including invalid inputs) are saved in [`sample_output.txt`](sample_output.txt).

---

## Test Cases

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Low usage | 8 units | Rs. 40.0, Low Consumption |
| 2 | Exactly 10 units | 10 units | Rs. 50.0, Low Consumption |
| 3 | Moderate usage | 15 units | Rs. 90.0, Moderate Consumption |
| 4 | High usage | 25 units | Rs. 180.0, High Consumption |
| 5 | Above 30 units | 35 units | Rs. 305.0, High Consumption |
| 6 | Letters instead of numbers | `abc` | "Please enter numbers only!" |
| 7 | Negative usage | `-4` | "Invalid water usage!" |

All the above test cases passed.

---

## Python Concepts Used

- **Unit 1:** `print`, `input`, `if/elif/else`, strings, functions, return values
- **Unit 3:** exception handling (`try/except ValueError`)
- **Package development:** a user-defined package (`water_pkg`) with `__init__.py` and a module, imported in `main.py`


## Learning Outcomes

This project helped me understand how to create a user-defined Python package, organize code into modules, develop reusable functions, handle user input, and perform project testing.

---

Developed as part of Activity 2 - Python Package Development, JAIN (Deemed-to-be University)
