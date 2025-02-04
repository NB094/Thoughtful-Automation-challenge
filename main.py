from flask import Flask, request, jsonify

app = Flask(__name__)

def sort(width: int, height: int, length: int, mass: int):
    """
    A function to calculate the appropriate stack in which a package should be placed.

    --Inputs--
        width: how wide the package is, in centimeters (integer)
        height: how high the package is, in centimeters (integer)
        length: how long the package is, in centimeters (integer)
        mass: how heavy the package is, in kg (integer)

    --Outputs--
        stackName: the name of the final stack where the package should be placed (string)
    """
    
    # Calculate volume
    volume = width * height * length

    # Allocate to proper stack based on certain criteria.
    
    # Rejected check based on mass and volume
    if volume >= 1000000 or any(value >= 150 for value in [width, height, length]):
        if mass >= 20:
            stackName = 'REJECTED'
        else:
            stackName = 'SPECIAL'
    
    # Special if volume < 1000000 and mass >= 20
    elif mass >= 20:
        stackName = 'SPECIAL'
    
    # Otherwise, neither bulky nor heavy
    else:
        stackName = 'STANDARD'

    return stackName

@app.route('/sort', methods=['GET'])
def sort_package():
    # Get query parameters from the URL
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    length = int(request.args.get('length'))
    mass = int(request.args.get('mass'))

    # Call the sort function
    stack_name = sort(width, height, length, mass)

    # Return the result as JSON
    return jsonify({
        "stackName": stack_name
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)