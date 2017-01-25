import json
import datetime
import numpy as np
from scipy import interpolate


class yieldCurve:
    # A class with points on the yield curve and the interpolation type
    def __init__(self, name, start, interpolation, points, dcf):
        self.interpolation = interpolation
        self.points = points
        self.start = start
        self.name = name
        self.dcf = dcf
        self.s = interpolate.interp1d(self.points[:0],
                                      self.points[:1],
                                      self.interpolation)

    def getDiscount(self, day):
        return(np.exp(-self(day)*self.dcf(self.start, day)))

    def getFRA(self, start, end):
        return(0)

    def __call__(self, day):
        return(self.s(day))


class DayCountFraction:
    # Types of day count fraction
    def __init__(self, type):
        self.type = type

    def __call__(self, a, b):
        if(self.type == "30/360"):
            return(b-a)
        else:
            return("m")


ab = DayCountFraction("30/360")
cd = DayCountFraction("")
a = (ab, cd)
print(a[0](2, 1))
temp = json.loads('{"Tp":["Dp","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw","Sw"],"Start date":["1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017","1/10/2017"], "Maturity2":["1/11/2017","2/13/2017","4/12/2017","7/12/2017","10/12/2017","1/12/2018","4/12/2018","7/12/2018","10/12/2018","1/14/2019","1/13/2020","1/12/2021","1/12/2022","1/12/2023","1/12/2024","1/13/2025","1/12/2026","1/12/2027","1/12/2029","1/12/2032","1/12/2037","1/13/2042","1/14/2047","1/12/2057","1/12/2067"], "Maturity":["O/N","1M","3M","6M","9M","12M","15M","18M","21M","24M","3Y","4Y","5Y","6Y","7Y","8Y","9Y","10Y","12Y","15Y","20Y","25Y","30Y","40Y","50Y"],"ds.factor":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],"Market quote":[0.66,0.654,0.673,0.729,0.797,0.867,0.935,0.999,1.062,1.123,1.317,1.456,1.562,1.649,1.721,1.779,1.828,1.872,1.942,2.006,2.058,2.071,2.071,2.058,2.058]}')
print([datetime.datetime.strptime(date,'%m/%d/%Y').date() for date in temp['Maturity2']])
OIS = yieldCurve("OIS",datetime.date(2017,10,1),)
