# Auditoría de accesos

## Fecha de corte
2026-07-15

## Alcance
La auditoría se realizó sobre los siguientes archivos del repositorio:
- `data/usuarios.csv`
- `data/licencias.csv`
- `data/logins.csv`

## Hallazgos

### 1. Jorge Ramírez (Colaborador retirado)
- **Evidencia:** Usuario retirado el 2026-05-30. Licencias `Google Workspace` y `Salesforce` marcadas como "activa".
- **Regla de IT relacionada:** Regla 2 (Toda cuenta de una persona retirada se suspende el mismo día de su retiro).
- **Nivel de riesgo:** Alto (Acceso residual de ex-empleado).
- **Acción recomendada:** Suspender licencias inmediatamente y realizar el proceso de offboarding correspondiente.

### 2. jperez@alegra.com (Acceso sin correspondencia)
- **Evidencia:** Licencia `Figma` (Professional, $15/mes) activa. El email no figura en `usuarios.csv`.
- **Regla de IT relacionada:** Control de accesos y gestión de inventario.
- **Nivel de riesgo:** Medio (Requiere validación).
- **Acción recomendada:** Verificar la legitimidad de esta cuenta con el equipo de People Ops.

### 3. dev.externo@alegra.com (Acceso sin correspondencia)
- **Evidencia:** Licencia `GitHub` (Team, $4/mes) activa. El email no figura en `usuarios.csv`.
- **Regla de IT relacionada:** Control de accesos y gestión de inventario.
- **Nivel de riesgo:** Medio (Requiere validación).
- **Acción recomendada:** Verificar la naturaleza de esta cuenta con el líder técnico correspondiente.

### 4. Licencias inactivas (> 60 días)
*Nota: Se considera la fecha de corte 2026-07-15. No se incluyen las licencias de Jorge Ramírez en este grupo, ya que su problema es la vigencia post-retiro.*

- **juan.perez@alegra.com** / Figma / Último login: 2024-03-20 / Costo: $15
- **maria.lopez@alegra.com** / Figma / Último login: 2026-03-10 / Costo: $15
- **maria.lopez@alegra.com** / Salesforce / Último login: 2026-02-28 / Costo: $80

- **Regla de IT relacionada:** Regla 4 (Licencias sin uso por más de 60 días se reportan para reasignación o cancelación).
- **Nivel de riesgo:** Medio (Ineficiencia presupuestaria).
- **Acción recomendada:** Validar uso con los usuarios y proceder a la reasignación o cancelación de las licencias si no son necesarias.

## Resumen Final
Se han identificado costos mensuales de $110 USD en licencias potencialmente innecesarias (por inactividad > 60 días) y se han detectado riesgos de seguridad por acceso de ex-empleados y cuentas no verificadas.

**Acciones recomendadas urgentes:**
1. Suspender accesos de Jorge Ramírez (Regla 2).
2. Auditar cuentas `jperez@alegra.com` y `dev.externo@alegra.com` para verificar su origen.
3. Optimizar presupuesto cancelando o reasignando licencias inactivas (Regla 4) que suman $110 USD mensuales.
