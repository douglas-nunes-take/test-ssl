# Simple tests to validade SSL certificates

## Basic tests

1. Clone this repository to the desktop
2. Open the terminal as admin
3. Navigate to the folder where the repository was cloned
4. Run the command: `prepare-enviroment.bat`
5. Configure the private nexus repository in the pip.ini
6. Run the command: `pip install -r requirements.txt`
7. Run the first test: `python simple-requests-test\run-get-requests.py`
8. Run the second test: `python simple-httpx-test\run-get-httpx.py`

If the tests run without errors, the SSL certificates are working properly.
If the tests fail check the print messages:

- Check if the `pip-system-certs` package is installed.
- Check if the `use-feature = truststore` was added to the pip.ini file.
- Check if you have the `REQUESTS_CA_BUNDLE` environment variable set to the right path of the certificate file.
- Check if you have the `SSL_CERT_FILE` environment variable set to the right path of the certificate file.
- Check if the right certificate were loaded by the scripts.

## Fixing Problems

1. Make sure to have the `REQUESTS_CA_BUNDLE` and `SSL_CERT_FILE` environment variables set to the right path of the certificate file (it should be `%ProgramData%\Netskope\STAgent\data\nscacert.pem`).
2. Install the `pip-system-certs` package in the python of the Windows machine running as admin the command `pip install pip-system-certs --index-url https://pypi.org/simple --trusted-host pypi.org --trusted-host files.pythonhosted.org`.
   - Depending on your enviroment config you could need to install `pip-system-certs` the package in each virtual enviroment.
3. Make sure to have the `trusted-host = nexus.stilingue.com.br` config in the pip.ini file.
4. Configure [GCloud CLI](https://cloud.google.com/sdk/docs/install) after installed) `gcloud config set core/custom_ca_certs_file "%ProgramData%\Netskope\STAgent\data\nscacert.pem"`

More information about the problem can be found [here](https://docs.netskope.com/en/netskope-help/data-security/netskope-secure-web-gateway/configuring-cli-based-tools-and-development-frameworks-to-work-with-netskope-ssl-interception/#configuring-cli-based-tools-and-development-frameworks-to-work-with-netskope-ssl-interception).
