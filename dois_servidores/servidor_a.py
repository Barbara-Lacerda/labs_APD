
import json
from datetime import datetime

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer #para trabalhar com http
from pathlib import Path 

from urllib import error, request

PASTA =Path(__file__).resolve().parent
ARQUIVO_REGISTRO = PASTA / "registro.json"
ARQUIVO_PAGINA = PASTA /"dois_servidores_pasta.html"
HOST = "127.0.0.1"
PORTA = 5000
NOME_B = "servidor_b"
TIMEOUT_SEGUNDOS = 0.8
relogio = 0 #relógio lógico do servidor A
pedidos = {} #{"valor": 12.0, "nome":1}

def hora_parede(): #identifica o relógio físico
    return datetime.now().strftime("%H:%M:%S")

def resolver(nome):
    with ARQUIVO_REGISTRO.open(encoding="utf-8-sig") as arquivo:
        tabela = json.load(arquivo)

    ficha = tabela[nome]
    return ficha["id"], ficha["host"], int(ficha["porta"])

def pedir_autorizacao(pedido, valor, L, host, port):   #bate no servidor_b e pede autorização do valor limite do pedido
    url = f"http://{host}:{port}/autorizar"   #como vou fazer a requisiçãp
    corpo = json.dumps({"pedido": pedido, "valor":valor, "L": L},
                       ensure_ascii=False   #smanter acentuações
                       ).encode("utf-8")

    requisicao = request.Request(
        url, data=corpo,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with request.urlopen(requisicao, timeout=TIMEOUT_SEGUNDOS) as resposta:  #aqui realmente fazer a requisiçãp
            return json.loads(resposta.read().decode("utf-8")), None  #retornar a resposta se foi aprovado ou não (responsabilidade do servidor_b)
    except error.URLError as falha:
        return None, falha.reason

class Tratador(BaseHTTPRequestHandler):
    def enviar_json(self, codigo, obj): #tratamentos de que tipos de envio e retorno ao clicar na página
        dados = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Lenght", str(len(dados)))
        self.end_headers()
        self.wfile.write(dados)

    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return

        html = ARQUIVO_PAGINA.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; chartset=utf-8")
        self.send_header("Content-Lenght", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def do_POST(self): #basicamente é o que vai executar o pagamento
        global relogio  #relógio de lamport
        if self.path != "/pedido":
            self.send_error(404)
            return 

        tamanho = int(self.headers.get("Content-Lenght", "0"))
        entrada = json.loads(self.rfile.read(tamanho).decode("utf-8"))
        valor = float(entrada["valor"])

        relogio += 1 #controlar a ordem das threads, assim cada requisição aumenta o relógio lógico
        L_registro = relogio

        numero = f"PED-{len(pedidos) + 1:04d}" #0001 completa com 0 até completar 4 dígitos 
    

