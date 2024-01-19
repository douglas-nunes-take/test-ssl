echo "Downloading Python 3.12.1"
bitsadmin.exe /transfer "PythonDownload" https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe %USERPROFILE%\Desktop\test-ssl\python-setup.exe

echo "Installing Python 3.12.1"
%USERPROFILE%\Desktop\test-ssl\python-setup.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Should install on each virtual environment or system wide?
echo "Installing pip-system-certs and truststore"
pip install pip-system-certs --index-url https://pypi.org/simple --trusted-host pypi.org --trusted-host files.pythonhosted.org

echo "Creating virtual environment"
python -m venv %USERPROFILE%\Desktop\test-ssl\venv

echo "Activating virtual environment"
%USERPROFILE%\Desktop\test-ssl\venv\Scripts\activate.bat
