use pyo3::prelude::*;
use rayon::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn process_points(points: Vec<(f64, f64, f64, f64)>) -> PyResult<Vec<f64>> {
    let result = points.par_iter().map(
        |p| {
            (1..1_000).fold(0_f64, |acc, ind| {
                ((p.0.powi(2) + p.1.powi(2) + p.2.powi(2) + p.3.powi(2)).sqrt()
                    / ind as f64) + acc
            })
        }
    )
        .collect();
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_lib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(process_points, m)?)?;
    Ok(())
}