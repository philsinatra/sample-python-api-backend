"""
Python API backend
Serverless function hosted on Vercel
"""
from http.server import BaseHTTPRequestHandler
from typing import Any
import random


def generate_random_number():
    return random.randint(0, 100)


class handler(BaseHTTPRequestHandler):
    """Primary handler"""

    def do_GET(self: Any) -> None:
        """@returns a simple string"""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.end_headers()
        num = generate_random_number()
        self.wfile.write(b"Hello, world! " + str(num).encode())
