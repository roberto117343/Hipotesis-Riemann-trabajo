#* «Copyright 2023 Roberto Reinosa»
#*
#* This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#*

import matplotlib.pyplot as plt
import math


def zeta(s):

    sumatorio_a = 0.0

    resultado = (1.0 / (1.0 - pow(2.0, 1.0 - s)))

    for n in range(0, 100):

        sumatorio_b = 0.0

        for k in range(0, n + 1):

            sumatorio_b += pow(-1, k)\
                           * (math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))\
                           * pow(k + 1.0, -s)

        sumatorio_a += (1.0 / pow(2.0, n + 1.0)) * sumatorio_b

    return resultado * sumatorio_a


valor_imaginario = -30.1

valores_real = []
valores_imaginario = []
valores_parte_imaginaria = []

while valor_imaginario < 30.0:

    valores_real.append(zeta(complex(0.5, valor_imaginario)).real)
    valores_imaginario.append(zeta(complex(0.5, valor_imaginario)).imag)
    valores_parte_imaginaria.append(valor_imaginario)

    valor_imaginario += 0.01

plt.scatter(valores_parte_imaginaria, valores_imaginario, s=1)
plt.scatter(valores_parte_imaginaria, valores_real, s=1)

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')

plt.show()
