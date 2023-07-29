#* «Copyright 2023 Roberto Reinosa»
#*
#* This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#*

import matplotlib.pyplot as plt
import math as ma


def comprobador_primo(x):

    for i in range(2, x):

        if (x % i) == 0:

            return False

    return True


def pi(x):

    contador_primos = 0

    for i in range(2, x+1):

        if comprobador_primo(i):

            contador_primos += 1

    return contador_primos


def teorema(x):

    return x/ma.log(x)


def li(x):

    x = ma.log(x)

    valor = 0.577215664 + ma.log(x)

    sumatorio = 0.0

    for n in range(1, 106):

        sumatorio += pow(x, n) / (n*ma.factorial(n))

    valor += sumatorio
    return valor


def funcion_mobius(valor):

    contador = 2
    valores_factores_primos = []

    while contador < valor:

        if valor % contador == 0:

            valor /= contador
            valores_factores_primos.append(contador)
            continue

        contador += 1

    valores_factores_primos.append(contador)

    visited = set()
    dup = {x for x in valores_factores_primos if x in visited or (visited.add(x) or False)}

    if valor == 1:

        return 1

    elif len(dup) == 0:

        if len(valores_factores_primos) % 2.0 == 0:

            return 1

        else:

            return -1

    else:

        return 0


def R(valor):

    resultado = 0.0

    for n in range(1, 500):

        resultado += (funcion_mobius(n)/n) * li(pow(valor, 1.0/n))

    return resultado


def pi_0(valor):

    ceros_zeta = [14.13499999999998, 21.023000000000167, 25.011000000001417,
                  30.425000000002356, 32.936000000001975, 37.58700000000075, 40.918999999999315,
                  43.32799999999745, 48.00599999999616, 49.77399999999415, 52.97099999999303,
                  56.4469999999922, 59.34799999999083, 60.83199999998855, 65.11299999998853,
                  67.07999999999116, 69.54699999999376, 72.06799999999565, 75.70499999999755,
                  77.14500000000153, 79.33800000000379, 82.91100000000539, 84.73600000000734,
                  87.42600000000955, 88.81000000001278, 92.49200000001441, 94.65200000001651,
                  95.87100000002137, 98.83200000002294, 101.31800000002418, 103.72600000002602,
                  105.4470000000294, 107.16900000003135, 111.03000000003335, 111.87500000003739,
                  114.3210000000394, 116.22700000004126, 118.79100000004239, 121.3710000000436,
                  122.94700000004677, 124.25700000005061, 127.51700000005216, 129.5790000000538,
                  131.08800000005667, 133.4980000000585, 134.75700000006114, 138.1170000000627,
                  139.73700000006463, 141.12400000006787, 143.11200000006963, 146.00100000007086,
                  147.42300000007282, 150.05400000007475, 150.92600000007891, 153.02500000008072,
                  156.11300000008194, 157.59800000008372, 158.8500000000868, 161.1890000000883,
                  163.03100000008936, 165.53800000009022, 167.1850000000918, 169.09500000009416,
                  169.91200000009806, 173.4120000000993, 174.7550000001009, 176.44200000010315,
                  178.37800000010466, 179.9170000001062, 182.208000000107, 184.87500000010863,
                  185.59900000011208, 187.22900000011455, 189.41700000011582, 192.0270000001167,
                  193.0800000001193, 195.26600000012056, 196.87700000012293, 198.016000000125,
                  201.265000000126, 202.49400000012753, 204.1900000001303, 205.39500000013268,
                  207.90700000013356, 209.5770000001343, 211.6910000001352, 213.34800000013684,
                  214.54800000013967, 216.17000000014113, 219.06800000014192, 220.7150000001435,
                  221.43100000014692, 224.0080000001486, 224.98400000015084, 227.42200000015185,
                  229.3380000001528, 231.25100000015468, 231.9880000001582, 233.69400000016006,
                  236.52500000016101, 237.77000000016213, 239.5560000001634, 241.05000000016523,
                  242.82400000016645, 244.07100000016757, 247.13700000016868, 248.1020000001733,
                  249.57400000017645, 251.01500000017802, 253.07100000017866, 255.30700000017967,
                  256.38100000017624, 258.6110000001689, 259.8750000001557, 260.8060000001337,
                  263.57600000013025, 265.55800000012397, 266.6150000001085, 267.9220000000967,
                  269.97100000009124, 271.49500000008624, 273.46000000008274, 275.5880000000754,
                  276.45300000005494, 278.25100000004585, 279.230000000037, 282.4660000000321,
                  283.2120000000145, 284.83600000000473, 286.6679999999996, 287.9119999999917,
                  289.57999999998566, 291.8469999999822, 293.55899999997513, 294.96599999996334,
                  295.57399999994897, 297.9799999999422, 299.8409999999388, 301.6499999999342,
                  302.6969999999238, 304.86499999991787, 305.7289999999022, 307.2199999998956,
                  310.1099999998917, 311.16599999988347, 312.42799999987034, 313.98599999986214,
                  315.47599999985556, 317.7349999998523, 318.8539999998449, 321.1609999998381,
                  322.144999999822, 323.46699999980984, 324.8629999998031, 327.44399999979936,
                  329.0339999997928, 329.9539999997782, 331.4749999997709, 333.6459999997649,
                  334.2119999997515, 336.84199999974663, 338.33999999974225, 339.858999999735,
                  341.0429999997213, 342.0549999997117, 344.66199999970735, 346.3479999997009,
                  347.27299999969097, 349.3169999996856, 350.4089999996741, 351.878999999668,
                  353.48899999966335, 356.01799999966084, 357.15199999965074, 357.9529999996318,
                  359.7439999996229, 361.28999999961735, 363.3319999996144, 364.73699999960985,
                  366.2129999996036, 367.9939999995973, 368.9689999995838]

    resultado_sumatorio = 0.0

    for y in range(0, len(ceros_zeta)):

        resultado_sumatorio += (ma.sin(ceros_zeta[y] * ma.log(valor))) / ceros_zeta[y]

    resultado = R(valor) - 2 * (ma.sqrt(valor) / ma.log(valor)) * resultado_sumatorio

    return resultado


valores_i = []
valores_pi = []
valores_teorema = []
valores_li = []
valores_pi_0 = []

for i in range(2, 501):

    valores_pi.append(pi(i))
    valores_teorema.append(teorema(i))
    valores_i.append(i)
    valores_li.append(li(i) - li(2))
    valores_pi_0.append(pi_0(i))

plt.scatter(valores_i, valores_pi, s=1)
plt.scatter(valores_i, valores_teorema, s=1)
plt.scatter(valores_i, valores_li, s=1)
plt.scatter(valores_i, valores_pi_0, s=1)

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')
plt.show()
