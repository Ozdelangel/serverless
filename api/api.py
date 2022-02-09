from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        if 'name' in dic:
            url = 'https://pokeapi.co/api/v2/pokemon/'
            r = requests.get(url + dic['name'])
            data = r.json()
            poke_mon = []
            for poke_data in data:
                pocket_mon = poke_data['results'][0]
                poke_mon.append(pocket_mon)

            message = str(poke_mon)
        else:
            message = 'please type in a pokemon to get url'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
    # def do_GET(self):
    #     url
    #     url = 'https://pokeapi.co/api/v2/pokemon/'
    #     r = requests.get(url)
    #     data = r.json()
# print(data)

# def_list = data
# poke_mon = data['results'][0]
# print(str(poke_mon))