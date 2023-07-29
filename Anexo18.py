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

import math as ma


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

    visitado = set()
    dup = {x for x in valores_factores_primos if x in visitado or (visitado.add(x) or False)}

    if valor == 1:

        return 1

    elif len(dup) == 0:

        if len(valores_factores_primos) % 2.0 == 0:

            return 1

        else:

            return -1

    else:

        return 0


def li(x):

    x = ma.log(x)

    valor = 0.577215664 + ma.log(x)

    sumatorio = 0.0

    for n in range(1, 106):

        sumatorio += pow(x, n) / (n*ma.factorial(n))

    valor += sumatorio
    return valor


def R(valor):

    resultado = 0.0

    for n in range(1, 500):

        resultado += (funcion_mobius(n)/n) * li(pow(valor, 1.0/n))

    return resultado

x = input("Introduce valor de x: ")
print(R(float(x)))
