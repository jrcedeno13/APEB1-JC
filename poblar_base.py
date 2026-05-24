from datetime import date
from configuracion import SessionLocal
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

session = SessionLocal()

# Poblar la base de datos con datos de ejemplo
facultad1 = Facultad(
    nombre="Facultad de Ingenierías y Arquitecntura",
    ubicacion="Bloque A",
    decano="Mgtr. Maria Soledad Segarra Morales"
)

facultad2 = Facultad(
    nombre="Facultad de Ciencias Económicas y Empresariales",
    ubicacion="Bloque B",
    decano="Dra. Veronica Alexandra Armijos Buitrón"
)

carrera1 = Carrera(
    nombre="Tecnologías de la información",
    codigo_interno="IS001",
    facultad=facultad1
)

carrera2 = Carrera(
    nombre="Telecomunicaciones",
    codigo_interno="IS002",
    facultad=facultad1
)

carrera3 = Carrera(
    nombre="Administración de Empresas",
    codigo_interno="AE001",
    facultad=facultad2
)

profesor1 = Profesor(
    nombres="María",
    apellidos="Gómez",
    correo_institucional="maria.gomez@universidad.edu",
    especialidad="Bases de Datos",
    carrera=carrera1
)

profesor2 = Profesor(
    nombres="Carlos",
    apellidos="Pérez",
    correo_institucional="carlos.perez@universidad.edu",
    especialidad="Programación",
    carrera=carrera2
)

profesor3 = Profesor(
    nombres="Laura",
    apellidos="Mendoza",
    correo_institucional="laura.mendoza@universidad.edu",
    especialidad="Gestión Empresarial",
    carrera=carrera3
)

recurso1 = RecursoAcademico(
    titulo="Introducción a SQLAlchemy",
    fecha_publicacion=date(2026, 5, 20),
    tipo_recurso="Guía de estudio",
    url="https://ejemplo.com/sqlalchemy",
    profesor=profesor1
)

recurso2 = RecursoAcademico(
    titulo="Video sobre ORM en Python",
    fecha_publicacion=date(2026, 5, 18),
    tipo_recurso="Video",
    url="https://ejemplo.com/orm-video",
    profesor=profesor2
)

recurso3 = RecursoAcademico(
    titulo="Manual de Administración",
    fecha_publicacion=date(2026, 5, 15),
    tipo_recurso="Libro",
    url="https://ejemplo.com/manual-admin",
    profesor=profesor3
)

session.add_all([
    facultad1, facultad2,
    carrera1, carrera2, carrera3,
    profesor1, profesor2, profesor3,
    recurso1, recurso2, recurso3
])

# Guardar los cambios en la base de datos
session.commit()

# Cerrar sesión
session.close()