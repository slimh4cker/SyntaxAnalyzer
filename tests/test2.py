import math
import pyweierstrass.weierstrass as ws
import matplotlib.pyplot as plt
import numpy as np
from mpmath import exp  # Para números complejos
import cmath

# Definir las constantes del trompo
params = [0.00233, 0.000125, 0.1, 0.15, 9.81]
params2 = [0.001, 0.002, 0.05, 2, 9.81]

# Condiciones iniciales
ics = [math.pi / 3, 0, 0, 9.18, 0, 251.98]
ics2 = [math.pi / 6, 0, 0, 9, 0, 240]


# ------------- Seccion de Calculos -------------------
def calculateConstants(parameters, initialConditions):
    """Calcular las constantes a, b, c."""
    A = parameters[0]
    CC = parameters[1]
    M = parameters[2]
    l = parameters[3]
    g = parameters[4]
    theta0, thetaPoint0, phi0, phiPoint0, psi0, psiPoint0 = initialConditions
    a = (A * phiPoint0) * (math.sin(theta0) ** 2) + CC * (psiPoint0 + phiPoint0 * math.cos(theta0)) * math.cos(theta0)
    b = CC * (psiPoint0 + phiPoint0 * math.cos(theta0))
    c = 0.5 * A * (thetaPoint0 ** 2) + (
            (a - b * math.cos(theta0)) ** 2 / (2 * A * math.sin(theta0) ** 2)) + M * g * l * math.cos(theta0)
    return a, b, c


def calculateValues(a, b, c, parameters):
    """
    Devuelve: soluciones, cosAlpha, cosBeta, cosGamma, e1, e2, e3, g2, g3,
              omega1, omega3, alpha, beta, wpell, wpk, ell, k, zetak, zetaell.
    """
    from sympy import symbols, Eq, solve

    # Extraer parámetros
    A = parameters[0]
    M = parameters[2]
    l = parameters[3]
    g = parameters[4]

    # Resolver el polinomio
    x = symbols('x')
    f = - ((a - b * x) ** 2) - 2 * A * M * g * l * (x - x ** 3) + 2 * A * c * (1 - x ** 2)
    solutions = solve(Eq(f, 0), x)
    # Soluciones del polinomio
    cosAlpha = float(solutions[0].as_real_imag()[0])
    cosBeta = float(solutions[1].as_real_imag()[0])
    cosGamma = float(solutions[2].as_real_imag()[0])

    # Calcular e1, e2, e3
    e1 = (M * g * l) / (2 * A) * cosGamma - (2 * A * c + b ** 2) / (12 * A ** 2)
    e2 = (M * g * l) / (2 * A) * cosBeta - (2 * A * c + b ** 2) / (12 * A ** 2)
    e3 = (M * g * l) / (2 * A) * cosAlpha - (2 * A * c + b ** 2) / (12 * A ** 2)

    # Calcular g2 y g3
    g2 = -4 * (e1 * e2 + e1 * e3 + e2 * e3)
    g3 = 4 * e1 * e2 * e3

    # Calcular omega1 y omega3
    omega1, omega3 = ws.omega_from_g(g2, g3)

    # Calcular alpha y beta
    alpha = (2 * A) / (M * g * l)
    beta = (2 * A * c + (b ** 2)) / (6 * A * M * g * l)

    # Calcular valores de wp, ell y k
    wpell = (M * g * l) / (2 * A) - (2 * A * c + b ** 2) / (12 * A ** 2)
    wpk = -(M * g * l) / (2 * A) - (2 * A * c + b ** 2) / (12 * A ** 2)
    ell = ws.invwp(wpell, (omega1, omega3))
    k = ws.invwp(wpk, (omega1, omega3))

    # Calcular zetas
    zetak = ws.wzeta(k, (omega1, omega3))
    zetaell = ws.wzeta(ell, (omega1, omega3))

    # Retornar todos los valores calculados
    return {
        "solutions": solutions,
        "cosAlpha": cosAlpha,
        "cosBeta": cosBeta,
        "cosGamma": cosGamma,
        "e1": e1,
        "e2": e2,
        "e3": e3,
        "g2": g2,
        "g3": g3,
        "omega1": omega1,
        "omega3": omega3,
        "alpha": alpha,
        "beta": beta,
        "wpell": wpell,
        "wpk": wpk,
        "ell": ell,
        "k": k,
        "zetak": zetak,
        "zetaell": zetaell
    }


def calculatePhiRhs(zetak, zetaell, omega1, omega3, k, ell, t):
    """Calcular phiRhs."""
    exponential_expr = cmath.exp(2 * t * (zetak - zetaell))
    #debug = cmath.exp(2 * (zetak - zetaell))
    #print(debug)
    phiRhsResult = (exponential_expr *
                    ws.wsigma(t - k + omega3, (omega1, omega3)) *
                    ws.wsigma(t + ell + omega3, (omega1, omega3)) /
                    ws.wsigma(t + k + omega3, (omega1, omega3)) *
                    ws.wsigma(t - ell + omega3, (omega1, omega3))
                    )
    return phiRhsResult


def calculatePsiRhs(zetak, zetaell, omega1, omega3, k, ell, t):
    """Calcular psiRhs."""
    exponential_expr = exp(2 * t * (zetak + zetaell))
    psiRhsResult = (exponential_expr *
                    ws.wsigma(t - k + omega3, (omega1, omega3)) *
                    ws.wsigma(t - ell + omega3, (omega1, omega3)) /
                    ws.wsigma(t + k + omega3, (omega1, omega3)) *
                    ws.wsigma(t + ell + omega3, (omega1, omega3))
                    )
    return psiRhsResult


def phaseFred(z):
    """Calcular la fase de Fred."""
    z = np.array(z, dtype=np.complex128)
    arg = np.angle(z)
    df = np.concatenate([[0], np.cumsum(np.round(np.diff(arg) / (2 * np.pi)))])
    arg = arg - 2 * np.pi * df
    return arg


def phiEx(tValues, parameters, initialConditions):
    import mplcursors
    """Calcular PhiEx y graficar tanto la parte real como la imaginaria de phiRhs."""

    # Calcular constantes y valores esenciales
    a, b, c = calculateConstants(parameters, initialConditions)

    # Calcular todos los valores utilizando la función consolidada
    results = calculateValues(a, b, c, parameters)

    # Extraer los valores necesarios del diccionario de resultados
    zetak = results["zetak"]
    zetaell = results["zetaell"]
    omega1 = results["omega1"]
    omega3 = results["omega3"]
    k = results["k"]
    ell = results["ell"]

    phiRhsRealValues = [
        np.real(calculatePhiRhs(zetak, zetaell, omega1, omega3, k, ell, t)) for t in tValues
    ]

    phiRhsImagValues = [
        np.imag(calculatePhiRhs(zetak, zetaell, omega1, omega3, k, ell, t)) for t in tValues
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(tValues, phiRhsRealValues, label=r'Parte real de $\phi_{RHS}$', color='blue')
    plt.xlabel('Tiempo (t)')
    plt.ylabel(r'Parte real de $\phi_{RHS}$')
    plt.title('Gráfica de la parte real de $\phi_{RHS}$ en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(tValues, phiRhsImagValues, label=r'Parte imaginaria de $\phi_{RHS}$', color='red')
    plt.xlabel('Tiempo (t)')
    plt.ylabel(r'Parte imaginaria de $\phi_{RHS}$')
    plt.title('Gráfica de la parte imaginaria de $\phi_{RHS}$ en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()

    return phiRhsRealValues, phiRhsImagValues


def psiEx(tValues, parameters, initialConditions):
    """Calcular PsiEx."""

    # Calcular constantes y valores esenciales
    a, b, c = calculateConstants(parameters, initialConditions)

    # Calcular todos los valores
    results = calculateValues(a, b, c, parameters)

    # Extraer los valores del diccionario de resultados
    zetak = results["zetak"]
    zetaell = results["zetaell"]
    omega1 = results["omega1"]
    omega3 = results["omega3"]
    k = results["k"]
    ell = results["ell"]

    # Calcular los valores de psiRhs
    psiRhsValues = [
        np.real(calculatePsiRhs(zetak, zetaell, omega1, omega3, k, ell, t)) for t in tValues
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(tValues, psiRhsValues, label=r'$\psi_{RHS, real}$', color='blue')
    plt.xlabel('Tiempo (t)')
    plt.ylabel(r'Parte real de $\psi_{RHS}$')
    plt.title('Gráfica de la parte real de $\psi_{RHS}$ en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()

    return psiRhsValues


def thetaEx(t, parameters, initialConditions):
    """Función principal para calcular theta."""
    try:
        a, b, c = calculateConstants(parameters, initialConditions)
        results = calculateValues(a, b, c, parameters)

        # Extraer los valores requeridos del diccionario de resultados
        omega1 = results["omega1"]
        omega3 = results["omega3"]
        alpha = results["alpha"]
        beta = results["beta"]

        # Calcular wpValue y theta
        wpValue = ws.wp(t + omega3, (omega1, omega3))
        theta = math.acos(float((alpha * wpValue + beta).real))

        return theta
    except Exception as e:
        print(f"Error en la función thetaEx: {e}")
        return None


def plotTheta(totalTime, h, thetaEx, params, ics):
    """ Graficar a theta conforme el tiempo """
    seconds = [i * h for i in range(int(totalTime / h) + 1)]
    thetaValues = []
    for t in seconds:
        theta = thetaEx(t, params, ics)
        if theta is not None:
            thetaValues.append(theta)
    plt.plot(seconds[:len(thetaValues)], thetaValues)
    plt.xlabel('Tiempo (t)')
    plt.ylabel('Theta (rad)')
    plt.title('Gráfica de $\Theta_{ex}$ en función de t')
    plt.grid(True)
    plt.show()


def plotPsiEx(t_values, parameters, initialConditions):
    """Graficar PsiEx en función de t."""
    psi_ex = psiEx(t_values, parameters, initialConditions)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, psi_ex, label=r'$\Psi_{ex}$', color='blue')
    plt.xlabel('Tiempo (t)')
    plt.ylabel(r'$\psi_{ex}$')
    plt.title('Gráfica de $\psi_{ex}$ en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()


def plotPhiEx(t_values, parameters, initialConditions):
    """Graficar PsiEx en función de t."""
    phiExResult = phiEx(t_values, parameters, initialConditions)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, phiExResult, label=r'$\Phi_{ex}$', color='blue')
    plt.xlabel('Tiempo (t)')
    plt.ylabel(r'$\phi_{ex}$')
    plt.title('Gráfica de $\phi_{ex}$ en función del tiempo')
    plt.legend()
    plt.grid(True)
    plt.show()


# Tests de las funciones
totalTime = 6
h = 0.01
tValuesTest = np.arange(0, totalTime + h, h)
#print(f'Theta: {thetaEx(1, params, ics)}')
#plotTheta(totalTime, h, thetaEx, params, ics)
#plotPsiEx(tValuesTest, params, ics)
#plotPhiEx(tValuesTest, params, ics)
phiEx(tValuesTest, params, ics)
#plotPhiEx(tValuesTest, params, ics)
#print(f'psiEx = {psiEx(tValuesTest, params, ics)}')