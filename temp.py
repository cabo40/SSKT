import numpy as np
from scipy import interpolate


class yieldCurve:
    # A class with points on the yield curve and the interpolation type
    def __init__(self, interpolation, points):
        self.interpolation = interpolation
        self.points = points

# def getDiscount(day):


x = yieldCurve("linear", np.zeros((6,2)))
s = interpolate.InterpolatedUnivariateSpline([1,2,3,4],[1,4,5,2])
print(s.get_knots()[0])
