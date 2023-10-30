import numpy as np

x0 = 0
y0 = 0
z0 = 0.9

yp = -0.18
xp = -0.8
zp = 0.3

#What is the lenght of the vectors from experimental data?
print("Length of x_0: ", np.sqrt(x0**2 + y0**2 + z0**2))
print("Length of x_-: ", np.sqrt(xp**2 + yp**2 + zp**2))

sx = np.array([[0, 1], [1, 0]])
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]])

id = np.array([[1, 0], [0, 1]])

# Define the state from experiment
rho_0 = 0.5 * (id + x0 * sx + y0 * sy + z0 * sz)
rho_plus = 0.5 * (id + xp * sx + yp * sy + zp * sz)

#What do they look like?
print("rho_0: ", rho_0)
print("rho_minus: ", rho_plus)

#The states we should get:
psi_0 = np.array([[1], [0]])
psi_plus = 1/(np.sqrt(2)) * np.array([[1], [-1]])

#These density matrices look like:
print("rho_0_expected: ", np.outer(psi_0, psi_0))
print("rho_minus_expected: ", np.outer(psi_plus, psi_plus))

F_0 = np.transpose(psi_0) @ rho_0 @ psi_0
F_plus = np.transpose(psi_plus) @ rho_plus @ psi_plus

print("Fidelity of 0: ", F_0)
print("Fidelity of minus (antidiagonal because we went with the wrong axis in the QWP): ", F_plus)