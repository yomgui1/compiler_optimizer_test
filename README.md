# Automatic tool to benchmark compilers on whole program optimization

I've tried to make a python tool to automaticaly build and test the .text section size
of a simple code where a vector emplace is called a fixed amount of time.
The test tries to benchmark this size over GCC and CLANG compiler to see if there are
differencies depending on the number of call iterations.

I've made this test after viewing this video of Jason Turner ("c++ weekly" web serie):
https://www.youtube.com/watch?v=D8eCPl2zit4

I've found that GCC 7 and GCC 8 doesn't have the same default behavior,
but CLANG mades an unusual choice after few call count, very different of GCC.

## Run the test

To run the test, display textual results and plot a graph of them, just type:

```python3 simple_vec_bench.py```

The test does 30 call iteration for each compiler configurations.

## Dependencies:

- Python3.6 or better
- g++ and clang++ (for the test itself)
- matplotlib (for the graphic plot at end of the test)