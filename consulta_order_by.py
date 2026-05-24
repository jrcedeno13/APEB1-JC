from configuracion import SessionLocal
from crear_base_entidades import Facultad, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()


# Consulta con ordenamiento ascendente por nombre de facultad, apellido de profesor y fecha de publicación del recurso.
print("\n===== FACULTADES ORDENADAS POR NOMBRE (ASCENDENTE) =====")

facultades = session.query(Facultad).order_by(
    Facultad.nombre.asc()
).all()

for facultad in facultades:
    print(facultad)


# Consulta con ordenamiento ascendente por apellido del profesor.
print("\n===== PROFESORES ORDENADOS POR APELLIDO (ASCENDENTE) =====")

profesores = session.query(Profesor).order_by(
    Profesor.apellidos.asc()
).all()

for profesor in profesores:
    print(profesor)


# Consulta con ordenamiento descendente por fecha de publicación del recurso.
print("\n===== RECURSOS ORDENADOS POR FECHA DE PUBLICACIÓN (DESCENDENTE) =====")

recursos = session.query(RecursoAcademico).order_by(
    RecursoAcademico.fecha_publicacion.desc()
).all()

for recurso in recursos:
    print(recurso)

# Consulta con ordenamiento ascendente por apellido del profesor, pero solo para aquellos profesores que sean especialistas en "Programación".
print("\n===== PROFESORES ESPECIALISTAS EN 'Programación' ORDENADOS POR APELLIDO (ASCENDENTE) =====")
session.query(Profesor).filter(
    Profesor.especialidad == "Programación"
).order_by(
    Profesor.apellidos.asc()
).all()

# Cerrar sesión
session.close()