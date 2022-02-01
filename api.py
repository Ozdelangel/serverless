from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components)
        dic = dict(query_string_list)

        if 'name' in dic:
            url = 'https://pokeapi.co/api/v2/pokemon/'
            r = requests.get(url + dic['name'])
            data = r.json()
            poke_mon = []
            for poke_data in data:
                moves = poke_data['moves'][0]['move'][0]['name']
                poke_mon.append(moves)
            message = str(poke_mon)
        else:
            message = ' please type a pokemon to see their moves'
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())



        return