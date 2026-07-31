@echo off

echo ============================================
echo ApexPlanet Automation Pipeline
echo ============================================

cd /d "%~dp0"

python run_pipeline.py

echo.
echo Pipeline Finished Successfully.
pause