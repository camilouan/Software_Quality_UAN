# 🧪 Calidad de Software – UAN

Repositorio oficial del curso **Calidad de Software** de la **Universidad Antonio Nariño**, orientado al diseño, implementación y análisis crítico de pruebas automatizadas en Python.

**Docente:** MSc. Andrés Bermúdez

---

## 🎯 Objetivo general

Desarrollar competencias para:

- Diseñar pruebas unitarias, de integración y end‑to‑end efectivas.
- Utilizar dobles de prueba (mocks, stubs, fakes) con criterio.
- Interpretar y cuestionar métricas de cobertura de código.
- Reconocer las limitaciones de las pruebas automatizadas.
- Evaluar la calidad de las pruebas como parte de la calidad del software.

---

## 📁 Estructura del repositorio

```
software-quality-uan/
│
├── README.md
├── requirements.txt
│
├── talleres/
│   ├── unit_testing/
│   │   ├── README.md
│   │   ├── ENTREGABLE.md
│   │   ├── requirements.txt
│   │   │
│   │   ├── data/
│   │   │   └── sample.txt
│   │   │
│   │   ├── notebooks/
│   │   │   ├── 01_mocks.ipynb
│   │   │   ├── 02_coverage.ipynb
│   │   │   ├── 03_analizador.ipynb
│   │   │   └── 04_lado_oscuro.ipynb
│   │   │
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── analizador.py
│   │   │   ├── estadistica.py
│   │   │   └── ordenador.py
│   │   │
│   │   ├── tests/
│   │   │   ├── test_analizador.py
│   │   │   ├── test_estadistica.py
│   │   │   └── test_ordenar.py
│   │   │
│   │   └── tests_hidden/          # 🔒 Solo para el docente
│   │       ├── test_ordenar_real.py
│   │       └── test_promedio_real.py
│   │
│   ├── integration_testing/
│   │   └── coming_soon.txt
│   │
│   └── e2e_testing/
│       └── coming_soon.txt
│
├── notebooks/                     # (Opcional – material global del curso)
├── src/                           # (Opcional – código compartido entre módulos)
├── tests/                         # (Opcional – pruebas compartidas)
└── tests_hidden/                  # (Opcional – pruebas ocultas globales-solo para el docente)
```

Cada módulo del curso es autocontenido e incluye instrucciones detalladas en su respectiva carpeta.

---

## 🧠 Enfoque pedagógico

Este repositorio **no solo enseña herramientas**, sino que desarrolla criterio ingenieril:

- ✅ Los tests pueden pasar y aun así ser deficientes.
- ✅ 100 % de cobertura no implica corrección.
- ✅ Es posible “engañar” a una suite de pruebas si no es rigurosa.
- ✅ La reflexión y el análisis crítico son tan importantes como el código.

---

## 👣 Metodología de los talleres

Cada taller está compuesto por:

1. **Código base** que debe ser probado.
2. **Tests iniciales** (a menudo incompletos o deliberadamente débiles).
3. **Ejercicios prácticos** guiados y abiertos.
4. **Preguntas de reflexión** que invitan a analizar la calidad de las pruebas.

Los estudiantes deben:

- Completar y mejorar las pruebas.
- Emplear correctamente mocks, stubs y fakes.
- Identificar debilidades en las suites existentes.
- Proponer y justificar mejoras.
- Entregar un breve documento de reflexión.

---

## ⚙️ Instalación y uso

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd software-quality-uan

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar las pruebas
pytest

# Medir cobertura
coverage run -m pytest
coverage report -m
coverage html
```

---

## 📦 Entregables y evaluación

Cada módulo requiere:

- Código de las pruebas implementadas.
- Uso adecuado de dobles de prueba.
- Documento de reflexión (Markdown o PDF) que responda a las preguntas planteadas.

La calificación no depende solo de que los tests pasen, sino de:

- La calidad y pertinencia de las aserciones.
- La correcta utilización de mocks.
- La profundidad del análisis crítico.
- La capacidad de detectar errores reales e identificar pruebas débiles.

---

## 🛠️ Tecnologías utilizadas

- Python ≥ 3.8
- [pytest](https://docs.pytest.org/)
- [pytest-mock](https://pytest-mock.readthedocs.io/)
- [coverage](https://coverage.readthedocs.io/)
- [Hypothesis](https://hypothesis.readthedocs.io/) (opcional, para property‑based testing)

---

## 👨‍🏫 Para el docente

Este repositorio está preparado para:

- Clases prácticas presenciales o virtuales.
- Evaluación automatizada con `pytest` (incluye tests ocultos en `tests_hidden/`).
- Discusión en clase sobre calidad de software y de pruebas.

---

## 📌 Autor

**MSc. Andrés Bermúdez**  
Curso de Calidad de Software  
Universidad Antonio Nariño

---

*“Pasar todos los tests no significa que el software sea correcto; significa que pasa las pruebas que escribiste.”*
