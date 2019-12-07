from sympy import nan, sqrt, sympify


def quadratic(a, b, c):
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def linear(a, b):
    return sympify(-b / a)


def bairstow(r, s, coeffs_a, acc_error=0.000000001, roots=None):
    if roots is None:
        roots = []

    if len(coeffs_a) < 2:
        return nan

    if len(coeffs_a) == 2:
        roots.append(linear(coeffs_a[0], coeffs_a[1]).round(4))
        return roots

    if len(coeffs_a) == 3:
        roots += [i.round(4) for i in quadratic(coeffs_a[0], coeffs_a[1], coeffs_a[2])]
        return roots

    eps_r = acc_error + 1
    eps_s = acc_error + 1
    ds = 0
    dr = 0

    while eps_r > acc_error or eps_s > acc_error:

        r += dr
        s += ds

        coeffs_b = list(coeffs_a)

        coeffs_b[0] = coeffs_a[0]
        coeffs_b[1] = coeffs_a[1] + r * coeffs_b[0]

        for n in range(2, len(coeffs_a)):
            coeffs_b[n] = coeffs_a[n] + r * coeffs_b[n - 1] + s * coeffs_b[n - 2]

        coeffs_c = coeffs_b[:len(coeffs_b) - 1]
        coeffs_c[0] = coeffs_b[0]
        coeffs_c[1] = coeffs_b[1] + r * coeffs_c[0]

        for n in range(2, len(coeffs_b) - 1):
            coeffs_c[n] = coeffs_b[n] + r * coeffs_c[n - 1] + s * coeffs_c[n - 2]

        try:
            dr = (coeffs_b[-2] * coeffs_c[-2] - coeffs_b[-1] * coeffs_c[-3]) / (
                        coeffs_c[-1] * coeffs_c[-3] - coeffs_c[-2] ** 2)
        except:
            dr = 0
        try:
            ds = (coeffs_b[-1] * coeffs_c[-2] - coeffs_b[-2] * coeffs_c[-1]) / (
                        coeffs_c[-1] * coeffs_c[-3] - coeffs_c[-2] ** 2)
        except:
            ds = 0

        try:
            eps_r = abs(dr / r)
        except:
            pass
        try:
            eps_s = abs(ds / s)
        except:
            pass

        if eps_r == nan or eps_s == nan:
            break

        if dr == 0 and ds == 0:
            break

    coeffs_b = coeffs_b[:-2]

    roots.append((r + sqrt(r ** 2 + 4 * s)) / 2)
    roots.append((r - sqrt(r ** 2 + 4 * s)) / 2)

    if len(coeffs_b) > 3:
        return bairstow(r, s, coeffs_b, acc_error, roots)
    elif len(coeffs_b) == 3:
        roots += quadratic(coeffs_b[0], coeffs_b[1], coeffs_b[2])
    elif len(coeffs_b) == 2:
        roots.append(linear(coeffs_b[0], coeffs_b[1]))

    return [i.round(6) for i in roots]
