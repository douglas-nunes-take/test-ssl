# Simple tests to validade SSL certificates

# Basic test

1. Clone this repository to the desktop
2. Open the terminal as admin
3. Navigate to the folder where the repository was cloned
4. Run the command: `prepare-enviroment.bat`
5. Run the command: `pip install -r requirements.txt`
6. Run the first test: `python simple-requests-test\run-get-requests.py`
7. Run the second test: `python simple-httpx-test\run-get-httpx.py`

If the tests run without errors, the SSL certificates are working properly.
If the tests fail check the print messages:

- Check if you have the REQUESTS_CA_BUNDLE environment variable set to the right path of the certificate file.
- Check if the right certificate were loaded by the scripts.

# Other problems

Instaling the [GCloud CLI](https://cloud.google.com/sdk/docs/install?hl=pt-br) and trying to authenticate raises the SSL
error.