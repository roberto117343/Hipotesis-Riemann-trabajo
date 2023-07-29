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

def funcion_gamma(x):

    resultado = 1

    for n in range(1, 30001):

        resultado *= pow((1.0 + (1.0/n)), x)/(1.0 + (x/n))

    resultado *= (1.0/x)

    return resultado


valores_x = []
valores_y = []

x = -5.00001

while x < 5.0:

    resultado = funcion_gamma(x)

    if resultado < 6.0:

        if resultado > -6.0:

            valores_x.append(x)
            valores_y.append(resultado)

    x += 0.00002

plt.scatter(valores_x, valores_y, s=1)

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')

plt.xlim(-5.1, 5)
plt.ylim(-6.0, 6)
plt.show()
