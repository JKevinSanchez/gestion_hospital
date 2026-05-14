INSERT INTO pacientes (nombre, dni, telefono, fecha_nacimiento) VALUES
('Juan Pérez', '12345678A', '600123456', '1980-05-15'),
('María García', '87654321B', '600654321', '1992-10-20'),
('Carlos López', '11223344C', '611223344', '1975-03-12');

INSERT INTO medicos (nombre, especialidad) VALUES
('Dr. Roberto Sánchez', 'Cardiología'),
('Dra. Laura Gómez', 'Pediatría'),
('Dr. Antonio Ruiz', 'Traumatología');

INSERT INTO citas (id_paciente, id_medico, fecha, estado) VALUES
(1, 1, '2026-06-01 10:00', 'PENDIENTE'),
(2, 2, '2026-06-02 11:30', 'PENDIENTE'),
(3, 1, '2026-06-03 09:00', 'PENDIENTE');
