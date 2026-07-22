# Client-Connection-Browser-Inspector-HTTP-80-vs-HTTPS-443
Actual browser Inspector
Description:
A lightweight Python HTTP server designed to inspect incoming client connections. It identifies whether the client is connecting via an unencrypted channel (HTTP on Port 80) or an encrypted channel (HTTPS on Port 443), extracts the client's User-Agent (browser and OS details), and logs the session information along with rendering an HTML summary report back to the user.
# Client Connection Inspector

A simple and lightweight diagnostic tool built in Python to inspect client connection protocols (HTTP/80 vs HTTPS/443) and parse `User-Agent` headers.

## Features
* Detects encryption status (`Encrypted` vs `Unencrypted`).
* Identifies the target port (`80` for HTTP, `443` for HTTPS).
* Extracts and logs the client's IP address and browser `User-Agent`.
* Serves a clean HTML report directly back to the requesting browser.

## Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/client-connection-inspector.git](https://github.com/your-username/client-connection-inspector.git)
   cd client-connection-inspector
