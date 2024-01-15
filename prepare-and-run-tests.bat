
echo "Downloading Python 3.12.1"
bitsadmin.exe /transfer "PythonDownload" https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe %USERPROFILE%\Desktop\test-ssl\python-setup.exe

echo "Installing Python 3.12.1"
%USERPROFILE%\Desktop\test-ssl\python-setup.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo "Creating virtual environment"
python -m venv %USERPROFILE%\Desktop\test-ssl\venv

echo "Activating virtual environment"
%USERPROFILE%\Desktop\test-ssl\venv\Scripts\activate.bat

echo "Installing dependencies"
pip install -r %USERPROFILE%\Desktop\test-ssl\requirements.txt

echo "Running httpx test"
python %USERPROFILE%\Desktop\test-ssl\simple-httpx-test/run-get-httpx.py

echo "Running requests test"
python %USERPROFILE%\Desktop\test-ssl\simple-requests-test/run-get-requests.py

pause
