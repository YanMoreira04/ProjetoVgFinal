from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Conectar ao banco 
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cashback_db"
    )
    return conn


# Regras
def calcular_cashback(tp_cliente, valor, desconto):
    tp_cliente = tp_cliente.strip().lower()

    valor_final = valor * (1 - desconto / 100)

    # Cashback base (5%)
    cashback = valor_final * 0.05

    # Bônus VIP
    if tp_cliente == "vip":
        cashback *= 1.10

    # Se valor > 500
    if valor_final > 500:
        cashback *= 2

    return valor_final,cashback

# Criando cashback
@app.route('/cashback', methods=['POST'])
def create_cashback():
    data = request.get_json()

    tp_cliente = data.get('tp_cliente')
    valor = data.get('valor')
    desconto = data.get('desconto', 0)

    if not tp_cliente or valor is None:
        return jsonify({"erro": "Dados inválidos"}), 400

    valor_final, cashback = calcular_cashback(
        tp_cliente, float(valor), float(desconto)
    )

    # Salvar no banco
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO cashback (tp_cliente, valor, cashback) VALUES (%s, %s, %s)",
            (tp_cliente, valor_final, cashback)
        )

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    return jsonify({
        "tipo_cliente": tp_cliente,
        "valor": valor,
        "valor_final": valor_final,
        "cashback": cashback
    }), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)