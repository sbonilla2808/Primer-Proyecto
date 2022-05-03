while True:
  if x &gt; 4:
    print("¡La condición era verdadera!") #Esta sentencia se ejecuta</code></pre><h3 id="sentencia-else"><strong>Sentencia else</strong></h3><p>Opcionalmente, puedes agregar una respuesta <code>else</code> que se ejecutará si la condición es <code>false</code></p><pre><code class="language-python">if not True:
    print('¡La sentencia If se ejecutará!')
  else:
    print('¡La sentencia Else se ejecutará!')</code></pre><p>O también puedes ver este ejemplo:</p><pre><code class="language-python">y = 3

  if y &gt; 4:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
  else:
  print("¡La condición no era verdadera!") #esta sentencia se ejecuta</code></pre><p><strong>Sentencia elif</strong></p><p>Se pueden verificar varias condiciones al incluir una o más verificaciones <code>elif</code> después de su declaración <code>if</code> inicial. Ten en cuenta que solo se ejecutará una condición:</p><pre><code class="language-python">z = 7

  if z &gt; 8:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
  elif z &gt; 5:
  print("¡Yo lo haré!") #esta sentencia se ejecuta
  elif z &gt; 6:
  print("¡Tampoco voy a imprimir!") #esta sentencia no se ejecuta
  else:
  print("¡Yo tampoco!") #esta sentencia no se ejecuta</code></pre><p><em>Nota: solo se ejecutará la primera condición que se evalúe como <em><code>true</code></em>. </em>Aunque <code>z &gt; 6</code> es <code>true</code>, el bloque <code>if/elif/else</code> termina después de la primera condición verdadera. Esto significa que un <code>else</code> solo se ejecutará si ninguna de las condiciones es <code>true</code>.</p><p><strong>Sentencias if anidadas</strong></p><p>También podemos crear if anidados para la toma de decisiones. </p><p>Tomemos un ejemplo de cómo encontrar un número que sea par y también mayor que 10</p><pre><code class="language-text">python 
  x = 34
  if x %  2 == 0:  # así es como creas un comentario y ahora comprueba número par.
  if x &gt; 10:
  print("Este número es par y es mayor que 10")
  else:
  print("Este número es par, pero no mayor 10")
  else:
  print ("El número no es par. Así que punto de verificación más.")</code></pre><p><br>Este fue solo un ejemplo simple de if anidados. No dudes en explorar más en línea.</p><p>Si bien los ejemplos anteriores son simples, puedes crear condiciones complejas utilizando comparaciones booleanas y operadores booleanos.</p><p><strong>Declaración if-else de Python en línea</strong><br>También podemos usar declaraciones if-else en funciones de Python en línea. El siguiente ejemplo debe verificar si el número es mayor o igual que 50, si es así, retorna True:</p><pre><code class="language-text">python 
  x = 89
  es_mayor = True if x &gt;= 50 else False





name = input("What is your name: ")
edad = int(input("Edad: "))
cedu = input("numero de ID: ")
a = [
     "nombre:", name,
     "ID", cedu,
     "edad:", edad,
]
EDAD_A = 18
while True:
    if int(edad) < EDAD_A:
        print("Eres menor de edad, el programa no puede seguir.")
        break
    else:
        pass
    c = str(input("What is your name: "))
    if c in a:
        print("Right")
        pass
    else:
        print("Wrong")
        continue
    d = str(input("What is your ID: "))
    if d in a:
        print("Right")
        break
    else:
        print("Wrong")
        continue
        
