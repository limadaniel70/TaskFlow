$SRC = ".\app"

Write-Host "Running Black" -ForegroundColor Yellow
black.exe $SRC

Write-Host "Running Isort" -ForegroundColor Yellow
isort.exe --profile black $SRC

Write-Host "Running Pylint" -ForegroundColor Yellow
pylint.exe $SRC

Write-Host "Lint Complete ✅" -ForegroundColor Gree
