@echo off
echo 🔧 Setting up Deep Research Clone Streamlit App
echo ================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found:
python --version

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    echo 🔑 Creating .env file...
    echo OPENAI_API_KEY=your_openai_api_key_here > .env
    echo ⚠️ Please update the .env file with your actual OpenAI API key
) else (
    echo ✅ .env file already exists
)

echo.
echo 🎉 Setup complete!
echo ==================
echo.
echo Next steps:
echo 1. Update the .env file with your OpenAI API key
echo 2. Activate the virtual environment: venv\Scripts\activate.bat
echo 3. Run the app: streamlit run app.py
echo.
echo Happy researching! 🔍
pause 