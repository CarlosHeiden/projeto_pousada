@echo off
setlocal enabledelayedexpansion

rem Definir caminho para ambiente virtual
set "VENV_PATH =G:\CARLOS\django\projeto_pousada\.venv"
rem Ativar ambiente virtual
call %VENV_PATH%

rem Iniciar Django
py manage.py runserver

endlocal
