# Playbook: Offboarding de usuario

## 1. Objetivo y alcance
Este playbook tiene como objetivo estandarizar y asegurar la ejecución del proceso de offboarding de colaboradores en Alegra. Su alcance incluye la suspensión de accesos, gestión de licencias y transferencia de información autorizada, garantizando que ninguna cuenta de un colaborador retirado permanezca activa más allá del día efectivo de su retiro, según la Regla 2.

## 2. Datos que deben verificarse antes de iniciar
- Ticket de solicitud de People Ops.
- Datos del usuario en `data/usuarios.csv`.
- Licencias asignadas en `data/licencias.csv`.
- Registros de actividad en `data/logins.csv` (opcional, para auditoría).

## 3. Verificación de la persona y fecha de retiro
1. Recibir la notificación de People Ops (ticket).
2. Validar que la persona existe en `data/usuarios.csv`.
3. Confirmar la fecha de retiro efectiva. Si no es clara, solicitar aclaración a People Ops.

## 4. Suspensión de cuenta (Regla 2)
El día efectivo del retiro:
1. Suspender la cuenta principal (ej. Google Workspace).
2. Verificar que no queden accesos activos en otros sistemas.

## 5. Revisión de licencias y accesos
1. Listar todas las licencias del usuario en `data/licencias.csv`.
2. Para cada licencia (ej. Salesforce, Figma, GitHub):
   - Evaluar si es necesaria para el equipo (reasignación) o debe cancelarse para optimizar costos (Regla 4).

## 6. Gestión de licencias
1. **Identificación:** Listar licencias del usuario. Identificar cuáles han estado sin uso por más de 60 días, las cuales deben reportarse para reasignación o cancelación según la Regla 4.
2. **Recomendación:** Documentar en el reporte de evidencia si cada licencia debe ser reasignada o cancelada.

## 7. Transferencia de archivos de Drive
1. Confirmar en el ticket la solicitud/autorización de transferencia de archivos.
2. Identificar el usuario destino para la transferencia.
3. Documentar en el reporte de evidencia la acción de transferencia a realizar.

## 8. Verificaciones finales
1. Confirmar que el usuario no tiene accesos activos.
2. Confirmar que las licencias han sido gestionadas.
3. Confirmar que los archivos fueron transferidos (si aplica).

## 9. Evidencias
Toda acción debe documentarse en `evidencia/offboarding-[correo_colaborador]-[fecha_ejecucion].md` siguiendo la estructura:
- Responsable de la acción.
- Fecha de ejecución.
- Descripción de las acciones tomadas.
- Soporte (fragmentos de archivos modificados).

## 10. Gestión de inconsistencias
Si los datos en `data/` no coinciden con la realidad (ej. usuario retirado pero licencia activa) o falta información crítica, **ESCALAR** el ticket a People Ops solicitando aclaración inmediata. Este playbook verifica los archivos de datos para documentar acciones necesarias; **no se deben modificar los archivos CSV originales durante este proceso**. Toda acción debe quedar registrada únicamente en el reporte de evidencia.

## 11. Prompt reutilizable para agentes de IA
> "Ejecuta el playbook de offboarding para el usuario [correo].
> Fecha efectiva de retiro: [fecha].
> Solicitud de transferencia de archivos: [Sí/No, a quién].
> Consulta `data/usuarios.csv`, `data/licencias.csv` y aplica las reglas de IT para:
> 1. Suspender accesos principales.
> 2. Gestionar licencias (reasignar/cancelar).
> 3. Gestionar archivos (si aplica).
> 4. Documentar el reporte en `evidencia/offboarding-[correo]-[fecha].md`."

## 12. Caso de prueba (TICKET-005)
**Colaborador:** María Fernanda López (`maria.lopez@alegra.com`)
**Fecha efectiva:** 2026-07-31
**Acciones:**
1. Verificar datos en `data/usuarios.csv`.
2. Identificar licencias en `data/licencias.csv` (Google Workspace, Figma, Salesforce).
3. Programar suspensión de cuenta para el 2026-07-31.
4. Programar gestión de licencias.
5. Programar transferencia de Drive según solicitud en ticket.
6. Documentar hallazgos y acciones en reporte de evidencia.
