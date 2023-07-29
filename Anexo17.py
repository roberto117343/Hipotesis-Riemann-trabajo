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

import math as ma


def li(x):

    x = ma.log(x)

    valor = 0.577215664 + ma.log(x)

    sumatorio = 0.0

    for n in range(1, 106):

        sumatorio += pow(x, n) / (n*ma.factorial(n))

    valor += sumatorio
    return valor


x = input("Introduce valor de x: ")
print(li(float(x)) - li(2))
