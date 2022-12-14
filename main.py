from src.timing import timeit_context
from src.python import pure_sp, pure_mp, numpy_sp, numba_sp, numba_mp, numba_numpy_sp, numba_numpy_mp
from src import rust_mp
from src.lib import Point, assert_eq

if __name__ == "__main__":
    sizes = [10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]
    for ind, size in enumerate(sizes):
        results = None  # Initial default value if there is nothing to compare to
        points: list[Point] = Point.build_points(size)  # List with `size` points

        # Warmup timing for compiling the numba functions with LLVM
        if ind == 0:
            print("Timing the numba one-time compilation cost")
            with timeit_context("WARMUP: Numba single-processing"):
                _ = numba_sp.process_points(points)

            with timeit_context("WARMUP: Numba multi-processing"):
                _ = numba_mp.process_points(points)

            with timeit_context("WARMUP: Numba&Numpy single-processing"):
                _ = numba_numpy_sp.process_points(points)

            with timeit_context("WARMUP: Numba&Numpy multi-processing"):
                _ = numba_numpy_mp.process_points(points)

        # Timing the processing duration
        print(f"Timing for size={size}")
        if size <= 10 ** 3:  # To slow for bigger numbers
            # Pure Python: single-threading
            with timeit_context("Pure Python single-processing"):
                _results = pure_sp.process_points(points)
            results = assert_eq(results, _results)

        if size <= 10 ** 4:  # To slow for bigger numbers
            # Pure Python: multi-threading
            with timeit_context("Pure Python multi-processing with workers"):
                _results = pure_mp.process_points(points)
            results = assert_eq(results, _results)

            # Numpy: vectorized
            with timeit_context("Numpy single-processing"):
                _results = numpy_sp.process_points(points)
            results = assert_eq(results, _results)

            # Numpy: vectorized and multi-threading
            with timeit_context("Numpy multi-processing"):
                _results = numpy_sp.process_points(points)
            results = assert_eq(results, _results)

        # Numba: compiled and single-threading
        with timeit_context("Numba single-processing"):
            _results = numba_sp.process_points(points)
        results = assert_eq(results, _results)

        # Numba: compiled and multi-threading
        with timeit_context("Numba multi-processing"):
            _results = numba_mp.process_points(points)
        results = assert_eq(results, _results)

        # Numba and Numpy: vectorized, compiled and single-threading
        with timeit_context("Numba&Numpy single-processing"):
            _results = numba_numpy_sp.process_points(points)
        results = assert_eq(results, _results)

        # Numba and Numpy: vectorized, compiled and multi-threading
        with timeit_context("Numba&Numpy multi-processing"):
            _results = numba_numpy_mp.process_points(points)
        results = assert_eq(results, _results)

        # Rust: compiled and FFI
        with timeit_context("Rust multi-processing"):
            _results = rust_mp.process_points(points)
        results = assert_eq(results, _results)
