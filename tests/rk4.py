import math
import matplotlib.pyplot as plt
import numpy as np

# Parámetros y condiciones iniciales
parameters = [0.00233, 0.000125, 0.1, 0.15, 9.81]
ics = [math.pi / 3, 0, 0, 9.18, 0, 251.98]


# Definimos las constantes del sistema
def getParams():
    A, CC, M, l, g = parameters
    return A, CC, M, l, g


# Condiciones iniciales
def getInitialConditions():
    return ics


# Ecuaciones diferenciales
def equations(t, y, params):
    A, CC, M, l, g = params

    theta0, thetaP0, phi0, phiP0, psi0, psiP0 = y

    # Definimos las ecuaciones diferenciales
    diffPhiP0 = ((-((2 * (A - CC) * phiP0 * np.cos(theta0) - CC * psiP0) * thetaP0 * np.sin(theta0)) -
                 (CC * np.cos(theta0) ** 2 + A * np.sin(theta0) ** 2) * phiP0 -
                 CC * psiP0 * np.cos(theta0))
                 / (CC * np.cos(theta0) ** 2 + A * np.sin(theta0) ** 2))

    diffThetaP0 = ((M * g * l + (A - CC) * phiP0 ** 2 * np.cos(theta0) - CC * phiP0 * psiP0) * np.sin(theta0)) / A

    diffPsiP0 = -phiP0 * np.cos(theta0) + phiP0 * thetaP0 * np.sin(theta0)

    return np.array([thetaP0, diffThetaP0, phiP0, diffPhiP0, psiP0, diffPsiP0])


# Método de Runge-Kutta 4
def rk4(func, t, y, dt, params):
    k1 = func(t, y, params)
    k2 = func(t + dt / 2, y + dt * k1 / 2, params)
    k3 = func(t + dt / 2, y + dt * k2 / 2, params)
    k4 = func(t + dt, y + dt * k3, params)
    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


# Resolver el sistema de ecuaciones diferenciales
def solveEqDif(duration, dt):
    params = getParams()
    y0 = getInitialConditions()
    tValues = np.arange(0, duration, dt)
    yValues = np.zeros((len(tValues), len(y0)))

    # Establecer condiciones iniciales
    yValues[0] = y0

    for i in range(1, len(tValues)):
        yValues[i] = rk4(equations, tValues[i - 1], yValues[i - 1], dt, params)

    return tValues, yValues


# Función para graficar theta(t)
def plotTheta(tValues, yValues):
    thetaValues = yValues[:, 0]
    plt.figure(figsize=(8, 5))
    plt.plot(tValues, thetaValues, label=r"$\theta(t)$", color="blue")
    plt.title("Evolución de $\Theta(t)$")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("$\Theta$ (rad)")
    plt.grid(True)
    plt.legend()
    plt.show()


# Función para graficar phi(t)
def plotPhi(tValues, yValues):
    phiValues = yValues[:, 2]
    plt.figure(figsize=(8, 5))
    plt.plot(tValues, phiValues, label=r"$\phi(t)$", color="green")
    plt.title("Evolución de $\Phi(t)$")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("$\Phi$ (rad)")
    plt.grid(True)
    plt.legend()
    plt.show()


# Función para graficar psi(t)
def plotPsi(tValues, yValues):
    psiValues = yValues[:, 4]
    plt.figure(figsize=(8, 5))
    plt.plot(tValues, psiValues, label=r"$\psi(t)$", color="red")
    plt.title("Evolución de $\Psi(t)$")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("$\Psi$ (rad)")
    plt.grid(True)
    plt.legend()
    plt.show()


# Función principal
def main():
    duration = 3
    dt = 0.001

    tValues, yValues = solveEqDif(duration, dt)

    # Graficar las soluciones
    plotTheta(tValues, yValues)
    plotPhi(tValues, yValues)
    plotPsi(tValues, yValues)


if __name__ == "__main__":
    main()
