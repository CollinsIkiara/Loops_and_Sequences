# Python Fundamentals: Lists, Tuples, Loops & Functional Programming

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Learning%20Project-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Two Python projects demonstrating fundamental programming concepts including **lists, tuples, loops, and enumerate** through practical examples.

This repository includes two scripts:

- **Number Pattern Generator**
- **PIN Extractor from Poems**

These examples illustrate how core Python constructs can be used to build simple but meaningful programs.

---

# Table of Contents

- [Project Overview](#project-overview)
- [Concepts Covered](#concepts-covered)
- [Project Structure](#project-structure)
- [Script 1: Number Pattern Generator](#script-1-number-pattern-generator)
- [Script 2: PIN Extractor](#script-2-pin-extractor)
- [How to Run the Code](#how-to-run-the-code)
- [Example Output](#example-output)

---

# Project Overview

This repository demonstrates several **core Python programming concepts** through small standalone scripts.

The scripts showcase:

- Input validation
- Iteration
- List manipulation
- String processing
- Algorithmic thinking

The goal of the project is to reinforce Python fundamentals while implementing simple real-world logic.

---

# Concepts Covered

- Lists  
- Common List Methods  
- Tuples  
- Common Tuple Methods  
- Loops  
- Range in Loops  
- Enumerate Function    

---

# Project Structure

```
loops_and_sequences/
│
├── Number_Pattern_Generator.py
├── Pin_Extractor.py
└── README.md
```

---

# Script 1: Number Pattern Generator

## File
`Number_Pattern_Generator.py`

## Description

Generates a sequence of numbers from **1 to a specified integer** and returns them as a space-separated string.

The function also performs **input validation** to ensure the argument:

- is an integer
- is greater than zero

---

## Function

```python
def number_pattern(n):
```

---

## Example Usage

```python
print(number_pattern(4))
```

### Output

```
1 2 3 4
```

### Invalid Input Examples

```
Argument must be an integer value.
Argument must be an integer greater than 0.
```

---

# Script 2: PIN Extractor

## File
`Pin_Extractor.py`

## Description

Extracts **secret numeric PIN codes from poems** using a positional word-length pattern.

For each line in a poem:

1. The program selects a word based on the **line index**
2. The **length of the selected word** becomes a digit
3. All digits are combined to form a **secret PIN**

---

## Example Poem

```
Stars and the moon
shine in the sky
white and
until the end of the night
```

---

## How the Algorithm Works

```
Line 0 → take word 0 → count letters
Line 1 → take word 1 → count letters
Line 2 → take word 2 → count letters
Line 3 → take word 3 → count letters
```

If the word does **not exist**, the digit **0** is used.

---

## Function

```python
def pin_extractor(poems):
```

---

## Example Usage

```python
print(pin_extractor([poem, poem2, poem3]))
```

### Example Output

```
['5162', '4034', '11111']
```

Each poem generates a **unique numeric PIN**.

---

# How to Run the Code

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/python-fundamentals.git
```

### 2. Navigate into the directory

```bash
cd python-fundamentals
```

### 3. Run the scripts

```
python Number_Pattern_Generator.py
```

```
python Pin_Extractor.py
```

---

# Example Output

```
Argument must be an integer value.
Argument must be an integer greater than 0.
1 2 3 4

['5162', '4034', '11111']
```

---
