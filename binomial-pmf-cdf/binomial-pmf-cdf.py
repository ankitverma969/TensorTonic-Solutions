import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    
    # Edge cases
    if p == 0:
        pmf = 1.0 if k == 0 else 0.0
        cdf = 1.0  # since X always 0
        return pmf, cdf
    
    if p == 1:
        pmf = 1.0 if k == n else 0.0
        cdf = 1.0 if k >= n else 0.0
        return pmf, cdf

    # PMF
    pmf = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    # CDF
    i = np.arange(0, k + 1)
    cdf = np.sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)))

    return float(pmf), float(cdf)