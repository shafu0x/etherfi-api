from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # Get the parameter from the URL
    param = request.args.get('param')
    
    # Check if the parameter was provided
    if param:
        response = {'message': f'You sent: {param}'}
    else:
        response = {'error': 'No parameter provided'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
