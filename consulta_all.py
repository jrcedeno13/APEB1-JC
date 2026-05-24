from configuracion import SessionLocal
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()

# CONSULTA ALL

#Consulta para obtener todas las facultades
print("\n===== FACULTADES =====")
facultades = session.query(Facultad).all()

for facultad in facultades:
    print(facultad)

#Consulta para obtener todas las carreras
print("\n===== CARRERAS =====")
carreras = session.query(Carrera).all()

for carrera in carreras:
    print(carrera)

#Consulta para obtener todos los profesores
print("\n===== PROFESORES =====")
profesores = session.query(Profesor).all()

for profesor in profesores:
    print(profesor)

#Consulta para obtener todos los recursos académicos
print("\n===== RECURSOS ACADÉMICOS =====")
recursos = session.query(RecursoAcademico).all()

for recurso in recursos:
    print(recurso)

# Cerrar sesión
session.close()