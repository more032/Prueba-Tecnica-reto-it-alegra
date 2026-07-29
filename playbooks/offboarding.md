# Playbook: Offboarding de usuario

> **Estado: BORRADOR.** Diana empezó a escribirlo antes de salir a vacaciones
> y quedó incompleto. Falta todo lo marcado con TODO y seguramente pasos que
> ni siquiera están listados.

## Cuándo se ejecuta

Cuando People Ops notifica el retiro de una persona (por ticket), con fecha
efectiva.

## Pasos

1. Recibir la notificación de People Ops y confirmar: nombre, correo, área y
   fecha efectiva del retiro.
2. Verificar que la persona exista en `data/usuarios.csv` y revisar qué
   licencias tiene asignadas en `data/licencias.csv`.
3. El día del retiro: suspender la cuenta de Google Workspace.
4. TODO: licencias de terceros (Salesforce, Figma, GitHub…) — ¿se suspenden,
   se cancelan, se reasignan? ¿en qué orden?
5. TODO: archivos y Drive — ¿a quién se transfieren? ¿quién lo aprueba?
6. TODO: actualizar los CSV de `data/` para que reflejen el retiro.
7. TODO: evidencia — qué se guarda, dónde y con qué formato.

## Verificación final

TODO

## Notas

- Ojo: hemos tenido casos de cuentas de retirados que quedan activas por
  semanas. Este playbook existe justamente para que eso no vuelva a pasar.
