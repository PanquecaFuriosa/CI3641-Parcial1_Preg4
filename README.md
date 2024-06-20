## Quaternions
Library that implements the Quaternions type and some arithmetic operators on them.

The quaternions are of the form a+bi+cj+dk and their operations are:

  - Sum:<br>
  ```C1(+)C2: (a1+b1i+c1j+d1k)+(a2+b2i+c2j+d2k) = (a1+a2)+(b1+b2)i+(c1+c2)j+(d1+d2 )k```<br>

  - Product:<br>
  ```C1(*)C2: (a1 + b1i + c1j + d1k) ∗ (a2 + b2i + c2j + d2k) = a1a2 − b1b2 − c1c2 − d1d2 + (a1b2 + b1a2 + c1d2 − d1c2)i + (a1c2 − b1d2 + c1a2 + d1b2)j + (a1d2 + b1c2 − c1b2 + d1a2)k```<br>
  
  - Conjugate:<br>
  ```(∼)C1: ∼(a + bi + cj + dk) = a − bi − cj − dk```<br>
  
  - Mean or absolute value:<br>
  ```(+)C1: &(a + bi + cj + dk) = sqrt(a^{2} + b^{2} + c^{2} d^{2})```<br>

Quaternion addition and product operations can also be performed with integers or floats.<br>
  - Add:<br>
  ```x(+)C1: (a1 + x) + bi + cj + dk```<br>
  
  - Product:<br>
  ```x(*)C1: (a1 * x) + bi + cj + dk```<br>

## Example of use:
from Quaternions import Quaternions
Cuaterniones(1, 2, 3, 4)

## Requirements:
- Python
