# Taller: Pruebas E2E — Del navegador al sistema completo

## 🎯 Objetivo

Comprender qué son las pruebas de extremo a extremo (End-to-End), cuándo son necesarias, cómo se implementan con Playwright en Python, y cuáles son sus principales limitaciones y antipatrones. Como complemento, se introduce Selenium para comprender la evolución histórica de las herramientas de automatización web.

---

## 📦 Estructura del proyecto

- `src/`: Aplicación Flask (gestor de tareas) — el sistema bajo prueba.
  - `app.py`: Rutas web de la aplicación.
  - `models.py`: Modelo `Task` con persistencia en JSON.
  - `templates/`: Plantillas HTML con `data-testid` para locators.
- `tests/`: Pruebas E2E.
  - `conftest.py`: Fixtures que levantan el servidor y el navegador.
  - `test_tareas_e2e.py`: Pruebas iniciales (débiles).
- `notebooks/`: Cuadernillos educativos (capítulos del taller).
- `data/`: Almacenamiento JSON de tareas.

---

## 🧪 Parte 1 — Instalación y ejecución inicial

1. Instala las dependencias:

```bash
pip install -r requirements.txt
playwright install chromium
```

2. Levanta la aplicación manualmente para explorarla:

```bash
cd src
python app.py
```

Visita `http://localhost:5000` en tu navegador. Interactúa con la aplicación: crea tareas, complétalas, elimínalas.

3. Ejecuta las pruebas E2E iniciales:

```bash
pytest tests/ -v
```

4. Observa que todas pasan. ¿Están verificando algo útil?

---

## 🔍 Parte 2 — Análisis crítico de las pruebas

Responde en tu informe:

- ¿Las pruebas actuales verifican que las tareas se crean correctamente?
- ¿Qué acciones del usuario no están siendo validadas?
- ¿Qué fallos críticos de la UI podrían pasar desapercibidos?

---

## ⚠️ Parte 3 — El lado oscuro de las pruebas E2E

1. Abre `src/app.py` y modifica la ruta `create_task` para que no guarde la tarea (simplemente devuelve redirect sin llamar a `repo.add()`).
2. Ejecuta de nuevo las pruebas:

```bash
pytest tests/test_tareas_e2e.py -v
```

3. Analiza el resultado.

Responde:
- ¿Los tests detectaron el error?
- ¿Por qué siguen pasando?
- ¿Qué debilidad fundamental tienen estas pruebas E2E?

---

## 🔧 Parte 4 — Playwright: locators y aserciones

Usando el notebook `notebooks/02_playwright_basico.ipynb`, escribe pruebas que:

- Verifiquen que al crear una tarea, su título aparece en la lista.
- Verifiquen que al completar una tarea, aparece el badge "✓ Completada".
- Verifiquen que al eliminar una tarea, desaparece de la lista.

Escribe estas pruebas en `tests/test_tareas_e2e.py` bajo una clase `TestCrearTareaFuerte`.

---

## 🔧 Parte 5 — Page Object Model

Usando el notebook `notebooks/03_escenarios_usuario.ipynb`:

1. Implementa la clase `TaskPage` como Page Object.
2. Reescribe las pruebas de la Parte 4 usando `TaskPage`.
3. Agrega un flujo completo: crear tarea → completarla → verificar estado → eliminarla → verificar que no existe.

---

## 🔧 Parte 6 — Escenarios de error y casos extremos

Amplía las pruebas para cubrir:

- Intentar crear una tarea con título vacío (¿qué debería pasar?).
- Crear tareas duplicadas.
- Verificar que la lista muestra "No hay tareas" cuando está vacía.
- Crear múltiples tareas y verificar el orden.

---

## 📊 Parte 7 — Reflexión sobre pruebas E2E en CI/CD

Usando el notebook `notebooks/04_lado_oscuro_e2e.ipynb`, responde:

- ¿Qué son los flaky tests y por qué son especialmente comunes en E2E?
- ¿Cómo garantizarías el aislamiento entre tests en una suite E2E?
- ¿En qué casos usarías E2E en lugar de pruebas de integración?

---

## 📦 Entregable

Sigue las instrucciones detalladas en `ENTREGABLE.md`.

---

## ⚠️ Nota importante

Se evaluará:

- La calidad de los locators (preferencia por `data-testid` sobre XPath frágiles).
- La robustez de las aserciones (verificación de estado, no solo de ausencia de errores).
- La aplicación correcta del Page Object Model.
- El aislamiento entre tests (ningún test debe depender del estado dejado por otro).
- La profundidad del análisis crítico en el informe.
