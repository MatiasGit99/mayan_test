��    +      t  ;   �      �  	   �     �     �     �     �  2   �  �   0     �  �   �     t     �     �     �     �     �     �  ]   �     E  S   ^     �     �     �  
   �     �  
   �               1  
   :     E     R     b     q  
   �  r   �  j   	  �   s	     
  
   !
     ,
     8
     J
  �  `
  
   �     �          "     /  Q   A  �   �  8  L  �   �     j     �     �     �     �  &   �  )   �  u        �  i   �          .     G     N     _     {  "   �  #   �     �     �     �          (  '   A     i  }   y  �   �  �   |     G  
   L     W     m     �                             $   
                         (               !                          )      	           %      #       +         '   *                                         "         &       Arguments Background task workers Celery Concurrency Default queue? Default: "AMQPLAIN". Set custom amqp login method. Default: "Disabled". Toggles SSL usage on broker connection and SSL settings. The valid values for this option vary by transport. Default: "amqp://". Default broker URL. This must be a URL in the form of: transport://userid:password@hostname:port/virtual_host Only the scheme part (transport://) is required, the rest is optional, and defaults to the specific transports default values. Default: No result backend enabled by default. The backend used to store task results (tombstones). Refer to http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend Dotted path Host Is transient? Keyword arguments Label Low latency high volume tasks Low latency, long lived tasks Maximum amount of resident memory a worker can execute before it's replaced by a new process. Maximum memory per child Maximum number of tasks a worker can execute before it's replaced by a new process. Maximum tasks per child Medium latency tasks Name Nice level Queue count Queue list Queue: %s, not found Queues for worker: %s Schedule Start time Task manager Task type count Task type list Task types for queue: %s Test queue The nice value determines the priority of the process. A higher value lowers the priority. The default value is 0. The number of worker processes/threads to launch. Defaults to the number of CPUs available on the machine. Transient queues are not persistent. Tasks in a transient queue are lost if the broker is restarted. Transient queues use less resources and managed non critical tasks. Type View tasks Worker list Worker process ID Worker: %s, not found Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-07-11 12:52+0000
Last-Translator: Roberto Rosario, 2024
Language-Team: Spanish (https://app.transifex.com/rosarior/teams/13584/es/)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: es
Plural-Forms: nplurals=3; plural=n == 1 ? 0 : n != 0 && n % 1000000 == 0 ? 1 : 2;
 Argumentos Trabajadores de tareas de fondo Celery Concurrencia ¿Cola principal? Valor predeterminado: "AMQPLAIN". Establece el método de inicio de sesión amqp. Valor predeterminado: "Deshabilitado". Alterna el uso de SSL en la conexión del agente y la configuración de SSL. Los valores válidos para esta opción varían según el transporte. Valor predeterminado: "amqp://". URL del intermediario predeterminado Debe ser una URL en forma de: transporte://usuario:contraseña@servidor:puerto/virtual_host Solo se requiere la parte de esquema (transporte: //), el resto es opcional y se predetermina a los valores predeterminados de transporte específico. Predeterminado: Sin back-end de resultados habilitado por defecto. El backend utilizado para almacenar resultados de tareas (lápidas). Consulte http://docs.celeryproject.org/en/v4.1.0/userguide/configuration.html#result-backend Ruta separada por puntos Servidor ¿Es transitoria? Argumentos explícitos Etiqueta Tareas de alto volumen y baja latencia Tareas de baja latencia y larga duración Cantidad máxima de memoria residente que un trabajador puede ejecutar antes de ser reemplazada por un nuevo proceso. Memoria máxima por subprocesso Número máximo de tareas que un trabajador puede ejecutar antes de ser reemplazado por un nuevo proceso. Tareas máximas por subproceso Tareas de latencia media Nombre Nivel de amistad Cantidad de colas de tareas Lista de colas de tareas Cola de tareas: %s , no encontrada Colas de tareas para trabajador: %s Horario Tiempo de inicio Administrador de tareas Cantidad de tipos de tareas Lista de tipos de tareas Tipos de tareas para cola de tareas: %s Lista de prueba El valor de amistad determina la prioridad del proceso. Un valor más alto reduce la prioridad. El valor predeterminado es 0. El número de procesos/hilos de trabajo que se lanzarán. El valor predeterminado es la cantidad de CPUs disponibles en la máquina. Las colas transitorias no son persistentes. Las tareas en una cola transitoria se pierden si se reinicia el intermediario. Las colas transitorias utilizan menos recursos y gestionan tareas no críticas. Tipo Ver tareas Lista de trabajadores ID del proceso trabajador Trabajador: %s , no encontrado 