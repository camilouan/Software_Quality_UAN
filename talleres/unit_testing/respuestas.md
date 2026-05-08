Respuestas – Taller de Pruebas Unitarias

Curso: Calidad de Software – UAN
Fecha: Mayo 2026
Estudiante: CAMILO ANDRÉS PARRA CUENCA

PARTE 2 – Análisis crítico de las pruebas
¿Las pruebas actuales garantizan que el código sea correcto?

La verdad, no del todo.

Cuando ejecuté los tests por primera vez pensé que todo estaba bien porque todos pasaban sin errores. Pero después, revisando mejor el código y las pruebas, me di cuenta de que varias validaciones eran demasiado básicas y realmente no comprobaban si el comportamiento era correcto.

Por ejemplo, había pruebas como esta:

def test_tipo_retorno_float():
    res = calcular_promedio([1, 2, 3])
    assert isinstance(res, float)

Ese test únicamente revisa que el resultado sea un float, pero nunca pregunta si el promedio calculado realmente corresponde al valor esperado.

Entonces casos como estos seguirían pasando:

return 2.0
return 3.14
return 999.0

Mientras siga siendo un número decimal, el test pasa igual.

Ahí fue donde empecé a entender mejor el objetivo del taller. Un test no sirve solamente porque salga en verde. Lo importante es que sea capaz de detectar errores reales cuando el código está mal.

También me di cuenta de que varios tests parecían hechos solo para comprobar que el programa no se dañara, pero no validaban la lógica interna de las funciones.

¿Qué cosas no estaban siendo validadas?

Había varios comportamientos importantes que prácticamente no se estaban probando.

En calcular_promedio()

No se validaban cosas como:

números negativos
números decimales
precisión del resultado
listas con un solo elemento
cálculos reales del promedio

Por ejemplo:

calcular_promedio([2, 4, 6])

debería devolver 4.0, pero los tests originales nunca comprobaban directamente si ese valor era correcto.

En ordenar()

Aquí encontré algo curioso. Muchas pruebas usaban listas que ya estaban ordenadas:

[1, 2, 3]

Entonces incluso una función incorrecta podía pasar perfectamente:

def ordenar(lista):
    return lista

Eso fue algo que me llamó bastante la atención porque técnicamente los tests seguían pasando, pero la función realmente no estaba haciendo el trabajo de ordenar.

Tampoco se estaban probando:

números negativos
elementos repetidos
listas realmente desordenadas
números decimales
En analizar_texto()

Esta parte me pareció más delicada porque la función hacía llamadas reales a internet usando requests.get().

Los tests originales prácticamente no validaban escenarios importantes como:

timeout
errores de conexión
respuestas vacías
reintentos
errores HTTP

Entonces si el servidor fallaba o internet tenía problemas, las pruebas realmente no ayudaban mucho a detectar esos casos.

¿Qué errores podrían pasar desapercibidos?

Después de revisar mejor las pruebas originales, me di cuenta de que varios bugs importantes podían pasar sin problema.

Por ejemplo:

Una función que siempre devuelve el mismo valor
def calcular_promedio(numeros):
    if not numeros:
        return None
    return 3.14

Los tests seguían pasando porque solamente verificaban el tipo de dato.

Una función que nunca ordena
def ordenar(lista):
    return lista

Como algunas listas ya venían ordenadas, el error ni siquiera se notaba.

Problemas con decimales
def calcular_promedio(numeros):
    return int(sum(numeros) / len(numeros))

Aquí se pierden decimales por convertir el resultado a entero, pero las pruebas originales tampoco detectaban eso.

Problemas con listas vacías
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

Si la lista está vacía, la función falla.

Y aunque parezca un caso sencillo, si nadie lo prueba, el error puede terminar llegando hasta producción.

PARTE 3 – El lado oscuro de las pruebas
Experimento realizado

La parte que más me hizo cambiar la forma de pensar sobre los tests fue cuando modifiqué la función intencionalmente para dañarla.

Cambié calcular_promedio() para que siempre devolviera 3.14.

def calcular_promedio(numeros):
    if not numeros:
        return None
    return 3.14

Sinceramente pensé que los tests iban a fallar de inmediato, pero pasó algo totalmente distinto.

Resultado con los tests originales
3 passed

Todos seguían pasando.

Y ahí fue donde realmente entendí el problema.

El código estaba mal, los resultados eran incorrectos y aun así las pruebas seguían diciendo que todo funcionaba correctamente.

Eso demuestra que un test puede verse “bien” visualmente y aun así no servir realmente para detectar errores importantes.

Resultado con los tests mejorados

Después de agregar pruebas validando resultados reales, los errores aparecieron enseguida:

FAILED - assert 3.14 == 4.0
FAILED - assert 3.14 == 2.0
FAILED - assert 3.14 == 5.0

Ahí sí se notó la diferencia entre una prueba superficial y una prueba útil.

Los nuevos tests sí detectaban que el comportamiento era incorrecto.

¿Por qué los tests originales seguían pasando?

Porque estaban validando cosas demasiado simples.

Por ejemplo:

assert isinstance(res, float)

Ese test solamente pregunta:

¿es un float?
sí o no

Pero nunca valida si el valor calculado corresponde al promedio correcto.

Entonces con 3.14:

¿es float? → sí
¿el resultado está bien? → el test nunca lo revisa

Ahí entendí que validar únicamente tipos de datos es demasiado débil para una prueba unitaria seria.

Debilidades principales de las pruebas originales
Validaban tipos y no resultados reales
assert isinstance(res, float)

Eso puede pasar incluso con resultados incorrectos.

Mucho mejor sería:

assert res == 2.0

porque ya valida lógica real.

No existían edge cases

No se estaban probando escenarios importantes como:

listas vacías
un solo elemento
negativos
valores repetidos
decimales

Y normalmente es justamente ahí donde suelen aparecer errores.

Algunas pruebas prácticamente no hacían nada
assert True

Cuando vi eso entendí que algunas pruebas estaban más como placeholder que como validaciones reales.

PARTE 4 – Mejoras realizadas

Después de encontrar todas esas debilidades, empecé a crear pruebas más completas y más cercanas a escenarios reales.

En test_estadistica.py agregué pruebas para:

negativos
decimales
un solo elemento
múltiples elementos
listas vacías

Ejemplo:

assert calcular_promedio([2, 4, 6]) == 4.0

También usé pytest.approx() para comparar resultados decimales sin problemas de precisión.

En test_ordenador.py agregué validaciones para:

listas realmente desordenadas
negativos
repetidos
flotantes
orden ascendente real
conservación de elementos

Ejemplo:

assert ordenar([3, 1, 2]) == [1, 2, 3]

Eso ya obliga a la función a ordenar de verdad y no simplemente devolver la lista original.

PARTE 5 – Uso de mocks

Antes de hacer este taller realmente no entendía muy bien por qué se usaban mocks en testing.

Después de implementarlos en analizar_texto(), la idea quedó mucho más clara.

La función hacía llamadas reales usando:

requests.get()

El problema es que depender de internet hace que las pruebas puedan fallar por razones externas:

mala conexión
caída del servidor
lentitud de red
timeout

Y ahí el problema ya no sería necesariamente del código.

¿Qué hice con los mocks?

Usé @patch para simular respuestas falsas sin necesidad de conectarme realmente a internet.

@patch('src.analizador.requests.get')

Con eso pude probar:

respuestas exitosas
timeout
errores de conexión
reintentos
respuestas vacías
Lo que más me gustó de esta parte

Sinceramente esta fue una de las partes más interesantes del taller.

Con los mocks pude recrear situaciones difíciles de probar normalmente.

Por ejemplo:

mock_get.side_effect = Timeout("Timeout")

Eso simula una falla de conexión por tiempo de espera.

También pude verificar si la función realmente hacía reintentos cuando ocurría un error.

PARTE 6 – Cobertura vs calidad

Antes de este taller yo pensaba que tener muchos tests o un coverage alto automáticamente significaba buena calidad.

Después de hacer el experimento del 3.14, entendí que no necesariamente es así.

Un proyecto puede tener:

muchos tests
coverage alto
todo en verde

y aun así seguir teniendo errores importantes.

Diferencia entre coverage y calidad

La cobertura simplemente muestra qué partes del código fueron ejecutadas.

Pero eso no significa automáticamente que las pruebas sean buenas.

Por ejemplo:

def test():
    calcular_promedio([1,2,3])
    assert True

Aquí el código sí se ejecuta completamente.

El coverage subiría, pero la calidad de la prueba sigue siendo mala porque realmente no está validando nada importante.

Entonces, ¿100% coverage garantiza que el código esté bien?

No.

Y el experimento del 3.14 lo dejó bastante claro.

La función estaba mal y aun así los tests originales seguían pasando.

Entonces sí, el coverage ayuda bastante para encontrar partes no probadas, pero no garantiza que las pruebas detecten errores reales.

Lo importante no es solo ejecutar código

Lo realmente importante es validar comportamientos reales.

Por eso ahora entiendo mejor que una buena prueba debería:

validar lógica
probar edge cases
detectar errores reales
comprobar resultados correctos

y no simplemente ejecutar líneas de código.

PARTE 7 – Reflexión final
¿Qué aprendí sobre las pruebas unitarias?

Aprendí que las pruebas unitarias ayudan muchísimo, pero tampoco solucionan todo por sí solas.

Sirven para detectar errores rápidos y validar funciones pequeñas, aunque eso no garantiza automáticamente que toda la aplicación vaya a funcionar perfectamente cuando todo se conecte.

Limitaciones que noté
Solo prueban funciones aisladas

Una función puede funcionar sola y aun así fallar cuando interactúa con:

bases de datos
APIs
otros módulos
usuarios reales
No prueban rendimiento

Una función puede pasar todos los tests con pocos datos, pero comportarse muy mal cuando recibe miles o millones de elementos.

No prueban todos los escenarios posibles

Siempre van a existir situaciones inesperadas:

datos corruptos
errores externos
entradas raras
fallos de red

Es imposible cubrir absolutamente todo.

Entonces, ¿qué significa realmente que “los tests pasen”?

Después de hacer este taller, para mí significa simplemente esto:

Las validaciones que escribimos dieron verdadero en esa ejecución específica.

Nada más.

No significa que:

el sistema esté perfecto
no existan bugs
producción vaya a funcionar sin problemas
¿Cómo evitar falsas confianzas en un proyecto real?

Creo que hay varias cosas importantes:

validar resultados reales y no solo tipos
probar edge cases
usar mocks
revisar las pruebas críticamente
combinar unit testing con integration testing
no obsesionarse únicamente con el coverage

También entendí que hacer testing bien requiere pensar bastante más de lo que parece.

A veces el código “parece funcionar”, pero cuando empiezas a probar escenarios reales es donde aparecen los errores de verdad.

Reflexión personal final

Lo que más me dejó este taller fue entender que un test no sirve solo porque salga en verde.

Antes veía los tests como una confirmación de que todo estaba correcto.

Ahora entiendo que una prueba realmente útil es la que logra detectar errores antes de que el usuario los encuentre.

Y honestamente, el experimento de cambiar el promedio a 3.14 fue lo que más me ayudó a entender eso, porque mostró claramente cómo unos tests podían seguir pasando incluso cuando el código estaba roto.

Al final, no se trata de tener muchísimas pruebas, sino de tener pruebas que realmente sirvan para validar el comportamiento real del sistema.