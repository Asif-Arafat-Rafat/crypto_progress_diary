@echo off
if not exist "%USERPROFILE%\Documents\Binance-tracker" (
    git clone https://github.com/Asif-Arafat-Rafat/crypto_progress_diary.git "%USERPROFILE%\Documents\Binance-tracker"
)
cd "%USERPROFILE%\Documents\Binance-tracker"

if not exist env (
    echo creating env
    python -m venv env
    python -m pip install -r requirements.txt
) else (
    pip install --upgrade --no-deps --requirement requirements.txt
)
call env\Scripts\activate.bat
:noapi
set /p BINANCE_API_KEY=Enter your Binance API key:
if not defined BINANCE_API_KEY ( goto noapi )
:noapi_s
set /p BINANCE_API_SECRET=Enter your Binance API secret:
if not defined BINANCE_API_SECRET ( goto noapi_s )

echo BINANCE_API_KEY=%BINANCE_API_KEY%>.env
echo BINANCE_API_SECRET=%BINANCE_API_SECRET%>.env

python main.py

start /d "./sub" excel.exe "TradingData.xlsx"

pause 
