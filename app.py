from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Atividade Final - ADS</title></head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>Wanderson Sousa - Portfólio ADS</h1>
            <p>Aplicação Containerizada com Docker para a Atividade Final.</p>
            <div style="background: #f4f4f4; padding: 20px; display: inline-block; border-radius: 10px;">
                <strong>Status:</strong> Online e Rodando em Nuvem (Simulação)
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)