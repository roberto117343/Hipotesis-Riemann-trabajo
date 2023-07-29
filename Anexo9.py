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

import cmath


def funcion_gamma(s):

    resultado = 1.0

    for n in range(1, 150000):

        resultado *= pow((1.0 + (1.0/n)), s)/(1.0 + (s/n))

    resultado *= (1.0/s)

    return resultado


def zeta_1(s):

    resultado = 0

    for i in range(1, 1500):

        resultado += 1.0/pow(i, s)

    return resultado


def zeta_2(s):

    resultado = pow(2.0, s) * pow(3.14159, s - 1.0) * cmath.sin((3.14159 * s)/2.0)
    resultado *= funcion_gamma(1.0 - s) * zeta_1(1.0 - s)

    return resultado;


def zeta_3(s):

    valor = 0

    for i in range(1, 150000):

        valor += pow(-1.0, i + 1.0)/pow(i, s)

    return 1.0/(1.0-(pow(2.0, 1.0 - s)))*valor


s = complex(input("Introduce valor de s: "))

if s.real < 0.0:

    print(zeta_2(s))

elif s.real > 1.0:

    print(zeta_1(s))

else:

    if s.real != 1.0:

        if s.real != 0.0:

            print(zeta_3(s))
