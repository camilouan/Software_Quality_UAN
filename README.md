# 🧪 Calidad de Software – UAN

Repositorio oficial del curso **Calidad de Software** de la **Universidad Antonio Nariño**, orientado al diseño, implementación y análisis crítico de pruebas automatizadas en Python.

**Docente:** MSc. Andrés Bermúdez

---

## 🎯 Objetivo general

Desarrollar competencias para:

- Diseñar pruebas unitarias, de integración y end-to-end efectivas.
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
│   │   └── tests_hidden/
│   │       ├── test_ordenar_real.py
│   │       └── test_promedio_real.py
│   │
│   ├── integration_testing/
│   │   └── coming_soon.txt
│   │
│   └── e2e_testing/
│       └── coming_soon.txt
│
├── notebooks/
├── src/
├── tests/
└── tests_hidden/
```

Cada módulo del curso es autocontenido e incluye instrucciones detalladas en su respectiva carpeta.

---

## 🧠 Enfoque pedagógico

El propósito de este repositorio no se limita a enseñar el uso de herramientas de prueba. Busca, sobre todo, desarrollar criterio ingenieril frente a la calidad del software de pruebas. A lo largo de los talleres, el estudiante se enfrenta a situaciones reales donde:

- Una suite de pruebas puede ejecutarse sin errores y, aun así, ser insuficiente o mal diseñada.
- Alcanzar el 100 % de cobertura de código no implica que el software sea correcto ni que las pruebas tengan la calidad necesaria.
- Es posible escribir código que "burla" pruebas poco rigurosas, evidenciando la necesidad de diseñar aserciones sólidas y casos representativos.
- La reflexión crítica y el análisis de las debilidades de las pruebas son habilidades tan fundamentales como la propia implementación de las mismas.

En este curso las pruebas no son solo un producto que debe pasar, sino un objeto de estudio que debe ser cuestionado, mejorado y evaluado con rigor.

---

## 👣 Metodología de los talleres

Cada taller está compuesto por:

1. Código base que debe ser probado.
2. Tests iniciales (a menudo incompletos o deliberadamente débiles).
3. Ejercicios prácticos guiados y abiertos.
4. Preguntas de reflexión sobre la calidad de las pruebas.

Los estudiantes deben:

- Completar y mejorar las pruebas.
- Emplear correctamente mocks, stubs y fakes.
- Identificar debilidades en las suites existentes.
- Proponer y justificar mejoras.
- Entregar un documento de reflexión.

---

## ⚙️ Instalación y uso

```bash
git clone <url-del-repo>
cd software-quality-uan

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

pytest

coverage run -m pytest
coverage report -m
coverage html
```

---

## 📦 Entregables y evaluación

Cada módulo requiere:

- Código de pruebas implementadas.
- Uso adecuado de dobles de prueba.
- Documento de reflexión en Markdown o PDF.

La evaluación se basa en:

- Calidad de las aserciones.
- Uso correcto de mocks.
- Profundidad del análisis crítico.
- Capacidad de detectar debilidades en las pruebas.

---

## 🛠️ Tecnologías utilizadas

- Python ≥ 3.8
- pytest
- pytest-mock
- coverage
- Hypothesis (opcional)

---

## 👨‍🏫 Para el docente

Este repositorio está diseñado para:

- Clases prácticas presenciales o virtuales.
- Evaluación automatizada con pytest.
- Discusión crítica sobre calidad de software y pruebas.

---

## 📌 Autor

**MSc. Andrés Bermúdez**  
Curso de Calidad de Software  
Universidad Antonio Nariño

---

*“Pasar todos los tests no significa que el software sea correcto; significa que pasa las pruebas que escribiste.”*