# Taller: Pruebas Unitarias – Más allá del verde

## 🎯 Objetivo

Este taller tiene como propósito comprender las limitaciones de las pruebas unitarias y desarrollar criterio para diseñar pruebas robustas, más allá de simplemente obtener resultados "en verde".

---

## 🧪 Parte 1 – Exploración inicial

1. Instala las dependencias:

```
pip install -r requirements.txt
```

2. Ejecuta las pruebas existentes:

```
pytest
```

3. Observa el resultado general.

---

## 🔍 Parte 2 – Análisis crítico de las pruebas

Responde en un documento:

* ¿Las pruebas actuales garantizan que el código es correcto?
* ¿Qué aspectos del comportamiento NO están siendo validados?
* ¿Qué tipo de errores podrían pasar desapercibidos?

---

## ⚠️ Parte 3 – El lado oscuro de las pruebas

1. Ubica la función `calcular_promedio` en:

```
src/estadistica.py
```

2. Modifícala para que SIEMPRE retorne un valor constante (por ejemplo `3.14`).

3. Ejecuta nuevamente SOLO los tests relevantes:

```
pytest tests/test_estadistica.py -v
```

4. Analiza el resultado.

Responde:

* ¿Las pruebas detectaron el error?
* ¿Por qué siguen pasando?
* ¿Qué debilidad tienen estos tests?

---

## 🔧 Parte 4 – Mejora de pruebas

Modifica los tests en:

```
tests/test_estadistica.py
```

para que:

* Verifiquen valores correctos (no solo tipos)
* Detecten implementaciones incorrectas
* Incluyan casos adicionales:

  * listas vacías
  * un solo elemento
  * múltiples valores
  * valores negativos

---

## 🧪 Parte 5 – Pruebas con mocks

Utiliza el notebook:

```
notebooks/03_analizador_mejorado.ipynb
```

y crea pruebas para `analizar_texto` que:

* Simulen una respuesta exitosa
* Simulen un fallo seguido de éxito (reintento)
* Simulen fallo total (excepción)

⚠️ No debes realizar llamadas reales a internet.

---

## 📊 Parte 6 – Reflexión sobre cobertura

Utiliza el notebook:

```
notebooks/02_coverage_mejorado.ipynb
```

y responde:

* ¿Qué diferencia hay entre cobertura y calidad de pruebas?
* ¿Por qué 100% coverage no garantiza corrección?

---

## 🧠 Parte 7 – Reflexión final

Responde:

* ¿Qué aprendiste sobre las limitaciones de las pruebas unitarias?
* ¿Qué significa realmente que "los tests pasen"?
* ¿Cómo evitarías falsas confianzas en un proyecto real?

---

## 📦 Entregable

Debes entregar:

1. Tests mejorados en:

   * `tests/test_estadistica.py`
   * `tests/test_analizador.py`

2. Documento (PDF o Markdown) con:

   * Respuestas a las preguntas
   * Explicaciones de decisiones de testing

3. (Opcional) Casos adicionales o mejoras propuestas

---

## ⚠️ Nota importante

Se evaluará no solo que los tests pasen, sino:

* La calidad de las aserciones
* La capacidad de detectar errores reales
