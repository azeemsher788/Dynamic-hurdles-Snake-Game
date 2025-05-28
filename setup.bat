@echo off
echo Setting up dependencies for Snake Game...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo Tkinter is not available in your Python installation.
    echo Please reinstall Python and make sure to check the option to install tcl/tk and IDLE during installation.
    echo See README.md for more information.
    pause
    exit /b 1
)

REM Install Python package dependencies
echo Installing Python package dependencies...
pip install -r requirements.txt

echo Setup complete! You should now be able to run the Snake Game.
pause