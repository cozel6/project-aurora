import socket
import sys
from datetime import datetime

def scan_ports(target, port_range):
    """
    Scanează un interval de porturi pe un target IP dat.

    Args:
        target (str): Adresa IP sau hostname de țintă (ex: "127.0.0.1").
        port_range (tuple): Intervalul de porturi (start_port, end_port).
    """
    print("-" * 50)
    print(f"Scanare inițiată pe țintă: {target}")
    print(f"Interval de porturi: {port_range[0]} - {port_range[1]}")
    print("-" * 50)

    start_time = datetime.now()
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        # Creează un nou socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Setează un timeout pentru a evita blocarea infinite în caz de port neaccesibil
        s.settimeout(1) 

        # Încearcă să te conectezi la port
        result = s.connect_ex((target, port))

        if result == 0:
            # Conexiunea a reușit, portul este deschis
            try:
                # Încearcă să obții serviciul care rulează pe port (ex: http, ssh)
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = "unknown"
                
            print(f"[*] Port {port} este DESCHIS ({service})")
            open_ports.append(port)
        
        s.close() # Închide socket-ul pentru următorul ciclu

    end_time = datetime.now()
    duration = end_time - start_time
    
    print("-" * 50)
    print(f"Scanare finalizată în {duration}")
    
    if open_ports:
        print(f"Porturile deschise găsite: {open_ports}")
    else:
        print("Nu s-au găsit porturi deschise în intervalul specificat.")
    print("-" * 50)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Mod de utilizare: python port_scanner.py <adresa_ip> <port_start>-<port_end>")
        print("Exemplu: python port_scanner.py 127.0.0.1 20-100")
        sys.exit(1)

    target_ip = sys.argv[1]
    port_spec = sys.argv[2]
    
    try:
        # Parsează intervalul de porturi
        start_str, end_str = port_spec.split('-')
        start_port = int(start_str)
        end_port = int(end_str)
        
        if start_port < 1 or end_port < 1 or start_port > 65535 or end_port > 65535 or start_port > end_port:
             print("Eroare: Intervalul de porturi trebuie să fie valid (1-65535) și Start <= End.")
             sys.exit(1)
             
        scan_ports(target_ip, (start_port, end_port))

    except ValueError:
        print("Eroare: Formatul intervalului de porturi trebuie să fie 'START-END'.")
        sys.exit(1)
