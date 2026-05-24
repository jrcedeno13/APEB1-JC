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

facultad3 = Facultad(
    nombre="Facultad de Ciencias de la Salud",
    ubicacion="Bloque C",
    decano="Esp. Med. Patricia Bonilla Sierra"
)

facultad4 = Facultad(
    nombre="Facultad de Ciencias Jurídicas y Políticas",
    ubicacion="Bloque A",
    decano="Dra. Diana Gabriela Moreira Aguirre"
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

carrera4 = Carrera(
    nombre="Medicina",
    codigo_interno="CS001",
    facultad=facultad3
)

carrera5 = Carrera(
    nombre="Enfermería",
    codigo_interno="CS002",
    facultad=facultad3
)

carrera6 = Carrera(
    nombre="Derecho",
    codigo_interno="CJ001",
    facultad=facultad4
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

profesor4 = Profesor(
    nombres="María",
    apellidos="Carrillo",
    correo_institucional="maria.carrillo@universidad.edu",
    especialidad="Química",
    carrera=carrera4
)

profesor5 = Profesor(
    nombres="Pablo",
    apellidos="Bravo",
    correo_institucional="pablo.bravo@universidad.edu",
    especialidad="Biología Básica",
    carrera=carrera5
)

profesor6 = Profesor(
    nombres="Marianela",
    apellidos="Armijos",
    correo_institucional="marianela.armijos@universidad.edu",
    especialidad="Introducción al Derecho ",
    carrera=carrera6
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

recurso4 = RecursoAcademico(
    titulo="Quimica Orgánica para Estudiantes de Medicina",
    fecha_publicacion=date(2026, 5, 20),
    tipo_recurso="Libro base",
    url="https://ejemplo.com/Quimica",
    profesor=profesor4
)

recurso5 = RecursoAcademico(
    titulo="Video sobre Biología Básica",
    fecha_publicacion=date(2020, 3, 10),
    tipo_recurso="Video",
    url="https://ejemplo.com/Biología-básica-video",
    profesor=profesor5
)

recurso6 = RecursoAcademico(
    titulo="Introducción al Derecho",
    fecha_publicacion=date(2026, 5, 15),
    tipo_recurso="Libro base",
    url="https://ejemplo.com/manual-admin",
    profesor=profesor6
)
session.add_all([
    facultad1, facultad2, facultad3, facultad4,
    carrera1, carrera2, carrera3, carrera4, carrera5, carrera6,
    profesor1, profesor2, profesor3, profesor4, profesor5, profesor6,
    recurso1, recurso2, recurso3, recurso4, recurso5, recurso6
])

# Guardar los cambios en la base de datos
session.commit()

# Cerrar sesión
session.close()