DAA PYTHON PROGRAMS
===================

This folder contains separate Python implementations for the algorithms in the supplied list.
Each program is saved as its own .py file and can be run with Python 3:

    python filename.py

Most files contain a small example under `if __name__ == "__main__":`.
You can also import the function from a file and call it with your own input.

Abbreviation interpretations used:
- ALS = Activity Selection
- WB = Weighted Interval Scheduling
- TEXT = Text Pattern Matching (KMP)
- BINPA1K = Bin Packing (First-Fit Decreasing approximation)
- SET 1OVER = Greedy Set Cover approximation
- VERTEX 1OVER = Vertex Cover 2-approximation

Other notes:
- Binary search expects sorted input.
- Dijkstra requires non-negative edge weights.
- Bellman-Ford detects reachable negative-weight cycles.
- Floyd-Warshall uses infinity for missing edges.
- Strassen implementation accepts square matrices and pads to a power-of-two size.
- TSP uses Held-Karp dynamic programming and returns a minimum tour starting at vertex 0.
- 0/1 knapsack and fractional knapsack are separate implementations.
- The optimal BST implementation uses successful-search frequencies only.
- Container loading uses a lightest-first greedy strategy.
- Graph algorithms expect the input formats described in their docstrings.

These are educational reference implementations. Check your course's exact input/output format
and algorithm variant before submitting them for an assignment.
