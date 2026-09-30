from http.server import BaseHTTPRequestHandler,HTTPServer
class http_logger(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"request from {self.client_address[0]} ")
        print(f"path: {self.path}")
        print(f"{self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"logged")
        
        
        
def start_logger():
    server=HTTPServer(("0.0.0.0",8080),http_logger)
    print("Starting http logger on 8080")
    server.serve_forever()