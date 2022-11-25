
# Backtracking (NP-complete problems)

- eligibility:

Examples of CSP solved by Backtracking
- Permutations, Combinations, Subsets

- Boolean satisfiability problem (SAT)
- Hamiltonian path problem
- Travelling salesman problem
- Graph coloring

```
function backTrackAlgorithm(parameters) {
  function backtrack(startingState) {
    if (final condition is met) {
      add result;
    } else {
      loop from the starting state
        try a candidate;
        backtrack(adjustedStartingState);
        remove the candidate;
    }
  }
  
  handle edge cases
  initialize the result structure;
  backtrack(startingState);
  return result;
}

```

