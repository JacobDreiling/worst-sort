# worst-sort
Python implementation of Miguel Lerma's infamous "worstsort" algorithm

A helper function, badsort, is defined as followed:
- If the recursion depth, k, equals zero, return bubblesort of the list L.
- Otherwise, let P be the list of all permutations of L. Return the first item of badsort(P, k-1), i.e. the sorted list L.

Worstsort takes a list L and an increasing computable function f and returns badsort(L, f(length(L))). The resulting complexity is slightly worse than O(f(n)).

https://arxiv.org/abs/1406.1077
