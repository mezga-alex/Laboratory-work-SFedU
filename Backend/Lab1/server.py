#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class S(BaseHTTPRequestHandler):
    def _send_image_response(self, stat_code, image):
        self.send_response(stat_code)
        self.send_header("Content-type", "image")
        self.end_headers()
        self.wfile.write(image)

    def do_GET(self):
        try:
            path = self.path.split('img=')[1]
            image = open(f'./images/{path}', 'rb').read()
            code = 200
        except Exception:
            image = open(f'./images/404.jpeg', 'rb').read()
            code = 404

        self._send_image_response(code, image)
        logging.info(
            f"\nGET request\n"
            f"Status: {code}\n"
            f"PATH: {self.path}\n"
            f"IP: {self.client_address[0]}\n"
        )


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(filename='log.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting server...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping server...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
