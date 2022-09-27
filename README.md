# Cookbook: Python acceleration and multithreading
Examples on how to accelerate Python via vectorization, multithreading, cross-compilation or FFI.
Demonstration of having an expensive calculation for a few objects.

```bash
# Building the Rust dependency
maturin develop --release
```

# Benchmark results
> Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz with 16 GB RAM

```
Timing the numba one-time compilation cost
	[WARMUP: Numba single-processing] finished in 337 ms
	[WARMUP: Numba multi-processing] finished in 13 ms
	[WARMUP: Numba&Numpy single-processing] finished in 9 ms
	[WARMUP: Numba&Numpy multi-processing] finished in 16 ms
Timing for size=10
	[Pure Python single-processing] finished in 5 ms
	[Pure Python multi-processing with workers] finished in 26 ms
	[Numpy single-processing] finished in 1 ms
	[Numpy multi-processing] finished in 1 ms
	[Numba single-processing] finished in 0 ms
	[Numba multi-processing] finished in 5 ms
	[Numba&Numpy single-processing] finished in 0 ms
	[Numba&Numpy multi-processing] finished in 4 ms
	[Rust multi-processing] finished in 0 ms
Timing for size=100
	[Pure Python single-processing] finished in 47 ms
	[Pure Python multi-processing with workers] finished in 40 ms
	[Numpy single-processing] finished in 13 ms
	[Numpy multi-processing] finished in 13 ms
	[Numba single-processing] finished in 1 ms
	[Numba multi-processing] finished in 6 ms
	[Numba&Numpy single-processing] finished in 0 ms
	[Numba&Numpy multi-processing] finished in 6 ms
	[Rust multi-processing] finished in 0 ms
Timing for size=1000
	[Pure Python single-processing] finished in 473 ms
	[Pure Python multi-processing with workers] finished in 198 ms
	[Numpy single-processing] finished in 129 ms
	[Numpy multi-processing] finished in 133 ms
	[Numba single-processing] finished in 7 ms
	[Numba multi-processing] finished in 11 ms
	[Numba&Numpy single-processing] finished in 7 ms
	[Numba&Numpy multi-processing] finished in 9 ms
	[Rust multi-processing] finished in 1 ms
Timing for size=10000
	[Pure Python multi-processing with workers] finished in 1739 ms
	[Numpy single-processing] finished in 1434 ms
	[Numpy multi-processing] finished in 1399 ms
	[Numba single-processing] finished in 72 ms
	[Numba multi-processing] finished in 63 ms
	[Numba&Numpy single-processing] finished in 71 ms
	[Numba&Numpy multi-processing] finished in 48 ms
	[Rust multi-processing] finished in 16 ms
Timing for size=100000
	[Numba single-processing] finished in 732 ms
	[Numba multi-processing] finished in 417 ms
	[Numba&Numpy single-processing] finished in 711 ms
	[Numba&Numpy multi-processing] finished in 403 ms
	[Rust multi-processing] finished in 158 ms
```