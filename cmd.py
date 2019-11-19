#En este programa pondre una guia basica para cmd y bash

print('\n\tQue quieres hacer: ')
print('''
	0. Guia sobre cmd

	1. Guia sobre bash

	2. Ambas guias 
	''')

opcion = input('\tOpcion: ')



def cmd():
	print ('''
	Como configurar la Consola de CMD o Símbolo del sistema en Windows

	Personalizar el aspecto, el tamaño y los colores de la consola de comandos 
	o ventana de MSDOS. Habilitar la Edición rápida para poder copiar y pegar 
	texto y otras opciones. Como guardar la configuración creada en una clave 
	del Registro. Establecer el tamaño y los colores con los que se muestran 
	los archivos batch.

	La consola de CMD, tan utilizada por los emplean la línea de comandos, es 
	posible configurarla de forma tal que muestre otro aspecto, colores y 
	fuentes, otras dimensiones para que se adapte mejor a nuestro escritorio, 
	de acuerdo al tamaño del monitor que usamos.
	También es posible habilitar otras opciones, como es la Edición rápida que 
	permite editar el texto, es decir copiar los mensajes generados e incluso 
	pegar las instrucciones y así no tener que escribirlas.

	Configuración de la consola de CMD

	Para acceder al cuadro de configuración, da un clic en la esquina superior 
	izquierda de la ventana, donde aparece el icono negro, selecciona en el menú 
	que aparece "Propiedades" y se abrirá la ventana de configuración de la consola.

	Valores de configuración recomendados para la consola

	Los siguientes valores son los que recomienda Microsoft, para los que realizan 
	trabajo de edición regularmente con esta herramienta.
	Estos valores hacen que aumente un poco el consumo de memoria asignada, pero 
	logran una mejor visualización, más resolución y ajuste del texto.
	Sigue los siguientes pasos, pero los valores son opcionales, algunos como el 
	tamaño de la pantalla dependen de las dimensiones del monitor y de su resolución.

	La pestaña Opciones
	• En la sección Historial de comandos, escribe en Tamaño del búfer: 999
	Al aumentar el tamaño del búfer de pantalla a 999, se habilita el desplazamiento 
	por la ventana de la consola.
	• Escribe en Número de búferes: 5
	Al aumentar el número de búferes a cinco, se incrementa el número de líneas de 
	la ventana de la consola a 5000
	• En la sección Opciones de edición, activa las casillas de Modalidad de edición 
	rápida y Modalidad de inserción.
	La modalidad de edición rápida va a permitir copiar contenido de cualquier archivo 
	de texto o documento y pegarlo en la consola solo dando un clic derecho con el ratón.
	Así mismo se podrá copiar el texto que selecciones en la consola, dando un clic con 
	el botón derecho en el área seleccionada y luego pegarlo en cualquier editor o archivo 
	de texto.

	La pestaña Diseño
	• En la sección Tamaño del búfer de pantalla, escribe 2500 en Alto y aumenta el Ancho.
	• En la sección Tamaño de la ventana, aumenta el Alto y Ancho.
	• En la sección Posición de la ventana, cambia los valores de Izquierda y Superior.
	• Desactiva la casilla de verificación El sistema ubica la ventana
	En el cuadro de diálogo Aplicar propiedades, has clic en "Guardar propiedades para todas 
	las ventanas con el mismo título".

	La pestaña Fuente
	Permite selecciona el tipo y el tamaño del texto.

	La pestaña Colores
	Aquí puedes personalizar la apariencia de la consola escogiendo los colores del texto y del fondo.

	Guardar los ajustes de la configuración de la consola en el Registro de Windows

	Los valores de la configuración de la consola de CMD para el uso general, se encuentran en la 
	siguiente clave del registro:
	HKEY_CURRENT_USERconsole\
	HKEY_CURRENT_USERconsoleSystemRoot%_system32_cmd.exe
	Y la configuración específica del administrador se encuentra en la subclave:
	Esto se debe a que hay otras aplicaciones que utilizan la consola y necesitan tener su configuración 
	específica.
	Los valores usados en la sección anterior para configurar la consola, son los que aparecen en el cuadro 
	siguiente, con ellos se puede crear un archivo REG, para en otra ocasión combinar dicha clave y así no 
	tener que introducirlos nuevamente.
	Windows Registry Editor Version 5.00

	[HKEY_CURRENT_USERconsole]
	"QuickEdit"=dword:00000001
	"ScreenColors"=dword:0000000e

	[HKEY_CURRENT_USERconsoleSystemRoot%_system32_CMD.exe]
	"ScreenBufferSize"=dword:09c400c8
	"WindowSize"=dword:0019005a
	"NumberOfHistoryBuffers"=dword:00000005
	"WindowPosition"=dword:00e9021b
	"HistoryBufferSize"=dword:000003e7    

	Configurar el Autorun o inicio de la consola de CMD

	Podemos configurar la consola de manera que cada vez que se inicie, se muestre en ella un texto o mensaje determinado.
	Para eso solo es necesario especificarlo en la clave del Registro que controla su inicio, también llamado Autorum.
	Hazlo de la forma siguiente:
	• Accede a la siguiente clave del Registro: [HKEY_CURRENT_USER/Software/Microsoft/Command Processor]
	• Si no existe el valor Autorun, se debe crear un Nuevo valor de cadena y darle dicho nombre.
	• Da dos clics en el valor creado e introduce el mensaje que se quiere mostrar de la siguiente forma: Autorun= ECHO "Mensaje"

	Configurar como se muestra la consola y los archivos batch

	Hasta ahora vimos como configurar la consola para usar directamente la línea de comandos.
	También podemos configurar algunos valores de ajuste en los archivos batch, para en cada uno de ellos 
	se muestra la consola de forma diferente.
	La ventaja es que hay aplicaciones que solo necesitan de un espacio reducido en la pantalla, en ese 
	caso podemos agregar en el propio archivo batch las opciones necesarias para que se ejecute en la 
	consola, pero ajustándose ella en un valor especifico.
	También podemos hacer que algunos archivos batch se ejecuten usando colores determinados, en el fondo 
	y en el texto, que no son los que usamos normalmente.
	Configurar y ajustar el tamaño de la consola de CMD

	Las dimensionen de la consola y de los archivos batch, se establecen con el comando MODE CON.

	¿Cómo usar el comando MODE CON?

	El comando MODE CON configura los dispositivos de sistema, podemos usarlo con varios propósitos, en 
	este caso solo para ajustar el tamaño de la consola es de la siguiente forma:
	El modo de pantalla, es decir las dimensiones:
	MODE CON COLS=c LINES=n
	Donde c es la cantidad de columnas y n la cantidad de líneas.
	Por ejemplo:
	MODE CON cols=70 lines=9
	Lee sobre los otros empleos del comando MODE CON: Como usar la línea de comandos en Windows, ejemplos 
	prácticos

	Configurar y ajustar el color de la consola de CMD

	Los colores que le queremos asignar al fondo y al texto de la consola, de establecen con el comando COLOR.

	¿Cómo usar el comando COLOR?

	COLOR atributo
	Donde el atributo corresponde a dos dígitos hexadecimales, el primero corresponde al color del fondo, 
	es segundo al color del texto.
	Los dígitos pueden ser cualquiera de los siguientes valores:

	0 = Negro	
	1 = Azul oscuro	
	2 = Verde	
	3 = Verde-azul	
	4 = Marron	
	5 = Púrpura	
	6 = Oliva	
	7 = Blanco	
	8 = Gris	
	9 = Azul	
	A = Verde limon	
	B = Aguamarina	
	C = Rojo	
	D = Rosa	
	E = Amarillo	
	F = Blanco brillante

	Ejemplos de combinaciones usadas comunmente:

	COLOR 07 Fondo negro texto blanco (predeterminado)
	COLOR 0E Fondo negro texto amarillo
	COLOR 9F Fondo azul claro texto blanco brillante
	COLOR 17 Fondo azul oscuro texto blanco
	COLOR 27 Fondo verde texto blanco

	Puedes crear un archivo batch en tu equipo, que te ayudará a establecer los colores de la consola 
	de CMD y al mismo tiempo te será instructivo si miras el código que contiene.
	Usa el siguiente codigo.
	Si tienes dudas lee el siguiente artículo que explica cómo crearlo: Qué son los archivos BATCH o 
	BAT, usos prácticos y como crearlos

	Ejemplo práctico de la configuración de la consola de CMD

	Un sencillo ejemplo que muestra el código empleado para crear un archivo batch y la imagen del 
	aspecto que muestra la consola al ejecutarlo.

	@ECHO OFF
	mode con cols=46 lines=9
	COLOR 1F
	ECHO Algunas variables de entorno
	echo.
	echo S.O actual: %OS%
	echo Fecha actual: %DATE%
	echo Hora actual: %TIME%
	echo Nombre del equipo: %COMPUTERNAME%
	echo Nombre del usuario: %USERNAME%
	pause>nul

	''')

def bash():
	print ('''
	HHHHHHHHH
	HHHHHH
	HHH     B
	HHH     B
	HHHHHH
	HHHHHHHHH
	''')

if opcion == '0':
	print(cmd())
elif opcion == '1':
	print(bash())
elif opcion == '2':
	print(cmd())
	print(bash())