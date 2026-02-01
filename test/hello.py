from http.server import HTTPServer, SimpleHTTPRequestHandler

# サーバーの設定
port = 8080
address = ('', port)


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # ブラウザに表示する内容
        self.wfile.write('<h1>Hello from Docker Container!</h1>'.encode())
        self.wfile.write('<p>WindowsとChromebookで同期成功！</p>'.encode())


print(f"Server starting at http://localhost:{port} ...")
httpd = HTTPServer(address, MyHandler)
httpd.serve_forever()
