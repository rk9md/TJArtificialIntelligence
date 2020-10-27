import math
blackToSun = 1000
radSun = 700000000
volSun = 4/3 * math.pi *radSun*radSun*radSun
denSun = 1400000
massBlack = volSun*denSun*blackToSun

blackRad = 2160/4 *1.609*100000
volBlack = 4/3 * math.pi * pow(blackRad,3)

den = massBlack/blackRad
print(den)