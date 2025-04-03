$TEST_DIR = ".\tests"
$APP_DIR = ".\app"
$COVERAGE_FILE = ".coverage"

Write-Host "Running Tests with pytest" -ForegroundColor Cyan

if ($args.Count -eq 0) {
    & $PYTEST_CMD --cov=$APP_DIR --cov-report=term-missing --tb=short $TEST_DIR
} else {
    & $PYTEST_CMD $args
}

if (Test-Path $COVERAGE_FILE) {
    Remove-Item $COVERAGE_FILE -Force
}

Write-Host "Tests Complete" -ForegroundColor Green