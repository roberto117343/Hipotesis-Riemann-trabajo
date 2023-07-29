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


archivo_guardado = open("archivo de guardado", 'w')

valor_real = -10.1

while valor_real < 4.0:

    valor_imaginario = -10.1

    while valor_imaginario < 40.0:

        s = complex(valor_real, valor_imaginario)

        resultado = zeta(s)

        if abs(resultado) < 10:

            archivo_guardado.write(str(s.real) + " " + str(s.imag) + " " + str(abs(resultado)) + "\r\n")

        valor_imaginario += 0.2

    valor_real += 0.2

archivo_guardado.close()
