import socket

def port_scan(target_host, target_ports):
    # Belirtilen hedef IP adresini çözümleme
    target_ip = socket.gethostbyname(target_host)

    # Belirtilen portları tara
    for port in target_ports:
        # Yeni bir soket oluştur
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)

        # Port taramasını gerçekleştir
        result = client_socket.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: Açık")
        else:
            print(f"Port {port}: Kapalı")

        # Soketi kapat
        client_socket.close()

# Kullanıcıdan IP adresini ve portları al
target_host = input("Hedef IP adresini girin: ")
port_str = input("Taramak istediğiniz portları virgülle ayırarak girin: ")
target_ports = [int(port) for port in port_str.split(",")]

# Port taramasını gerçekleştir
port_scan(target_host, target_ports)
