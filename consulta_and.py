from sqlalchemy import and_

from configuracion import SessionLocal
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()

# Consulta 1: Profesores llamados 'María' y especialidad 'Química'
print("\n===== PROFESORES LLAMADOS 'María' Y ESPECIALIDAD 'Química' =====")

profesores = session.query(Profesor).filter(
    and_(
        Profesor.nombres == "María",
        Profesor.especialidad == "Química"
    )
).all()

for profesor in profesores:
    print(
        f"{profesor.nombres} {profesor.apellidos} "
        f"- Especialidad: {profesor.especialidad}"
    )

# Consulta 2: Recursos académicos de tipo 'Video' y publicados después de 2025
print("\n===== RECURSOS TIPO 'Video' Y PUBLICADOS DESPUÉS DE 2025 =====")

recursos = session.query(RecursoAcademico).filter(
    and_(
        RecursoAcademico.tipo_recurso == "Video",
        RecursoAcademico.fecha_publicacion >= "2025-01-01"
    )
).all()

for recurso in recursos:
    print(
        f"Título: {recurso.titulo} | "
        f"Fecha: {recurso.fecha_publicacion} | "
        f"Tipo: {recurso.tipo_recurso}"
    )

# Consulta 3: Facultades ubicadas en 'Bloque A' y con 'Ingenierías' en el nombre
print("\n===== FACULTADES EN 'Bloque A' Y CON 'Ingenierías' EN EL NOMBRE =====")

facultades = session.query(Facultad).filter(
    and_(
        Facultad.ubicacion == "Bloque A",
        Facultad.nombre.like("%Ingenierías%")
    )
).all()

for facultad in facultades:
    print(
        f"{facultad.nombre} - {facultad.ubicacion}"
    )

# Consulta 4: Recursos académicos de tipo 'Libro base' y publicados en 2026
print("\n===== RECURSOS TIPO 'Libro base' Y PUBLICADOS EN 2026 =====")

recursos_libros = session.query(RecursoAcademico).filter(
    and_(
        RecursoAcademico.tipo_recurso == "Libro base",
        RecursoAcademico.fecha_publicacion >= "2026-01-01"
    )
).all()

for recurso in recursos_libros:
    print(
        f"{recurso.titulo} | "
        f"Fecha: {recurso.fecha_publicacion}"
    )

# Consulta 5: Profesores de facultades con 'Ciencias' en el nombre 
# junto con su carrera y facultad y 
# presentados en orden ascendente por apellido de profesor
print("\n===== PROFESORES DE FACULTADES CON 'Ciencias' EN EL NOMBRE =====")

profesores_ciencias = session.query(Profesor).join(Carrera).join(Facultad).filter(
    Facultad.nombre.like("%Ciencias%")
).order_by(
    Profesor.apellidos.asc()
).all()

for profesor in profesores_ciencias:
    print(
        f"Profesor: {profesor.apellidos} {profesor.nombres} | "
        f"Carrera: {profesor.carrera.nombre} | "
        f"Facultad: {profesor.carrera.facultad.nombre}"
    )

# Cerrar sesión
session.close()