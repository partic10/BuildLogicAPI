# Build Logic API - Usage Examples

This directory contains example code for using the Build Logic API.

## Contents

- **client.py** - Python client library for interacting with the API

## Quick Examples

### Python Client

```python
from examples.client import BuildLogicClient

client = BuildLogicClient()

# Get grid
grid = client.get_grid()

# Set cell
client.set_cell(5, 5, 1)

# Logic operations
result = client.and_gate([1, 1])
print(result['output'])  # Output: 1
```

### Using curl

```bash
# Health check
curl http://localhost:5000/health

# Get grid
curl http://localhost:5000/grid

# Set cell
curl -X POST http://localhost:5000/grid/cell/5/5 \
  -H "Content-Type: application/json" \
  -d '{"value": 1}'

# Logic operation
curl -X POST http://localhost:5000/logic/and \
  -H "Content-Type: application/json" \
  -d '{"inputs": [1, 1]}'
```

### JavaScript/Node.js Example

```javascript
const fetch = require('node-fetch');

// Set cell
fetch('http://localhost:5000/grid/cell/5/5', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ value: 1 })
})
.then(res => res.json())
.then(data => console.log(data));

// AND gate
fetch('http://localhost:5000/logic/and', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ inputs: [1, 1] })
})
.then(res => res.json())
.then(data => console.log(`AND(1, 1) = ${data.output}`));
```

## Running Examples

### Python Client Example

```bash
# Make sure the API is running
python main.py

# In another terminal, run the example
cd examples
python client.py
```

This will output:
```
Building Logic API - Client Example
========================================

Testing API Health...
Status: healthy

Getting Grid State...
Grid size: 16x16
Active cells: 0

Setting cell (5, 5) to 1...
Result: Cell (5, 5) set to 1

Testing Logic Gates...
AND(1, 1) = 1
OR(0, 1) = 1
XOR(1, 0) = 1
```

## More Information

See [DOCUMENTATION.md](../DOCUMENTATION.md) for complete API documentation.
