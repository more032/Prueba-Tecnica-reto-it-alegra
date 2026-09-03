# NOTAS.md

## 1. Agente utilizado
Gemini CLI.

## 2. Modelo utilizado
Gemini 3.1 Flash Lite.

## 3. Instalación y configuración
El agente se utilizó en un entorno preconfigurado para el desarrollo del reto técnico, con los permisos y dependencias necesarias ya establecidos en el workspace.

## 4. Tareas delegadas al agente
- Auditoría integral de usuarios, licencias y registros de acceso (`data/` directory).
- Generación del reporte `evidencia/auditoria-accesos.md`.
- Procesamiento y resolución de tickets (`tickets/TICKET-003.md`, `TICKET-004.md`, `TICKET-005.md`).
- Redacción y estructuración del playbook de offboarding (`playbooks/offboarding.md`).

## 5. Verificaciones personales
- Revisión manual de todos los comandos de filtrado en PowerShell para garantizar la precisión de los datos extraídos de los archivos CSV.
- Validación línea por línea de los cambios efectuados en los tickets para asegurar coherencia con las reglas del README.
- Verificación de la estructura y contenido del playbook creado.

## 6. Errores y conclusiones corregidas
- **Comandos PowerShell:** Se detectaron bloqueos por "Command injection" en el uso de subexpresiones `$()` en comandos, lo que requirió simplificar la sintaxis de las consultas.
- **Justificación de tickets:** Se ajustó la redacción en las respuestas de IT para alinearlas estrictamente con las Reglas 2 y 3 del README, eliminando interpretaciones subjetivas o afirmaciones no explícitas.
- **Playbook:** Se corrigió la instrucción sobre la modificación directa de archivos `data/` en el playbook de offboarding para garantizar la integridad de los datos originales.

## 7. Propuestas de mejora
Con mayor disponibilidad de tiempo, se implementarían:
- Scripts de automatización en Python o PowerShell para generar reportes de auditoría de manera periódica, reduciendo la dependencia de consultas manuales.
- Un sistema de validación de datos más robusto para detectar automáticamente discrepancias entre registros de acceso y licencias activas antes de la intervención del agente.
