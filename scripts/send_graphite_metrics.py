import argparse
import random
import socket
import time
from urllib.request import urlopen


def http_available(url):
    try:
        with urlopen(url, timeout=3) as response:
            return 1 if 200 <= response.status < 400 else 0
    except Exception:
        return 0


def send_metric(host, port, name, value, timestamp):
    message = f"{name} {value} {timestamp}\n".encode("utf-8")
    with socket.create_connection((host, port), timeout=3) as sock:
        sock.sendall(message)


def main():
    parser = argparse.ArgumentParser(description="Send ABC Technologies sample metrics to Graphite.")
    parser.add_argument("--target-url", default="http://localhost:8080")
    parser.add_argument("--graphite-host", default="localhost")
    parser.add_argument("--graphite-port", type=int, default=2003)
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--interval", type=float, default=5.0)
    args = parser.parse_args()

    start = int(time.time())
    for index in range(args.count):
        now = int(time.time())
        available = http_available(args.target_url)
        uptime = now - start
        values = {
            "servers.abc.cpu.total": round(random.uniform(18, 62), 2),
            "servers.abc.memory.used": random.randint(180_000_000, 520_000_000),
            "servers.abc.network.rx": random.randint(24_000, 92_000),
            "servers.abc.network.tx": random.randint(18_000, 88_000),
            "website.abc.http.available": available,
            "website.abc.uptime.seconds": uptime,
        }

        for name, value in values.items():
            send_metric(args.graphite_host, args.graphite_port, name, value, now)

        print(f"sent metric batch {index + 1}/{args.count} at {now}")
        if index < args.count - 1:
            time.sleep(args.interval)


if __name__ == "__main__":
    main()
