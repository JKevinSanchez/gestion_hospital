CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    dni TEXT UNIQUE NOT NULL,
    telefono TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS medicos (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especialidad TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS citas (
    id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'PENDIENTE',
    FOREIGN KEY (id_paciente) REFERENCES pacientes (id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES medicos (id_medico) ON DELETE CASCADE
);
