Write-Host "Compiling Requirements" -ForegroundColor Yellow
pip-compile.exe .\requirements\requirements.in -o .\requirements\requirements.txt

Write-Host "Compiling Dev Requirements" -ForegroundColor Yellow
pip-compile.exe .\requirements\requirements-dev.in -o .\requirements\requirements-dev.txt

Write-Host "Compilation Complete ✅" -ForegroundColor Gree
