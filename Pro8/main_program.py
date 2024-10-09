# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:17:58 2024

@author: hpsin
"""

from bcae_package.staff_module import staff_function

from bcae_package.student_module import student_function

staff_result = staff_function("Jhon")
student_result = student_function("Alice")

print(staff_result)
print(student_result)