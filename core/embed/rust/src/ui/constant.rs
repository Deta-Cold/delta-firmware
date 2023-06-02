//! Reexporting the `constant` module according to the
//! current feature (detahard model)

#[cfg(all(feature = "model_tr", not(feature = "model_tt")))]
pub use super::model_tr::constant::*;
#[cfg(feature = "model_tt")]
pub use super::model_tt::constant::*;
