"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""

def Inport(Librarys=[]):
  import os
  for lib in Librarys:
    os.system(f"python -m pip install {lib}")