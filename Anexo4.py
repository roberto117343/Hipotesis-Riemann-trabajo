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

def funcion_compleja(z):

    resultado = z/(pow(z, 2)-3.0)

    return resultado


archivo_guardado = open("archivo de guardado", 'w')

valor_real = -4.0

while valor_real < 4.0:

    valor_imaginario = -4.0

    while valor_imaginario < 4.0:

        z = complex(valor_real, valor_imaginario)

        resultado = funcion_compleja(z)

        if abs(resultado) > -6.0:

            if abs(resultado) < 6.0:

                archivo_guardado.write(str(z.real) + " " + str(z.imag) + " " + str(abs(resultado)) + "\r\n")

        valor_imaginario += 0.02

    valor_real += 0.02

archivo_guardado.close()
