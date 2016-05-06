from scipy.stats import distributions
import math


def R_test(alpha, reflections, wR_A, parameters_A, wR_B, parameters_B):
    """Performs a Hamilton-R Test for a structure, method described below.
    !!!Model A MUST be the model with fewer parameters!!!
    alpha ... float percentage value (i.e. 0.05 for 5 %) for the probablility of error
    reflections ... number of unique reflections (data in shelx) of the measurement
    wR_A ... float value or percent of R1 value from Model A
    parameters_A ... int number of parameters used in Model A
    wR_B ... float value or percent of R1 value from Model B
    parameters_B ... int number of parameters used in Model B
    After Hamilton 1965, used eq 24 to get R values from F values. Input for equation:
    reflections ... n
    dimension ... b or parameters_B - parameters_A
    freedom ... b or N1"""
    dimension = parameters_B - parameters_A
    freedom = reflections - parameters_B
    F = distributions.f.ppf(1 - alpha, dimension, freedom)
    # 1 - alpha required because of pythons implemention of the F-distribution
    R = math.sqrt(dimension / freedom * F + 1)
    Rratio = wR_A / wR_B
    print("Rratio = %f\nR = %f" %(Rratio, R))
    print("Hypothesis: Model A is better than Model B")
    print("Reject if %f > %f at a probablility level of %f" % (Rratio, R, alpha))
    print("Result: Hypothesis is %s" % (Rratio < R))
    # the use of larger than and smaller than signs is correct! It's not a typo, just programing logic