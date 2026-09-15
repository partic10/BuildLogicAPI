"""
Logic Routes - API endpoints for logic gate operations
REST endpoints for all logic gate operations
"""

from flask import Blueprint, request, jsonify
from core.logic_gates import LogicGates, TruthTable

logic_bp = Blueprint('logic', __name__)

@logic_bp.route('/and', methods=['POST'])
def logic_and():
    """AND gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('AND', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'AND',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/or', methods=['POST'])
def logic_or():
    """OR gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('OR', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'OR',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/not', methods=['POST'])
def logic_not():
    """NOT gate operation"""
    data = request.get_json()
    
    if not data or 'input' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "input" in request body'
        }), 400
    
    input_val = data['input']
    result = LogicGates.analyze_operation('NOT', [input_val])
    
    return jsonify({
        'status': 'success',
        'operation': 'NOT',
        'input': input_val,
        'output': result['output']
    }), 200

@logic_bp.route('/xor', methods=['POST'])
def logic_xor():
    """XOR gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('XOR', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'XOR',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/nand', methods=['POST'])
def logic_nand():
    """NAND gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('NAND', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'NAND',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/nor', methods=['POST'])
def logic_nor():
    """NOR gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('NOR', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'NOR',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/xnor', methods=['POST'])
def logic_xnor():
    """XNOR gate operation"""
    data = request.get_json()
    
    if not data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "inputs" in request body'
        }), 400
    
    inputs = data['inputs']
    if not isinstance(inputs, list) or len(inputs) < 2:
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list with at least 2 values'
        }), 400
    
    result = LogicGates.analyze_operation('XNOR', inputs)
    
    return jsonify({
        'status': 'success',
        'operation': 'XNOR',
        'inputs': inputs,
        'output': result['output']
    }), 200

@logic_bp.route('/buffer', methods=['POST'])
def logic_buffer():
    """Buffer gate operation"""
    data = request.get_json()
    
    if not data or 'input' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "input" in request body'
        }), 400
    
    input_val = data['input']
    result = LogicGates.analyze_operation('BUFFER', [input_val])
    
    return jsonify({
        'status': 'success',
        'operation': 'BUFFER',
        'input': input_val,
        'output': result['output']
    }), 200

@logic_bp.route('/truth-table/<operation>', methods=['GET'])
def get_truth_table(operation):
    """Get truth table for a logic operation"""
    operation = operation.upper()
    
    # Get number of inputs from query parameter (default: 2)
    num_inputs = request.args.get('inputs', 2, type=int)
    
    if num_inputs < 1 or num_inputs > 8:
        return jsonify({
            'status': 'error',
            'message': 'inputs parameter must be between 1 and 8'
        }), 400
    
    # Special case: NOT only takes 1 input
    if operation == 'NOT':
        num_inputs = 1
    
    if operation == 'AND':
        table = TruthTable.generate_and(num_inputs)
    elif operation == 'OR':
        table = TruthTable.generate_or(num_inputs)
    elif operation == 'XOR':
        table = TruthTable.generate_xor(num_inputs)
    elif operation == 'NOT':
        table = TruthTable.generate_and(1)  # Simplified for NOT
    else:
        return jsonify({
            'status': 'error',
            'message': f'No truth table available for operation: {operation}'
        }), 400
    
    if not table:
        return jsonify({
            'status': 'error',
            'message': f'Failed to generate truth table'
        }), 400
    
    return jsonify({
        'status': 'success',
        'operation': operation,
        'inputs': num_inputs,
        'truth_table': table
    }), 200

@logic_bp.route('/analyze', methods=['POST'])
def analyze_operation():
    """Analyze any logic operation"""
    data = request.get_json()
    
    if not data or 'operation' not in data or 'inputs' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "operation" or "inputs" in request body'
        }), 400
    
    operation = data['operation']
    inputs = data['inputs']
    
    if not isinstance(inputs, list):
        return jsonify({
            'status': 'error',
            'message': 'inputs must be a list'
        }), 400
    
    result = LogicGates.analyze_operation(operation, inputs)
    
    if not result.get('success', False):
        return jsonify({
            'status': 'error',
            'message': result.get('error', 'Operation failed')
        }), 400
    
    return jsonify({
        'status': 'success',
        'operation': result['operation'],
        'inputs': result['inputs'],
        'output': result['output']
    }), 200
