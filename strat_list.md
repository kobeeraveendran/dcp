# List of strategies for frequently occurring tasks

- using dicts/hashtable for "seen" values (helps with doing things in less passes)
    - as seen in problem 1
- to satisfy memory constraints, and if dealing with arrays of integers, consider using the array indices as dictionary 'keys'
    - as seen in problem 4
- instead of going through an entire list skipping a variable # of indices n, consider using recursion (similar to below strat), like so:
    - curr + find_sum(list[1:]) or curr + find_sum(list[2:]), or both
- for "number of ways to do x" problems, recursion is usually a good approach
    - breaking down problem into subunits at a time