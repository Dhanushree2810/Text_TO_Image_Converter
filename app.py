import http.server
import webbrowser
import json
from core.api import generate
from core.safety import safe
def load_html():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(load_html().encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data   = json.loads(self.rfile.read(length))

        key    = data.get("key","").strip()
        prompt = data.get("prompt","").strip()
        neg    = data.get("neg","").strip()

        if not key or not prompt:
            return self._send({"error":"Missing token or prompt"})
        if not key.startswith("hf_"):
            return self._send({"error":"Token must start with hf_"})
        if not safe(prompt):
            return self._send({"error":"🚫 Blocked by NSFW filter!"})

        import os
        img, result = generate(os.environ.get("HF_TOKEN"), prompt, neg)

        if img:
            self._send({"image": img, "model": result})
        else:
            self._send({"error": result})

    def _send(self, obj):
        body = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.send_header("Content-Length",len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a): pass


if __name__ == "__main__":
    import os
    PORT = int(os.environ.get("PORT", 8080))
    print(f"Open: http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    http.server.HTTPServer(("", PORT), Handler).serve_forever()