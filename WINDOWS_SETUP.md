# Build Logic API - Windows Setup Guide

## Installation Steps

### Step 1: Clone the Repository

Open PowerShell or Command Prompt and run:

```powershell
git clone https://github.com/partic10/BuildLogicAPI.git
cd BuildLogicAPI
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Run the API Server

```powershell
python main.py
```

You should see:
```
==================================================
Build Logic API - Windows Edition
==================================================
Starting server on http://127.0.0.1:5000
Grid Size: 16x16
==================================================
 * Running on http://127.0.0.1:5000
```

### Step 5: Test the API

Open a new PowerShell/Command Prompt window and test:

```powershell
# Health check
curl.exe -Uri "http://localhost:5000/health"

# Get grid
curl.exe -Uri "http://localhost:5000/grid"

# Set a cell
$body = @{value = 1} | ConvertTo-Json
curl.exe -Uri "http://localhost:5000/grid/cell/5/5" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body $body
```

## Windows Firewall

If you get a firewall warning, click "Allow" to allow the application through Windows Defender Firewall.

## Python Version Check

Make sure you have Python 3.9 or higher:

```powershell
python --version
```

## Troubleshooting

### "python" command not found

Install Python from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation.

### Port 5000 already in use

Find and kill the process:

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace 1234 with actual PID)
taskkill /PID 1234 /F
```

### ModuleNotFoundError

Make sure you're in the virtual environment and dependencies are installed:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Starting the Server on Windows Boot (Optional)

To run the API automatically on Windows startup:

1. Create a batch file `run_api.bat`:
```batch
@echo off
cd C:\Path\To\BuildLogicAPI
python main.py
pause
```

2. Create a shortcut to this batch file

3. Move the shortcut to `C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## Usage

Once the server is running, you can:

1. Access the API at `http://localhost:5000`
2. Use Python client: See `examples/client.py`
3. Use curl commands: See `DOCUMENTATION.md`
4. Access `/endpoints` for full endpoint list

## Next Steps

- Read [DOCUMENTATION.md](DOCUMENTATION.md) for complete API documentation
- Check [examples/README.md](examples/README.md) for code examples
- Review [examples/client.py](examples/client.py) for Python client usage

Enjoy using Build Logic API! 🚀
