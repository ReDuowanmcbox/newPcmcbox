@echo off

rem -------------------------------------------------
rem           Reduowanmcbox Windows Beta
rem           Ver:1.0.0     Libver: 0.0.1
rem           2022/11/22
rem -------------------------------------------------

:main

cls
goto check
goto regapi
goto startmc
exit
cls

:check

cls
python3 checkPath.py 2>nul
python checkPath.py 2>nul
python3 checkNetwork.py 2>nul
python checkNetwork.py 2>nul
cls

:regapi

cls
reg import regapi.reg
cls

:startmc
python3 load.py 2>nul
python load.py 2>nul
