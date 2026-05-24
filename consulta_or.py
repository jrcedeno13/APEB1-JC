from sqlalchemy import or_

from configuracion import SessionLocal
from crear_base_entidades import Facultad, Profesor, RecursoAcademico

# Crear sesión
session = SessionLocal()

# Consulta 1: Profesores de 'Programación' O 'Bases de Datos'
print("\n===== PROFESORES DE 'Programación' O 'Bases de Datos' =====")

profesores = session.query(Profesor).filter(
    or_(
        Profesor.especialidad == "Programación",
        Profesor.especialidad == "Bases de Datos"
    )
).all()

for profesor in profesores:
    print(
        f"{profesor.nombres} {profesor.apellidos} "
        f"- Especialidad: {profesor.especialidad}"
    )

# Consulta 2: Profesores con nombre 'María' O 'Marianela'
print("\n===== PROFESORES CON NOMBRE 'María' O 'Marianela' =====")

profesoras = session.query(Profesor).filter(
    or_(
        Profesor.nombres == "María",
        Profesor.nombres == "Marianela"
    )
).all()

for profesora in profesoras:
    print(
        f"{profesora.nombres} {profesora.apellidos} "
        f"- Especialidad: {profesora.especialidad}"
    )

# Consulta 3: Recursos académicos de tipo 'Video' O 'Libro base, 
# + ordenado ascendentemente por tipo de recurso'
print("\n===== RECURSOS TIPO 'Video' O 'Libro base' =====")

recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo_recurso == "Video",
        RecursoAcademico.tipo_recurso == "Libro base"
    )
).order_by(
    RecursoAcademico.tipo_recurso.asc()
).all()

for recurso in recursos:
    print(
        f"Título: {recurso.titulo} | "
        f"Tipo: {recurso.tipo_recurso}"
    )

# Consulta 4: Facultades ubicadas en 'Bloque A' O 'Bloque C, 
# + ordenado ascendentemente por ubicación'
print("\n===== FACULTADES UBICADAS EN 'Bloque A' O 'Bloque C' =====")

facultades = session.query(Facultad).filter(
    or_(
        Facultad.ubicacion == "Bloque A",
        Facultad.ubicacion == "Bloque C"
    )
).order_by(
    Facultad.ubicacion.asc()
).all()

for facultad in facultades:
    print(
        f"{facultad.nombre} - {facultad.ubicacion}"
    )

# Cerrar sesión
session.close()