import os
import shutil
import csv
import re
import xml.etree.ElementTree as ET

PASTA_ENTRADA = 'entrada'
PASTA_SAIDA = 'notas'
ARQUIVO_LOG = 'log_notas.csv'

os.makedirs(PASTA_SAIDA, exist_ok=True)

def extrair_dados_xml(caminho_xml):
    try:
        tree = ET.parse(caminho_xml)
        root = tree.getroot()
        ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

        emitente = root.find('.//nfe:emit', ns)
        cnpj = emitente.find('nfe:CNPJ', ns).text
        nome = emitente.find('nfe:xNome', ns).text.strip().replace('/', '-')
        ide = root.find('.//nfe:ide', ns)
        numero = ide.find('nfe:nNF', ns).text
        data_emissao = ide.find('nfe:dhEmi', ns).text if ide.find('nfe:dhEmi', ns) is not None else ''
        return {
            'cnpj': cnpj,
            'nome': nome,
            'numero': numero,
            'data': data_emissao[:10] if data_emissao else ''
        }
    except Exception as e:
        print(f"[ERRO] Falha ao processar {caminho_xml}: {e}")
        return None

def organizar_arquivos():
    log = []
    arquivos = os.listdir(PASTA_ENTRADA)
    for arquivo in arquivos:
        caminho = os.path.join(PASTA_ENTRADA, arquivo)

        if arquivo.lower().endswith('.xml'):
            dados = extrair_dados_xml(caminho)
            if not dados:
                continue
            pasta_destino = os.path.join(PASTA_SAIDA, f"{dados['cnpj']}_{dados['nome']}")
            os.makedirs(pasta_destino, exist_ok=True)
            novo_caminho = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho, novo_caminho)
            log.append([arquivo, dados['cnpj'], dados['nome'], dados['numero'], dados['data'], novo_caminho])

        elif arquivo.lower().endswith('.pdf'):
            # Tenta inferir CNPJ do nome do arquivo
            match = re.search(r'\d{14}', arquivo)
            cnpj = match.group(0) if match else 'desconhecido'
            nome = 'desconhecido'
            pasta_destino = os.path.join(PASTA_SAIDA, f"{cnpj}_{nome}")
            os.makedirs(pasta_destino, exist_ok=True)
            novo_caminho = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho, novo_caminho)
            log.append([arquivo, cnpj, nome, '-', '-', novo_caminho])

    # Gera log
    with open(ARQUIVO_LOG, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Arquivo', 'CNPJ', 'Razão Social', 'Nº NF', 'Data Emissão', 'Novo Caminho'])
        writer.writerows(log)

    print(f"\n[SUCCESSO] Organização concluída. Log salvo em: {ARQUIVO_LOG}")

if __name__ == '__main__':
    organizar_arquivos()