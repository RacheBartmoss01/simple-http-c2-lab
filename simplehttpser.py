import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Serve files from the current directory on localhost:8080
# This is useful for local learning, testing, and lab environments.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
