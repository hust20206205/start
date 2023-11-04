@echo off
setlocal
pause
set "sourcePath=C:\Users\vvn20206205\Desktop\BanDau"
set "destinationPath=C:\Users\vvn20206205\Desktop\nghia\src"
del /q "%destinationPath%\*.\*"
for /d %%i in ("%destinationPath%\*") do (
rmdir /s /q "%%i"
)
xcopy /s /i /y "%sourcePath%\*" "%destinationPath%"
cd /d "C:\Users\vvn20206205\Desktop\nghia\workspace"
code .\vvn20206205.code-workspace
endlocal
