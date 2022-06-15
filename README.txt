Librería que implementa el tipo Cuaterniones y algunos operadores aritméticos sobre ellos.

Los cuaterniones son de la forma a+bi+cj+dk y las operaciones de los mismos son:
-Suma C1(+)C2: (a1+b1i+c1j+d1k)+(a2+b2i+c2j+d2k) = (a1+a2)+(b1+b2)i+(c1+c2)j+(d1+d2)k
-Producto C1(*)C2: (a1 + b1i + c1j + d1k) ∗ (a2 + b2i + c2j + d2k) = a1a2 − b1b2 − c1c2 − d1d2 + (a1b2 + b1a2 + c1d2 − d1c2)i + (a1c2 − b1d2 + c1a2 + d1b2)j + (a1d2 + b1c2 − c1b2 + d1a2)k
-conjugada (∼)C1: ∼(a + bi + cj + dk) = a − bi − cj − dk
-Media o valor absoluto (+)C1: &(a + bi + cj + dk) = sqrt(a^{2} + b^{2} + c^{2} d^{2})

También se pueden realizar las operaciones de suma y producto de cuaterniones con enteros o flotantes
-Suma x(+)C1: (a1 + x) + bi + cj + dk
-Prducto x(*)C1: (a1 * x) + bi + cj + dk

Ejemplo de uso:
from Cuaterniones import Cuaterniones
Cuaterniones(1, 2, 3, 4)

Requerimentos:
Python (?)
importar las Librerías:
from __future__ import annotations
import math
