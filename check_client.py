import http.server
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler

class CheckClientHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Determine if the connection is encrypted (HTTPS/443) or unencrypted (HTTP/80)
        # If the connection socket is wrapped in SSL, it is secured.
        is_secure = isinstance(self.connection, ssl.SSLSocket)
        
        protocol = "HTTPS" if is_secure else "HTTP"
        port = 443 if is_secure else 80
        security_status = "Encrypted (Secure)" if is_secure else "Unencrypted (Insecure)"
        
        # Retrieve client browser/OS info from the User-Agent header
        user_agent = self.headers.get('User-Agent', 'Unknown Browser')
        client_ip = self.client_address[0]

        # Output detailed logs to the server console
        print("\n" + "=" * 50)
        print(f"📥 New Connection from: {client_ip}")
        print(f"🌐 Protocol: {protocol}")
        print(f"🔌 Port: {port}")
        print(f"🔒 Security Status: {security_status}")
        print(f"💻 Client Browser / User-Agent: {user_agent}")
        print("=" * 50 + "\n")

        # Send HTTP response back to the client browser
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        response_html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>Connection Inspector</title>
            </head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1 style="color: {'green' if is_secure else 'orange'};">Connection Analysis Complete</h1>
                <p><b>Protocol:</b> {protocol}</p>
                <p><b>Port:</b> {port}</p>
                <p><b>Security:</b> {security_status}</p>
                <p><b>Your Browser (User-Agent):</b> {user_agent}</p>
            </body>
        </html>
        """
        self.wfile.write(response_html.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=CheckClientHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Server running on port {port}. Open http://localhost in your browser.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("🛑 Server stopped.")

if __name__ == '__main__':
    # Note: Running on standard port 80 may require administrative privileges (sudo).
    # Change port to 8080 or 5000 for standard user testing.
    run(port=80)