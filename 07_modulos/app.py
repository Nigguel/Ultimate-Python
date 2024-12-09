"""     APP     """

# import usuarios.gestion
# import usuarios.impuestos
from usuarios.impuestos.utilidades import pagar_impuesto

# import usuarios

# print(dir(usuarios))

# print(f"\n{usuarios.__name__}")
# print(f"\n{usuarios.__package__}")
# print(f"\n{usuarios.__path__}")
# print(f"\n{usuarios.__file__}")

# print(f"\n{usuarios.gestion.__name__}")
# print(f"\n{usuarios.impuestos.__package__}")
# print(f"\n{usuarios.gestion.__path__}")
# print(f"\n{usuarios.impuestos.__file__}")

pagar_impuesto()
print(__name__)
