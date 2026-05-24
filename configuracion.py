from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la base de datos
DATABASE_URL = "sqlite:///universidades.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=False)

# Crear una clase base para las entidades
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la clase base para las entidades
Base = declarative_base()