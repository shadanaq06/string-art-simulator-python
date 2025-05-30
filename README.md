# Turtle Nail & String Art - using Python Turtle 🐢🎨

A Python project using Turtle graphics to simulate geometric string art and calculate material costs for nails, string, and the board. 

## 🧠 Project Summary

This program allows users to:
- Input custom coordinates for nails.
- Visually create string art using Turtle graphics.
- Automatically draw connecting strings between nails.
- Calculate the total material cost based on user input and pre-defined rates.

## 🛠️ Features

- Interactive input for nail placement (x, y coordinates)
- Visual stamping of nails and drawing of threads using `turtle`
- Real-time cost calculation including:
  - Nail cost
  - String length converted to cost
  - Fixed board cost
- Output of final cost displayed graphically

## 💸 Cost Assumptions

| Item         | Unit Cost    |
|--------------|--------------|
| Nail         | $0.12 each   |
| String       | $0.07/meter  |
| Board        | $5.00 flat   |
| 1 Meter ≈    | 32 pixels    |


## 🐍 Requirements

- Python 3.x
- `turtle` module (included with Python by default)

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/turtle-string-art-python.git
   cd turtle-string-art-python
