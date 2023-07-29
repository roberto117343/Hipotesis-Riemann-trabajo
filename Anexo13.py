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


s = float(input("Introduce el valor de la parte imaginaria del número complejo s: "))
print(zeta(complex(0.5, s)))
