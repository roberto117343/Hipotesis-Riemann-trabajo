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

    for n in range(0, 300):

        sumatorio_b = 0.0

        for k in range(0, n + 1):

            sumatorio_b += pow(-1, k)\
                           * (math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))\
                           * pow(k + 1.0, -s)

        sumatorio_a += (1.0 / pow(2.0, n + 1.0)) * sumatorio_b

    return resultado * sumatorio_a


valor_parte_imaginaria_inicio = 14.1
valor_parte_imaginaria = valor_parte_imaginaria_inicio

while valor_parte_imaginaria < 400.0:

    valor_funcion_zeta = zeta(complex(0.5, valor_parte_imaginaria))

    valor_real = valor_funcion_zeta.real
    valor_imaginario = valor_funcion_zeta.imag

    if valor_parte_imaginaria == valor_parte_imaginaria_inicio:

        if valor_real < 0:

            signo_real_temp = -1

        else:

            signo_real_temp = 1

        if valor_imaginario < 0:

            signo_imaginario_temp = -1

        else:

            signo_imaginario_temp = 1


    if valor_real < 0:

        signo_real = -1

    else:

        signo_real = 1

    if valor_imaginario < 0:

        signo_imaginario = -1

    else:

        signo_imaginario = 1

    if signo_real != signo_real_temp:

        if signo_imaginario != signo_imaginario_temp:

            print(str(valor_parte_imaginaria) + ", ", end="")

    signo_real_temp = signo_real
    signo_imaginario_temp = signo_imaginario

    if valor_real <= 0.5:

        if valor_real >= -0.5:

            if valor_imaginario <= 0.5:

                if valor_imaginario >= -0.5:

                    valor_parte_imaginaria += 0.001

                else:

                    valor_parte_imaginaria += 0.1

            else:

                valor_parte_imaginaria += 0.1

        else:

            valor_parte_imaginaria += 0.1

    else:

        valor_parte_imaginaria += 0.1
      
