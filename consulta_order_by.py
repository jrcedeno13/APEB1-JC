from configuracion import SessionLocal
from crear_base_entidades import Facultad, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()

# CONSULTA ORDER BY - Ordenar facultades por nombre de forma ascendente
print("\n===== FACULTADES ORDENADAS POR NOMBRE (ASCENDENTE) =====")

facultades = session.query(Facultad).order_by(
    Facultad.nombre.asc()
).all()

for facultad in facultades:
    print(facultad)

# Ordenar profesores por apellido de forma ascendente
print("\n===== PROFESORES ORDENADOS POR APELLIDO (ASCENDENTE) =====")

profesores = session.query(Profesor).order_by(
    Profesor.apellidos.asc()
).all()

for profesor in profesores:
    print(profesor)

# Ordenar recursos académicos por fecha de publicación de forma descendente
print("\n===== RECURSOS ORDENADOS POR FECHA DE PUBLICACIÓN (DESCENDENTE) =====")

recursos = session.query(RecursoAcademico).order_by(
    RecursoAcademico.fecha_publicacion.desc()
).all()

for recurso in recursos:
    print(
        f"Título: {recurso.titulo} | "
        f"Fecha: {recurso.fecha_publicacion} | "
        f"Tipo: {recurso.tipo_recurso}"
    )

# Ordenar recursos académicos por título de forma ascendente
print("\n===== RECURSOS ORDENADOS POR TÍTULO (ASCENDENTE) =====")

recursos_titulo = session.query(RecursoAcademico).order_by(
    RecursoAcademico.titulo.asc()
).all()

for recurso in recursos_titulo:
    print(recurso)

# Cerrar sesión
session.close()