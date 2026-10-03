CYAN = "\033[96m"
RESET = "\033[0m"

BANNER = CYAN + r"""
 _       __                    _____ _           
| |     / /___ _____  ____     / ___/(_)___  ____ 
| | /| / / __ `/ __ \/ __ \    \__ \/ / __ \/ __ \
| |/ |/ / /_/ / / / / / / /   ___/ / / /_/ / / / /
|__/|__/\__,_/_/ /_/_/ /_/   /____/_/\____/_/ /_/

        WannnSion Scanner v1.0 | by Wannn Sion
""" + RESET
print(BANNER)




import socket, argparse
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description="Port scanner sederhana")
parser.add_argument("target", help="IP atau hostname")
parser.add_argument("-p", "--ports", default="1-1024", help="contoh: 1-1000")
parser.add_argument("-t", "--threads", type=int, default=100)
args = parser.parse_args()

awal, akhir = map(int, args.ports.split("-"))

def cek_port(port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        if s.connect_ex((args.target, port)) == 0:
            try:
                nama = socket.getservbyport(port)
            except OSError:
                nama = "unknown"
            return (port, nama)
    finally:
        s.close()
    return None

def ambil_banner(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((args.target, port))
        if port in (80, 8000, 8080):
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        data = s.recv(200).decode(errors="ignore").strip()
        s.close()
        return data.splitlines()[0] if data else ""
    except Exception:
        return ""

with ThreadPoolExecutor(max_workers=args.threads) as pool:
    hasil = pool.map(cek_port, range(awal, akhir + 1))

for item in hasil:
    if item:
        banner = ambil_banner(item[0])
        print(f"Port {item[0]} terbuka ({item[1]}) {banner}")
