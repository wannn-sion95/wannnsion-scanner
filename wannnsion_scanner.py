import socket, argparse
from concurrent.futures import ThreadPoolExecutor

CYAN = "\033[96m"
HIJAU = "\033[92m"
RESET = "\033[0m"

BANNER = CYAN + r"""
 _       __                    _____ _
| |     / /___ _____  ____     / ___/(_)___  ____
| | /| / / __ `/ __ \/ __ \    \__ \/ / __ \/ __ \
| |/ |/ / /_/ / / / / / / /   ___/ / / /_/ / / / /
|__/|__/\__,_/_/ /_/_/ /_/   /____/_/\____/_/ /_/

        WannnSion Scanner v1.0 | by Wannn Sion
        github.com/wannn-sion95/wannnsion-scanner
""" + RESET

print(BANNER)

parser = argparse.ArgumentParser(description="WannnSion Scanner - port scanner sederhana")
parser.add_argument("target", help="IP atau hostname")
parser.add_argument("-p", "--ports", default="1-1024", help="contoh: 1-1000")
parser.add_argument("-t", "--threads", type=int, default=100)
parser.add_argument("-V", "--version", action="version", version="WannnSion Scanner v1.0 by Wannn Sion")
args = parser.parse_args()

awal, akhir = map(int, args.ports.split("-"))


def cek_port(port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        if s.connect_ex((args.target, port)) != 0:
            return None

        try:
            nama = socket.getservbyport(port)
        except OSError:
            nama = "unknown"

        banner = ""
        try:
            if port in (80, 8000, 8080):
                s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            s.settimeout(1)
            data = s.recv(200).decode(errors="ignore").strip()
            banner = data.splitlines()[0] if data else ""
        except Exception:
            pass

        return (port, nama, banner)
    finally:
        s.close()


with ThreadPoolExecutor(max_workers=args.threads) as pool:
    hasil = pool.map(cek_port, range(awal, akhir + 1))

for item in hasil:
    if item:
        port, nama, banner = item
        print(f"{HIJAU}[OPEN]{RESET} Port {port:<6} {nama:<12} {banner}")
