# Trabajo Práctico N.º 2 — Regex y Secuencias Basadas en Arrays

**Cátedra:** Programación III  
**Carrera:** Licenciatura en Sistemas — Facultad de Ciencias de la Administración, UNER  
**Año:** 2026 — 1er Cuatrimestre  
**Fecha de entrega:** Lunes 11 de Mayo de 2026


## Integrantes

| Apellido y nombre | Ejercicios a cargo |
|---|---|
| Ragone, Alejo | Ej. 1 y 2 (a, b) |
| Sosa, Martin | Ej. 2 (c, d, e, f) |
| Musuliotis, Juan | Ej. 3 y 4 |
| Gonzales, M. Paz | Ej. 5 y 6 (parcial) |
| Medrano, Augusto | Ej. 6 (continuación) y 7 |

---

## Estructura del proyecto

```
PROGRAMACION-3-TP2/
├── README.md
├── poetry.lock
├── pyproject.toml
├── .gitignore
├── ejercicio 2/
│   ├── f1_results.csv
│   ├── procesador_csv.py
│   └── resultado.py
├── ejercicio 3-4/
│   ├── array_stack_ext_abstract.py
│   └── array_stack_ext.py
├── ejercicio5/
│   └── array_stack_ext_client.py
├── ejercicio6/
│   ├── array_queue_ext_abstract.py
│   └── array_queue_ext.py
└── ejercicio7/
    └── array_queue_ext_client.py
```

---

## Configuración del ambiente

### Requisitos previos

- Python 3.12 o superior
- [Poetry](https://python-poetry.org/) o [UV](https://docs.astral.sh/uv/)

### Instalación con Poetry

```bash
# Crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate       # Linux / macOS
.venv\Scripts\activate          # Windows

# Inicializar el proyecto
poetry init

# Instalar la dependencia principal
poetry add python-ed-fcad-uner
```

### Instalación con UV

```bash
# Inicializar el proyecto
uv init

# Instalar la dependencia principal
uv add python-ed-fcad-uner
```

La biblioteca `python-ed-fcad-uner` está disponible en PyPI:  
https://pypi.org/project/python-ed-fcad-uner/

---

## Descripción de los ejercicios

### Ejercicio 1 — Configuración del ambiente

Creación del entorno virtual, inicialización del proyecto con Poetry/UV e instalación de la dependencia `python-ed-fcad-uner`.

### Ejercicio 2 — Procesamiento de resultados de Fórmula 1

Procesa el archivo `f1_results.csv` con los resultados de clasificación desde 1950 en adelante:

- Parseo del archivo con una única expresión regular.
- Definición de la clase `Resultado` para almacenar cada fila.
- Visualización de los últimos 20 resultados.
- Cálculo de los 3 pilotos más ganadores de la historia (mayor cantidad de primeras posiciones).
- Cálculo de las 3 escuderías más ganadoras.

**Ejecución:**
```bash
cd "ejercicio 2"
python procesador_csv.py
```

### Ejercicio 3 — Clase `ArrayStackExt`

Extiende `ArrayStack` del paquete `data_structures` e implementa los métodos definidos en `ArrayStackExtAbstract`:

| Método | Descripción |
|---|---|
| `__bool__` | Indica si la pila está vacía |
| `__iter__` | Iterador en orden LIFO |
| `__contains__` | Verifica si un elemento pertenece a la pila |
| `__reversed__` | Iterador en orden inverso |
| `remove_first` | Elimina y retorna el primer elemento |
| `remove_duplicates` | Elimina elementos duplicados |
| `__iadd__` | Concatena otra pila al tope de la actual |

### Ejercicio 4 — Constructor con `elems`

Modifica `ArrayStackExt` para aceptar un parámetro opcional `elems` (lista de Python) que configura los elementos iniciales de la pila al instanciarla.

### Ejercicio 5 — Cliente de `ArrayStackExt`

Módulo `array_stack_ext_client.py` que pone a prueba todos los métodos de `ArrayStackExt` sin uso de entrada por consola.

**Ejecución:**
```bash
python array_stack_ext_client.py
```

### Ejercicio 6 — Clase `ArrayQueueExt`

Extiende `ArrayQueue` del paquete `data_structures` e implementa los métodos definidos en `ArrayQueueExtAbstract`:

| Método | Descripción |
|---|---|
| `__bool__` | Indica si la cola está vacía |
| `__iter__` | Iterador en orden FIFO |
| `__contains__` | Verifica si un elemento pertenece a la cola |
| `reverse_upto(k)` | Invierte los primeros `k` elementos de la cola |
| `intercalar(queue)` | Intercala los elementos de otra cola con la actual |

**Ejemplo de `reverse_upto`:** con `k=4` y cola `[10, 20, 30, 40, 50, 60]`, el resultado es `[40, 30, 20, 10, 50, 60]`.

### Ejercicio 7 — Cliente de `ArrayQueueExt`

Módulo `array_queue_ext_client.py` que pone a prueba todos los métodos de `ArrayQueueExt` sin uso de entrada por consola.

**Ejecución:**
```bash
python array_queue_ext_client.py
```

---

## Dependencias

| Paquete | Versión | Fuente |
|---|---|---|
| `python-ed-fcad-uner` | última estable | [PyPI](https://pypi.org/project/python-ed-fcad-uner/) |

---

## Notas

- Todas las clases de estructuras de datos se importan desde el módulo `data_structures` provisto por la cátedra, salvo indicación contraria.
- Los módulos cliente no realizan ingreso de datos por consola.
- Las soluciones son de autoría propia del grupo.
