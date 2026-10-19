"""helper_functions.py

Utility and mathematical functions for the Bass Diffusion Model.
"""

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def bass_cumulative(t, p, q, M):
  """Calculates cumulative adopters N(t) at time t.

  F(t) = [1 - exp(-(p+q)t)] / [1 + (q/p)*exp(-(p+q)t)]
  N(t) = M * F(t)
  """
  numerator = 1.0 - np.exp(-(p + q) * t)
  denominator = 1.0 + (q / p) * np.exp(-(p + q) * t)
  return M * (numerator / denominator)


def bass_annual_sales(t, p, q, M):
  """Calculates discrete annual adopters S(t) = N(t) - N(t-1)."""
  cum = bass_cumulative(t, p, q, M)
  sales = np.zeros_like(cum)
  sales[0] = cum[0]
  for i in range(1, len(cum)):
    sales[i] = cum[i] - cum[i - 1]
  return sales


def fit_bass_model(
    periods, cum_sales, p0=[0.01, 0.4, 400], bounds=([1e-4, 0.01, 200], [0.1, 1.0, 600])
):
  """Fits the Bass model parameters (p, q, M) to historical cumulative data using

  non-linear least squares.
  """
  popt, _ = curve_fit(bass_cumulative, periods, cum_sales, p0=p0, bounds=bounds)
  return popt[0], popt[1], popt[2]


def forecast_diffusion(p, q, M_target, periods=10):
  """Generates a DataFrame forecasting annual and cumulative adopters for a new

  product.
  """
  t = np.arange(1, periods + 1)
  cum_adopters = bass_cumulative(t, p, q, M_target)

  annual_adopters = np.zeros(len(t))
  annual_adopters[0] = cum_adopters[0]
  for i in range(1, len(t)):
    annual_adopters[i] = cum_adopters[i] - cum_adopters[i - 1]

  return pd.DataFrame({
      "Year (t)": t,
      "Annual Adopters (M)": np.round(annual_adopters, 2),
      "Cumulative Adopters (M)": np.round(cum_adopters, 2),
  })


def fermi_market_potential(installed_base_m, earbud_pct, pro_tier_pct):
  """Estimates total market potential M using Fermi decomposition."""
  return installed_base_m * earbud_pct * pro_tier_pct