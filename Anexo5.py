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

def funcion_gamma(x):

    resultado = 1

    for n in range(1, 30001):

        resultado *= pow((1.0 + (1.0/n)), x)/(1.0 + (x/n))

    resultado *= (1.0/x)

    return resultado


x = input("Introduce valor de x: ")
print(funcion_gamma(float(x)))
