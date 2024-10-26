# Arvosanalaskuri

## Description

Arvosanalaskuri is a Python project for calculating grades for finnish university courses that use linear model for grades.

Grade is calulcated based on:

-   Points to get grade 1
-   Points to get grade 5
-   Your points

Linear calculus:  
$\text{grade} = 1 + (5 - 1) \times \frac{(\text{Your points} - \text{Points to get 1})}{(\text{Points to get 5} - \text{Points to get 1})}$

## Usage on the web

https://einesruoka.pyscriptapps.com/arvosanalaskuri

## Installation

To install the dependencies, use [Poetry](https://python-poetry.org/):

```sh
poetry install
```

## Usage

To run the project, execute the following
command

```sh
poetry run python3 main.py
```
