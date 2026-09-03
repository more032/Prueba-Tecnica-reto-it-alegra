import csv
from datetime import datetime

# Reference date: 2026-07-15
TODAY = datetime.strptime('2026-07-15', '%Y-%m-%d')

def read_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

usuarios = read_csv('data/usuarios.csv')
logins = read_csv('data/logins.csv')
licencias = read_csv('data/licencias.csv')

# Build helper lookups
usuarios_dict = {u['email']: u for u in usuarios}
logins_dict = {}
for l in logins:
    email = l['email']
    prod = l['producto']
    last_login = datetime.strptime(l['ultimo_login'], '%Y-%m-%d')
    if email not in logins_dict:
        logins_dict[email] = {}
    logins_dict[email][prod] = last_login

print("--- AUDITORÍA DE ACCESOS ---")

print("\n1. Usuarios retirados con cuentas/licencias activas:")
for u in usuarios:
    if u['estado'] == 'retirado':
        email = u['email']
        ret_date = datetime.strptime(u['fecha_retiro'], '%Y-%m-%d')
        # Check active licenses
        user_lics = [l for l in licencias if l['email'] == email]
        active_lics = [l for l in user_lics if l['estado'] == 'activa']
        
        print(f"\n- {u['nombre']} ({email}) - Retirado el {u['fecha_retiro']}")
        if active_lics:
            print(f"  ALERTA: Tiene licencias activas:")
            for l in active_lics:
                print(f"    * {l['producto']} ({l['plan']}) - Asignada el {l['fecha_asignacion']} - Costo: ${l['costo_mensual_usd']}/mes")
        else:
            print(f"  Correcto: No tiene licencias activas (todas suspendidas/removidas).")
            
        # Check logins after retirement
        if email in logins_dict:
            for prod, login_date in logins_dict[email].items():
                if login_date > ret_date:
                    days_after = (login_date - ret_date).days
                    print(f"  !!! BRECHA DE SEGURIDAD !!! Login en {prod} el {login_date.strftime('%Y-%m-%d')} ({days_after} días después del retiro)")

print("\n2. Licencias asociadas a correos que no existen en usuarios.csv (Cuentas Fantasma):")
for l in licencias:
    email = l['email']
    if email not in usuarios_dict:
        print(f"- Licencia de {l['producto']} ({l['plan']}) para {email} ({l['nombre_titular']}) - Estado: {l['estado']} - Costo: ${l['costo_mensual_usd']}/mes")
        if email in logins_dict and l['producto'] in logins_dict[email]:
            last_login = logins_dict[email][l['producto']].strftime('%Y-%m-%d')
            print(f"  Último login en {l['producto']}: {last_login}")
        else:
            print(f"  No tiene registros de login en {l['producto']}")

print("\n3. Logins de correos que no existen en usuarios.csv:")
for email in logins_dict:
    if email not in usuarios_dict:
        for prod, login_date in logins_dict[email].items():
            # Check if this login matches an active license
            has_lic = any(l for l in licencias if l['email'] == email and l['producto'] == prod and l['estado'] == 'activa')
            print(f"- Login en {prod} el {login_date.strftime('%Y-%m-%d')} por {email} (Tiene licencia activa: {has_lic})")

print("\n4. Licencias inactivas (sin uso por más de 60 días):")
for l in licencias:
    if l['estado'] == 'activa':
        email = l['email']
        prod = l['producto']
        if email in logins_dict and prod in logins_dict[email]:
            last_login = logins_dict[email][prod]
            days_inactive = (TODAY - last_login).days
            if days_inactive > 60:
                print(f"- {email} - {prod} ({l['plan']}): Inactiva por {days_inactive} días (Último login: {last_login.strftime('%Y-%m-%d')}) - Costo: ${l['costo_mensual_usd']}/mes")
        else:
            # No login record for this license in logins
            # Check if there's any login at all for this user in logins
            print(f"- {email} - {prod} ({l['plan']}): SIN REGISTRO de login para este producto - Costo: ${l['costo_mensual_usd']}/mes")
