import math
from sympy import symbols, Eq, solve
import pyweierstrass.weierstrass as ws
import matplotlib.pyplot as plt
import numpy as np
from mpmath import exp  # Para numeros complejos

# params contiene [A,C,M,l,g] (datos físicos del trompo)
params = [0.00233, 0.000125, 0.1, 0.15, 9.81]
params2 = [0.001, 0.002, 0.05, 2, 9.81]

# ics contiene las condiciones iniciales [theta0,thetaP0,phi0,phiP0,psi0,psiP0]
ics = [math.pi / 3, 0, 0, 9.18, 0, 251.98]
ics2 = [math.pi / 6, 0, 0, 9, 0, 240]


def thetaEx(t, parameters, initial_conditions, cache={}):
    # Verificar si ya se realizó el pre-cálculo
    if not cache:
        # Declarar valores iniciales
        A = parameters[0]
        CC = parameters[1]
        M = parameters[2]
        l = parameters[3]
        g = parameters[4]
        theta0 = initial_conditions[0]
        thetaPoint0 = initial_conditions[1]
        phi0 = initial_conditions[2]
        phiPoint0 = initial_conditions[3]
        psi0 = initial_conditions[4]
        psiPoint0 = initial_conditions[5]

        # Calcular constantes y resolver polinomio
        a = (A * phiPoint0) * (math.sin(theta0) ** 2) + CC * (psiPoint0 + phiPoint0 * math.cos(theta0)) * math.cos(
            theta0)
        b = CC * (psiPoint0 + phiPoint0 * math.cos(theta0))
        c = 0.5 * A * (thetaPoint0 ** 2) + (
                (a - b * math.cos(theta0)) ** 2 / (2 * A * math.sin(theta0) ** 2)) + M * g * l * math.cos(theta0)

        x = symbols('x')
        f = - ((a - b * x) ** 2) - 2 * A * M * g * l * (x - x ** 3) + 2 * A * c * (1 - x ** 2)
        solutions = solve(Eq(f, 0), x)

        # Asignar soluciones
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

        # Calcular omega1, omega3, alpha, beta
        omega1, omega3 = ws.omega_from_g(g2, g3)
        alpha = (2 * A) / (M * g * l)
        beta = (2 * A * c + (b ** 2)) / (6 * A * M * g * l)

        # Guardar en cache
        cache['omega1'] = omega1
        cache['omega3'] = omega3
        cache['alpha'] = alpha
        cache['beta'] = beta

        wpell = (M * g * l) / (2 * A) - (2 * A * c + b ** 2) / (12 * A ** 2)
        print(wpell)
        wpk = -(M * g * l) / (2 * A) - (2 * A * c + b ** 2) / (12 * A ** 2)
        print(wpk)
        ell = ws.invwp(wpell, (cache['omega1'], cache['omega3']))
        print(ell)
        k = ws.invwp(wpk, (cache['omega1'], cache['omega3']))
        print(k)
        zetak = ws.wzeta(k, (cache['omega1'], cache['omega3']))
        print(zetak)
        zetaell = ws.wzeta(ell, (cache['omega1'], cache['omega3']))
        print(zetaell)

        # Calcular phiRhs
        def phiRhs(t):
            exponential_expr = math.exp(2 * t * (zetak - zetaell))
            phiRhsResult = (exponential_expr * ws.wsigma(t - k + omega3, (cache['omega1'], cache['omega3'])) *
                            ws.wsigma(t + ell + omega3, (cache['omega1'], cache['omega3'])) /
                            ws.wsigma(t + k + omega3, (cache['omega1'], cache['omega3'])) *
                            ws.wsigma(t - ell + omega3, (cache['omega1'], cache['omega3']))
                            )
            return phiRhsResult

        # Calcular psiRhs
        def psiRhs(t):
            exponential_expr = math.exp(2 * t * (zetak + zetaell)).real
            psiRhsResult = (exponential_expr * ws.wsigma(t - k + omega3, (cache['omega1'], cache['omega3'])) *
                            ws.wsigma(t - ell + omega3, (cache['omega1'], cache['omega3'])) /
                            ws.wsigma(t + k + omega3, (cache['omega1'], cache['omega3'])) *
                            ws.wsigma(t + ell + omega3, (cache['omega1'], cache['omega3']))
                            )
            return psiRhsResult

        cache['phiRhs'] = phiRhs
        cache['psiRhs'] = psiRhs

        def phaseFred(z):
            arg = np.angle(z)
            # Calcula las diferencias
            df = np.concatenate([[0], np.cumsum(np.round(np.diff(arg) / (2 * np.pi)))])
            arg = arg - 2 * np.pi * df
            return arg

    # Usar valores almacenados en cache
    try:
        wpValue = ws.wp(t + cache['omega3'], (cache['omega1'], cache['omega3']))
        theta = math.acos(float((cache['alpha'] * wpValue + cache['beta']).real))
        return theta
    except Exception as e:
        print(f"Error en la función wp: {e}")
        return None


# Prueba:
cache = {}

totalTime = 5
h = 0.01

print(f'Theta: {thetaEx(5, params, ics)}')


def plotTheta(totalTime, h, thetaEx, params, ics):
    seconds = [i * h for i in range(int(totalTime / h) + 1)]
    thetaValues = []
    for t in seconds:
        theta = thetaEx(t, params, ics)
        if theta is not None:
            thetaValues.append(theta)
    plt.plot(seconds[:len(thetaValues)], thetaValues)
    plt.xlabel('Tiempo (t)')
    plt.ylabel('Theta (rad)')
    plt.title('Gráfica de Theta en función de t')
    plt.grid(True)
    plt.show()


plotTheta(totalTime, h, thetaEx, params, ics)
