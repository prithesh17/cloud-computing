from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_even_numbers():
    n = request.args.get('n', default=10, type=int)  # Default to 10 if not specified
    even_numbers = [i for i in range(0, n * 3, 3)]  # Generate n even numbers
    return jsonify(even_numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
