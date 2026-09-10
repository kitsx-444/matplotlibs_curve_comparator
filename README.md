# Multi-Pair Equity Curve Comparator

## What it does:
This program uses trade results and dates to create a visual equity comparator using `matplotlib`.

## Its purpose:
This helps traders visualize their accounts equity curve so they can make informed decisions on what drives their growth and what doesn't.

## Output
<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/a5702bd9-ba8c-46da-96f1-10b52dd7c742" />

## Concepts demonstrated:
1. Sorting a list of tuples using `key=lambda`
2. Using the `datetime` module to turn a string into usable code.
3. `matplotlib` and its plotting syntax to create the equity curve.
4. Using for loops to track and append a running total.
5. Date appending and running total appending to be jotted as x and y values.
6. Using and plotting multiple assets to have a multi-key asset equity curve graph.
7. Dictionaries

## The bug:
Before all the assets shared one starting number, when it was plotted the graph was a visual mess. 

## The fix:
To fix that bug there are multiple starting balances for each asset. because without those variables the starting balances of each asset would be at the last balance iteration of the running total from the assets loop before it. 

## How to run:
1. Install matplotlibs. `pip install matplotlib`
2. This program uses hardcoded data. It is really straightforward from here. Click run on your preferred IDE.
