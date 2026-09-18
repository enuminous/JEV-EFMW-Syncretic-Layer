import numpy as np
from src.detectors import ewma,efmw_residual
def test_zero(): assert np.allclose(efmw_residual(np.zeros(20)),0)
def test_length(): assert len(ewma(np.arange(20.)))==20
