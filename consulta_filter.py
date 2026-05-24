from configuracion import SessionLocal
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()


# Busca textos que contengan la palabra “Ingeniería”
print("\n===== CARRERAS QUE CONTIENEN 'Tecnologías' =====")

carreras = session.query(Carrera).filter(
    Carrera.nombre.like("%Tecnologías%")
).all()

for carrera in carreras:
    print(carrera)


# Filtra únicamente profesores con esa especialidad.
print("\n===== PROFESORES ESPECIALISTAS EN 'Bases de Datos' =====")

profesores = session.query(Profesor).filter(
    Profesor.especialidad == "Bases de Datos"
).all()

for profesor in profesores:
    print(profesor)


# Filtra únicamente recursos de tipo "Video".
print("\n===== RECURSOS DE TIPO 'Video' =====")

recursos = session.query(RecursoAcademico).filter(
    RecursoAcademico.tipo_recurso == "Video"
).all()

for recurso in recursos:
    print(recurso)


# Filtra únicamente profesores de facultades que contengan "Ingenierías".
print("\n===== PROFESORES DE FACULTADES CON 'Ingenierías' =====")

profesores_ingenierias = session.query(Profesor).join(Carrera).join(Facultad).filter(
    Facultad.nombre.like("%Ingenierías%")
).all()

for profesor in profesores_ingenierias:
    print(profesor)


# Cerrar sesión
session.close()