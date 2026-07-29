"""Multi-threaded HTTP server that sends no-cache headers for every file."""
import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/index-pro.html"
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def address_string(self):
        # Override to prevent extremely slow reverse DNS lookups on Windows
        return self.client_address[0]

    def log_message(self, format, *args):
        print(f"[Server] {self.address_string()} - {format % args}")

if __name__ == "__main__":
    with ThreadingHTTPServer(("", PORT), NoCacheHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}  (multi-threaded, no-cache mode)")
        httpd.serve_forever()
