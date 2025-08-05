# 🧾 Organizador de Notas Fiscais (XML e PDF)

Script em Python para automatizar a organização de Notas Fiscais eletrônicas (NFe) em XML e PDF. Ideal para empresas ou pessoas que recebem notas por e-mail ou download.

---

## 💡 Objetivo

- Ler uma pasta com arquivos de NFe (XML e/ou PDF)
- Extrair dados como CNPJ, razão social, data e número da nota
- Criar pastas automaticamente com base no CNPJ e nome da empresa
- Mover os arquivos para as pastas corretas
- Gerar um log CSV com os dados extraídos

---

## ✅ Funcionalidades

- Organização automática com base no conteúdo do XML
- Suporte a NFe modelo nacional e PDFs com nomes padronizados
- Geração de log `log_notas.csv` com:
  - CNPJ
  - Razão social
  - Número da nota
  - Caminho original e novo
- Estrutura gerada:

  
notas/
├── 12345678000195_MercadoXYZ/
│ ├── NF123456.xml
│ ├── NF123456.pdf
├── 98765432000100_ConstrutoraABC/


---

## 🧠 Tecnologias utilizadas

- `xml.etree.ElementTree` ou `lxml` – leitura e parsing de XML
- `os`, `re`, `shutil` – manipulação de arquivos e pastas
- `csv` – geração do log em CSV

---

## 📁 Estrutura do Projeto



organizador_nf/
├── organizar_notas.py
├── entrada/
│ ├── NF1234.pdf
│ ├── 35220512345678000195550010012345671123456789.xml
├── notas/
├── log_notas.csv



---

## ▶️ Como usar

1. Coloque os arquivos XML e PDF na pasta `entrada/`
2. Execute o script:
```bash
python organizar_notas.py
Os arquivos serão movidos automaticamente para notas/ em subpastas organizadas por empresa, e o log será salvo em log_notas.csv.


## 🧾 NFe Organizer (XML and PDF) — English Version

Python script to automate the organization of Brazilian electronic invoices (NFe) in XML and PDF formats. Ideal for accounting, finance, or personal use.

---

# 💡 Purpose
Scan a folder containing NFe files (XML and/or PDF)

Extract key data: CNPJ, company name, invoice number and date

Create subfolders by CNPJ and company name

Move related files to the correct folder

Generate a log_notas.csv with the extracted data

---

# ✅ Features
Automatic sorting based on XML contents

Supports NFe XML (Brazilian standard) and standardized PDF filenames

Log file includes:

CNPJ

Company name

Invoice number

Old and new file paths

Folder structure:

notas/
├── 12345678000195_MarketplaceXYZ/
│   ├── NF123456.xml
│   ├── NF123456.pdf
├── 98765432000100_CompanyABC/

---

# 🧠 Tech Stack
xml.etree.ElementTree or lxml – for XML parsing

os, re, shutil – for filesystem manipulation

csv – to generate the invoice log

# 📁 Project Structure
 
organizador_nf/
├── organizar_notas.py
├── entrada/
│   ├── NF1234.pdf
│   ├── 35220512345678000195550010012345671123456789.xml
├── notas/
├── log_notas.csv

# ▶️ How to Use
Place your XML and PDF invoice files inside the entrada/ folder

Run the script:

python organizar_notas.py
Files will be automatically moved to notas/ and logged into log_notas.csv.

---

# 👤 Author
Rodrigo Assarice


📧 rodrigo.assarice@hotmail.com
