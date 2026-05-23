# Entregable del Taller de Pruebas E2E

Debes entregar un archivo ZIP o repositorio con la siguiente estructura:

## 📁 Archivos requeridos

### 1. Tests mejorados

- `tests/test_tareas_e2e.py` con:
  - `TestCrearTareaFuerte`: al menos 3 pruebas con aserciones sobre el estado de la UI.
  - `TestCompletarTareaFuerte`: verifica el badge y el tachado del título.
  - `TestEliminarTareaFuerte`: verifica desaparición de la lista.
  - `TestFlujoCompleto`: flujo crear → completar → eliminar en un solo test.
  - `TestCasosExtremos`: título vacío, duplicados, lista vacía.

- `tests/page_objects.py` con la clase `TaskPage` (Page Object Model).

### 2. Informe (PDF o Markdown)

El informe debe responder:

**Parte 2 — Análisis:**
- ¿Las pruebas iniciales verifican algo útil? ¿Por qué?
- ¿Qué interacciones de usuario no estaban cubiertas?

**Parte 3 — Sabotaje:**
- ¿Las pruebas iniciales detectaron la modificación maliciosa?
- ¿Qué debilidad fundamental expone este experimento?

**Parte 7 — Reflexión E2E:**
- Explica con tus palabras qué es un flaky test y da un ejemplo concreto.
- ¿Cómo garantizarías el aislamiento entre tests E2E?
- ¿Cuándo preferirías una prueba de integración sobre una E2E?
- ¿Cómo aplicarías Playwright o Selenium en un proyecto con microservicios?

## ✅ Criterios de evaluación

| Criterio | Peso |
|----------|------|
| Calidad de los locators (preferencia `data-testid`) | 15% |
| Robustez de aserciones (verifican estado, no solo ausencia de errores) | 25% |
| Implementación del Page Object Model | 20% |
| Aislamiento entre tests (sin contaminación de estado) | 20% |
| Profundidad del análisis crítico en el informe | 20% |

## ⚠️ Restricciones

- Las pruebas deben ejecutarse con `pytest tests/ -v` sin modificaciones al `conftest.py`.
- No se permite usar `time.sleep()` para esperas fijas; usa `wait_for_selector` o `expect()`.
- Cada test debe ser independiente: no asumir estado de tests anteriores.
