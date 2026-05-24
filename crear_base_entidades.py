from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from configuracion import Base, engine

# Definición de las entidades:
# Facultad, Carrera, Profesor, RecursoAcademico
class Facultad(Base):
    __tablename__ = "facultades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(100), nullable=False)
    decano = Column(String(100), nullable=False)

    carreras = relationship("Carrera", back_populates="facultad")

    def __repr__(self):
        return f"Facultad(id={self.id}, nombre='{self.nombre}')"

class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo_interno = Column(String(20), nullable=False, unique=True)
    facultad_id = Column(Integer, ForeignKey("facultades.id"), nullable=False)

    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __repr__(self):
        return f"Carrera(id={self.id}, nombre='{self.nombre}')"

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo_institucional = Column(String(120), nullable=False, unique=True)
    especialidad = Column(String(100), nullable=False)
    carrera_id = Column(Integer, ForeignKey("carreras.id"), nullable=False)

    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __repr__(self):
        return f"Profesor(id={self.id}, nombres='{self.nombres}', apellidos='{self.apellidos}')"

class RecursoAcademico(Base):
    __tablename__ = "recursos_academicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo_recurso = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=False)

    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return f"RecursoAcademico(id={self.id}, titulo='{self.titulo}')"

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)