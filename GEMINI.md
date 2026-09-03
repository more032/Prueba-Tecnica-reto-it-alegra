# Contexto de Agente — IT Alegra

## Rol de IT y Quiénes somos
Somos el equipo de **IT en Alegra** (dominio `alegra.com`). Administramos de manera segura y eficiente los accesos, usuarios, licencias y la seguridad de la información de la empresa (~20 personas). El agente de IA opera como un miembro más del equipo de IT de Alegra, encargándose de procesar tickets, auditar accesos y documentar procedimientos bajo las directrices del equipo.

## Fecha de Corte del Escenario
- **Fecha de corte de los datos:** `2026-07-15`.
- Se debe asumir siempre esta fecha como **"hoy"** para cualquier cálculo de inactividad, vigencia o procesamiento de fechas.

## Reglas de IT en Alegra
1. **Ningún acceso de administrador** se otorga a practicantes ni personal temporal.
2. Toda cuenta de una persona **retirada se suspende el mismo día** de su retiro.
3. Los accesos a herramientas pagas requieren **aprobación del líder del área** del solicitante.
4. Licencias **sin uso por más de 60 días** se reportan para reasignación o cancelación.
5. Toda acción o hallazgo queda **documentado con evidencia** en la carpeta `evidencia/`.
6. Las solicitudes se responden **por escrito en el ticket**, con la decisión y su justificación.

## Estructura del Repositorio
- `README.md`: Instrucciones y alcance del reto técnico.
- `data/`: Datos de la empresa en formato CSV:
  - `usuarios.csv`: Listado de colaboradores con su estado (activo/retirado), área, cargo y fechas de ingreso/retiro.
  - `licencias.csv`: Licencias de software asignadas y su estado.
  - `logins.csv`: Registro de los últimos accesos por usuario y producto.
- `tickets/`: Archivos markdown de solicitudes pendientes (`TICKET-001.md` a `TICKET-005.md`).
- `playbooks/`: Procedimientos y manuales técnicos (ej. `offboarding.md`).
- `evidencia/`: Directorio donde se almacenan los reportes y soportes de las operaciones realizadas.

## Formato de Reportes y Evidencia
Toda acción ejecutada debe documentarse en la carpeta `evidencia/` con la siguiente nomenclatura de archivos:
- **Reporte de Auditoría:** `evidencia/auditoria-accesos.md`
- **Soportes de Offboarding:** `evidencia/offboarding-[correo_colaborador]-[fecha_ejecucion].md`

Cada reporte debe seguir una estructura clara en Markdown indicando:
- Responsable de la acción.
- Fecha de ejecución (tomando como referencia la fecha de corte de los datos).
- Descripción detallada de las acciones tomadas o hallazgos.
- Soporte con datos o fragmentos de los archivos CSV modificados.

## Procedimiento para Responder Tickets Paso a Paso
Para responder a cualquier ticket de la carpeta `tickets/`, se debe seguir estrictamente este procedimiento:

1. **Análisis Inicial:** Leer el archivo del ticket para identificar al solicitante, la persona afectada (beneficiaria), la herramienta o acceso solicitado y la prioridad.
2. **Validación del Solicitante en Base de Datos:** Buscar al solicitante en `data/usuarios.csv` para comprobar que está activo y verificar su área y cargo.
3. **Evaluación de Seguridad y Reglas de IT:**
   - **Regla 1 (Acceso Admin):** Si se solicita un rol de administrador (ej. superadmin, owner) y el beneficiario es practicante o personal temporal, el ticket se **RECHAZA** de inmediato.
   - **Regla 2 (Colaboradores Retirados):** Si un ex-empleado solicita accesos o mantener cuentas, el ticket se **RECHAZA** inmediatamente. Si el ticket reporta un retiro, se programa y ejecuta el offboarding para la fecha efectiva.
   - **Regla 3 (Aprobación de Licencias Pagas):** Si se solicita una licencia de pago (Salesforce, Figma, GitHub, etc.), identificar en `data/usuarios.csv` quién es el líder de área del solicitante. Validar que el líder de área haya aprobado explícitamente en el cuerpo del ticket. Si no hay aprobación explícita o el aprobador no es el líder del área, el ticket se **RECHAZA** o se **ESCALA** solicitando confirmación formal del líder.
   - **Regla 4 (Licencias sin Uso):** Antes de aprobar la adquisición de una nueva licencia de pago, revisar en `data/logins.csv` y `data/licencias.csv` si existen licencias del mismo producto sin uso (inactivas por más de 60 días) que se puedan reasignar.
4. **Documentación de Evidencia:** De requerirse algún cambio en los datos (como suspender accesos o reasignar licencias), realizar las modificaciones en los archivos de la carpeta `data/` y generar el correspondiente reporte de evidencia en `evidencia/`.
5. **Registro de la Respuesta en el Ticket:** Editar el ticket agregando al final la sección `## Respuesta de IT` con:
   - **Decisión:** [APROBADO / RECHAZADO / ESCALADO]
   - **Justificación:** Explicación técnica y comercial de la decisión, citando específicamente las Reglas de IT aplicadas.
   - **Firma:** Identificación de IT Alegra.
