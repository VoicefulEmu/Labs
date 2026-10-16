# %%
import numpy as np
import math

##knowns
T0 = 72  # deg F
T0_R = T0 + 459.67  # deg R
P0 = 64.54  # mmHg
P_atm = 12.57  # psi
h = 0.375  # in
l = 4.2  # in
R_air = 287 * 5.97994  # ft*lbf/(slug*R)
gamma = 1.4

X_taps = np.array([-0.2, 0.3, 1, 1.7, 2.4, 3.1, 3.8])


def w(x):
    """definition of the diverging portion of the nozzle
    4.2 in long
    0.375 in deep
    defined width below where x is distance from the throat"""
    return 0.4 + 0.04762 * x


def A_cross(x, h):
    """cross-sectional area of the nozzle given distance x from the throat and height h"""
    return w(x) * h


# %%


# %%

# Determine P_exit and m_dot for just choked flow, using dimensions of the nozzle

# Calculate cross sectional areas
A_star_1 = A_cross(0, h)
A_exit = A_cross(l, h)
A_taps = A_cross(X_taps, h)

# print("A_star_1: " + str(A_star_1) + " in^2")
# print("A_exit: " + str(A_exit) + " in^2")
# print("A_taps: " + str(A_taps) + " in^2")
print("A_exit/A_star_1: " + str(A_exit / A_star_1) + " (dimensionless)")

P_p0_calculator = 0.88051683

P_exit_sub = P_p0_calculator * P_atm
print("P_exit_sub: " + str(P_exit_sub) + " psi")

m_dot = (
    (P_atm * A_star_1 / math.sqrt(R_air * T0_R))
    * np.sqrt(gamma)
    * ((gamma + 1) / 2) ** (-(gamma + 1) / (2 * (gamma - 1)))
)
print("m_dot: " + str(m_dot) + " slugs/s")  # in units slugs/s
print("m_dot (lbm/s): " + str(m_dot * 32.174) + " lbm/s")  # convert slugs/s to lbm/s


# %%

##Calcualte Pressure Ratios for each tap (P/P0)

# Calculate the expected pressure for each tap (P_expected)
# P_p0_taps =
# P_expected = P_atm * P_p0_taps


# Load measured pressure data from text file and calculate pressure ratios (P/P0)
P_taps = np.loadtxt(
    "C:/Users/lamor/OneDrive/Documents/BYUINFO/Fall 2026/ME EN 510/Labs/Lab1/BryceandEzra.txt",
    skiprows=1,
)
P_taps_table = np.atleast_2d(P_taps)
print("BryceandEzra.txt data table:")
print("\t".join(f"Column {i + 1}" for i in range(P_taps_table.shape[1])))
for row in P_taps_table:
    print("\t".join(str(value) for value in row))
# P_P0_M = P_taps[1:4,:] / P_atm
# print("P_P0_M: " + str(P_P0_M) + " measured (dimensionless)")

# %%
