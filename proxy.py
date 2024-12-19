from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    target_url = request.args.get('url')  # URL para redirecionar
    if not target_url:
        return "Por favor, forneça a URL como parâmetro 'url'.", 400

    try:
        if request.method == 'GET':
            resp = requests.get(target_url, headers=request.headers)
        elif request.method == 'POST':
            resp = requests.post(target_url, data=request.data, headers=request.headers)

        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except Exception as e:
        return f"Erro ao acessar {target_url}: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

