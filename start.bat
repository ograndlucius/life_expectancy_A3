@echo off

REM 
python -m venv .venv

REM 
call .\.venv\Scripts\activate

REM 
pip install --upgrade pip

REM 
pip install -r requirements.txt

echo Ambiente virtual criado e dependências instaladas.

REM E
python main.py

REM
deactivate

REM 
echo Ambiente virtual desativado.
echo Pressione qualquer tecla para fechar...
pause
