# Notas del Proyecto SQLAlchemy

## Activación del entorno virtual

### CMD
```cmd
venv\Scripts\activate
```

### PowerShell
```powershell
.\venv\Scripts\Activate.ps1
```

-------------

## Error de PowerShell

Error:

```powershell
No se puede cargar Activate.ps1...
```

Solución:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

-------------

## Crear entorno virtual

```Ejecutar
python -m venv venv
```

-------------

## Instalar SQLAlchemy

```Ejecutar
python -m pip install sqlalchemy
```

-------------

## Ejecutar archivos

### Crear tablas

```bash
python crear_base_entidades.py
```

### Poblar base

```Ejecutar
python poblar_base.py
```

-------------

## Reiniciar base de datos

1. Eliminar `universidad.db`
2. Ejecutar:

```Ejecutar
python crear_base_entidades.py
python poblar_base.py
```

-------------

## CONSULTAS

## Consultar todo el contenido de la base de datos
python consulta_all.py

## Consultas con filtros, +join
python consulta_filter.py

## Consultas con ordenadas
python consulta_order_by.py

## Consultas con or (que cumplan una condicion u otra), +order
python consulta_or.py

## 