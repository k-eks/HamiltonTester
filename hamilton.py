from scipy.stats import distributions
import math


def R_test(alpha, reflections, wR_A, parameters_A, wR_B, parameters_B):
    """After Hamilton 1965, used eq 24 to get R values from F values."""
    """reflections ... n"""
    """dimension ... b or parameters_B - parameters_A"""
    """freedom ... b or N1"""
    dimension = parameters_B - parameters_A
    freedom = reflections - parameters_B
    F = distributions.f.ppf(1 - alpha, dimension, freedom)
    # 1 - alpha required because of pythons implemention of the F-distribution
    R = math.sqrt(dimension / freedom * F + 1)
    Rratio = wR_A / wR_B
    print("Reject if %f > %f at a probablility level of %f: %s" % (Rratio, R, alpha, (Rratio > R)))