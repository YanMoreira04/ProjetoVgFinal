# Sistema de Cashback

Este projeto é uma aplicação full stack desenvolvida em Python + Flask + MySQL + HTML/CSS/JavaScript puro, que simula um sistema de cashback baseado em regras de negócio de uma fintech.

---

 # Tecnologias utilizadas

 ## Backend:
- Python 3
- Flask
- Flask-CORS
- MySQL Connector

 ## Frontend:
- HTML5
- CSS3
- JavaScript (Vanilla JS)

 ## Banco de Dados
- MySQL

---

# Funcionalidades

- Cálculo de cashback baseado em regras de negócio
- Aplicação de desconto no valor da compra
- Identificação de cliente VIP
- Bônus adicional para clientes VIP
- Promoção de cashback dobrado para compras acima de R$ 500
- Persistência dos dados no banco MySQL
- Interface web simples para interação do usuário

---

# Regras de negócio implementadas:

## 1. Cashback base
- 5% sobre o valor final da compra (após desconto)

## 2. Cliente VIP
- Recebe 10% de bônus sobre o cashback base

## 3. Promoção especial
- Compras acima de R$ 500 recebem cashback dobrado (incluindo VIPs)


valor_final = valor - (valor * desconto / 100)

cashback = valor_final * 0.05

if VIP:
    cashback = cashback * 1.10

if valor_final > 500:
    cashback = cashback * 2

---

# Como funciona o sistema:

1. O usuário preenche:
   - tipo de cliente (vip ou normal)
   - valor da compra
   - percentual de desconto

2. O frontend envia os dados para a API Flask

3. O backend:
   - calcula o valor final com desconto
   - calcula o cashback seguindo as regras
   - salva os dados no banco MySQL

4. O frontend exibe o resultado na tela

---



# Como Rodar o Projeto?

## E necessário ter instalado:
- Python 3.8+
- MySQL Server
- pip (gerenciador de pacotes do Python)

## Clonar o repositório:
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd Backend
python apii.py

## Se precisar ajuste os dados de conexão:
host="localhost",
user="root",
password="",
database="cashback_db"






