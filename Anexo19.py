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


def R(valor):

    resultado = 0.0

    for n in range(1, 500):

        resultado += (funcion_mobius(n)/n) * li(pow(valor, 1.0/n))

    return resultado


valores_i = []
valores_pi = []
valores_teorema = []
valores_li = []
valores_R = []

for i in range(2, 1001):

    valores_i.append(i)
    valores_pi.append(pi(i))
    valores_teorema.append(teorema(i))
    valores_li.append(li(i) - li(2))
    valores_R.append(R(i))

plt.scatter(valores_i, valores_pi, s=1)
plt.scatter(valores_i, valores_teorema, s=1)
plt.scatter(valores_i, valores_li, s=1)
plt.scatter(valores_i, valores_R, s=1)

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')
plt.show()
