from scipy.stats import distributions
import math


def R_test(alpha):
    F = distributions.f.ppf(1 - alpha, dimension_b, freedom_N1)

    wRa = 0.0942
    wRb = 0.0853
    Pa = 333
    Pb = 613
    reflections_n = 5177
    dimension_b = Pb - Pa # 320
    freedom_N1 = reflections_n - Pb
    F = distributions.f.ppf(1 - alpha, dimension_b, freedom_N1)
    R = math.sqrt(dimension_b / freedom_N1 * F + 1)

    rratio = wRa / wRb
    rcontrast = 1 + 120 / freedom_N1 * (Rb - 1)
    print(rratio, rcontrast)