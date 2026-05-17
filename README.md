# 🏥 Sistema de Gestión Hospitalaria

Una aplicación de consola robusta desarrollada en Python para la gestión integral de un centro médico. Permite administrar pacientes, médicos y citas utilizando una base de datos relacional SQLite y una arquitectura de software modular basada en capas (Modelos, Servicios, Vistas).

---

##  Características Principales

* *Base de Datos Relacional (SQLite3)*
    * Inicialización automática mediante esquema.sql y volcado de datos iniciales con semilla.sql.
    * Uso de llaves foráneas (FOREIGN KEY) con borrado en cascada (ON DELETE CASCADE).
    * Transacciones seguras (@contextmanager) e inserciones atómicas para evitar la pérdida de datos.
* *Arquitectura Multicapa (MVC)*
    * *Vistas/Menús:* Interfaces de consola interactivas, tablas ASCII dinámicas y menús de navegación limpios.
    * *Servicios:* Capa intermedia que aplica las reglas de negocio y delega acciones.
    * *Modelos:* Capa de acceso a datos, encargada de las consultas SQL, JOINs y agregaciones estadísticas.
* *Sistema de Validaciones Estricto*
    * Comprobación de formato de DNI español y teléfonos mediante Expresiones Regulares (RegEx).
    * Verificación lógica de fechas temporales (nacimientos en el pasado, citas agendadas en el futuro).
* *Manejo de Errores Personalizado*
    * Sistema propio de excepciones (NotFoundError, DatabaseError, ValidationError).
    * Captura de interrupciones manuales (Ctrl+C) para un cierre limpio del programa sin romper la consola.

---

##  Estructura del Proyecto

El código está organizado de forma escalable, separando claramente las responsabilidades:

```text
gestion_hospitales/
│
├── main.py                 # Punto de entrada de la aplicación
│
├── database/               # Capa de Base de Datos
│   ├── conexion.py         # Gestor de contexto seguro para conexiones SQLite
│   ├── esquema.sql         # DDL: Estructura de tablas (pacientes, medicos, citas)
│   └── semilla.sql         # DML: Datos de prueba iniciales (Seeders)
│
├── menus/                  # Capa de Presentación (Vistas)
│   ├── main_menu.py        # Enrutador principal de la consola
│   ├── paciente_menu.py    # Interfaz CRUD para Pacientes
│   ├── medico_menu.py      # Interfaz CRUD para Médicos
│   └── cita_menu.py        # Interfaz de agenda y reportes estadísticos
│
├── modelos/                # Capa de Acceso a Datos (Data Access)
│   ├── paciente_model.py   # Consultas SQL a la tabla pacientes
│   ├── medico_model.py     # Consultas SQL a la tabla medicos
│   └── cita_model.py       # Consultas SQL, JOINs y validación de disponibilidad
│
├── servicios/              # Capa de Lógica de Negocio (Business Logic)
│   ├── paciente_service.py # Filtros y validaciones antes de insertar pacientes
│   ├── medico_service.py   # Filtros y validaciones para médicos
│   └── cita_service.py     # Lógica de agendamiento y prevención de choques de horario
│
└── utilidades/             # Herramientas Transversales (Cross-cutting)
    ├── ayudas.py           # Funciones UI: Limpiar pantalla, inputs seguros y tablas ASCII
    ├── excepciones.py      # Clases de error personalizadas
    └── validadores.py      # Funciones de sanitización de strings y comprobación de regex

---

##  Autores

El desarrollo de los diferentes componentes de la aplicación se organizó de forma equitativa entre los integrantes de 1º ASIR:

* *Jacques Kevin Sánchez Guerra*
    
* *Fred Farit Bendezu Hernández*
    
* *Mario López Sánchez*