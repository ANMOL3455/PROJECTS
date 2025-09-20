# ===============================================|
# Python Calculator Module beginner level--------|
# ===============================================|

# -------------------------
# Basic operations
# -------------------------
def add(number_1, number_2):
    return number_1 + number_2

def sub(number_1, number_2):
    return number_1 - number_2

def mul(number_1, number_2):
    return number_1 * number_2

def div(number_1, number_2):
    if number_2 != 0:
        return number_1 / number_2
    else:
        return print(">>>> ERROR: Division by zero >>>>")

# -------------------------
# Powers
# -------------------------
def sq(number):
    return number ** 2

def cb(number):
    return number ** 3

def exp(number, expo):
    return number ** expo

# -------------------------
# Area of shapes
# -------------------------
def ar_circle(radius):
    pi_val = 3.141592653589793
    return pi_val * radius ** 2

def ar_sq(length):
    return length ** 2

def ar_rect(length, bredth):
    return length * bredth

def ar_tri(side_1, side_2, side_3):
    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        return print("length cannot be zero or negative")
    s = (side_1 + side_2 + side_3) / 2
    return (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5

# -------------------------
# Perimeter of shapes
# -------------------------
def per_circle(radius):
    pi_val = 3.141592653589793
    return 2 * pi_val * radius

def per_sq(length):
    return 4 * length

def per_rect(length, bredth):
    return 2 * (length + bredth)

def per_tri(side_1, side_2, side_3):
    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        return print("length cannot be zero or negative")
    return side_1 + side_2 + side_3

# -------------------------
# Trigonometric functions (radians)
# -------------------------
def sin_ang(x):
    return x - (x ** 3) / 6 + (x ** 5) / 120 - (x ** 7) / 5040

def cos_ang(x):
    return 1 - (x ** 2) / 2 + (x ** 4) / 24 - (x ** 6) / 720

def tan_ang(x):
    return sin_ang(x) / cos_ang(x)

# -------------------------
# Degree to radians
# -------------------------
def sin_val(deg):
    return (deg * 3.141592653589793) / 180

def cos_val(deg):
    return (deg * 3.141592653589793) / 180

def tan_val(deg):
    return sin_val(deg) / cos_val(deg)

# -------------------------
# Tables
# -------------------------
def table(num):
    for i in range(1, 11):
        print(num * i)

# -------------------------
# Weight conversions
# -------------------------
def kg(gram):
    return gram / 1000

def gram(kg):
    return kg * 1000

def g_mgram(gram):
    return gram * 1000

def kg_mgram(kg):
    return kg * 1000000

def mgram_g(mgram):
    return mgram / 1000

def mgram_kg(mgram):
    return mgram / 1000000

# -------------------------
# Distance conversions
# -------------------------
def me(kilo):
    return kilo * 1000

def kme(me):
    return me / 1000

def kme_mm(kme):
    return kme * 1_000_000

def mm_kme(mm):
    return mm / 1_000_000

def m_cm(m):
    return m * 100

def cm_m(cm):
    return cm / 100

# -------------------------
# Time conversions
# -------------------------
def sec_hrs(sec):
    return sec / 3600

def hrs_sec(hrs):
    return hrs * 3600

def sec_min(sec):
    return sec / 60

def min_sec(min):
    return min * 60

def min_hrs(min):
    return min / 60

# -------------------------
# Fluid conversions
# -------------------------
def l_ml(l):
    return l * 1000

def ml_l(ml):
    return ml / 1000

# -------------------------
# Roots
# -------------------------
def sqrt(number):
    return number ** 0.5

def cbrt(number):
    return number ** (1/3)

def rdrt(number, root):
    return number ** (1/root)

# -------------------------
# Percentages
# -------------------------
def per_100(number):
    return number / 100

def per_def(number, defi):
    return (number / 100) * defi

# -------------------------
# Constants
# -------------------------
def pi():
    return 3.141592653589793

def e():
    return 2.718281828459045

def g():
    return 9.8  # acceleration due to gravity (m/s²)

def c():
    return 3e8  # speed of light (m/s)

def R():
    return 8.314  # ideal gas constant (J/(mol·K))

# -------------------------
# Keywords reference
# -------------------------
def keywords():
    print("""
          1 >> Basic operations
          2 >> Powers
          3 >> Area and perimeters of shapes
          4 >> Degree to radians
          5 >> Radian to Degree
          6 >> Table
          7 >> Weight
          8 >> Distance
          9 >> Time
          10 >> Fluid
          11 >> Roots
          12 >> Percents
          13 >> Constants
          """)
    try:
        cho = int(input(":: Which type keywords do you want ::> "))
    except ValueError:
        print(":: Enter the choice in digits ::")
    else:
        match cho:
            case 1:
                print("""
                      add(number_1, number_2)
                      sub(number_1, number_2)
                      mul(number_1, number_2)
                      div(number_1, number_2)
                      """)
            case 2:
                print("""
                      sq(number)
                      cb(number)
                      exp(number, expo)
                      """)
            case 3:
                print("""
                      Areas:
                          ar_circle(radius)
                          ar_sq(length)
                          ar_rect(length, bredth)
                          ar_tri(side_1, side_2, side_3)
                      Perimeters:
                          per_circle(radius)
                          per_sq(length)
                          per_rect(length, bredth)
                          per_tri(side_1, side_2, side_3)
                      """)
            case 4:
                print("""
                      sin_ang(x)
                      cos_ang(x)
                      tan_ang(x)
                      """)
            case 5:
                print("""
                      sin_val(deg)
                      cos_val(deg)
                      tan_val(deg)
                      """)
            case 6:
                print("""
                      table(num)
                      """)
            case 7:
                print("""
                      kg(gram)
                      gram(kg)
                      g_mgram(gram)
                      kg_mgram(kg)
                      mgram_g(mgram)
                      mgram_kg(mgram)
                      """)
            case 8:
                print("""
                      me(kilo)
                      kme(me)
                      kme_mm(kme)
                      mm_kme(mm)
                      m_cm(m)
                      cm_m(cm)
                      """)
            case 9:
                print("""
                      sec_hrs(sec)
                      hrs_sec(hrs)
                      sec_min(sec)
                      min_sec(min)
                      min_hrs(min)
                      """)
            case 10:
                print("""
                      l_ml(l)
                      ml_l(ml)
                      """)
            case 11:
                print("""
                      sqrt(number)
                      cbrt(number)
                      rdrt(number, root)
                      """)
            case 12:
                print("""
                      per_100(number)
                      per_def(number, defi)
                      """)
            case 13:
                print("""
                      pi() -> 3.141592653589793
                      e()  -> 2.718281828459045
                      g()  -> 9.8 m/s²
                      c()  -> 3 x 10^8 m/s
                      R()  -> 8.314 J/(mol·K)
                      """)
            case _:
                print(":: Invalid choice ::")
