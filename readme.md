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

- Check if the python-certifi-win32 and truststore packages were installed.
- Check if the use-feature = truststore was added to the pip.ini file.
- Check if you have the REQUESTS_CA_BUNDLE environment variable set to the right path of the certificate file.
- Check if you have the SSL_CERT_FILE environment variable set to the right path of the certificate file.
- Check if the right certificate were loaded by the scripts.
- Check if the gcloud config was set to the right path of the certificate file.

## Other problems

Instaling the [GCloud CLI](https://cloud.google.com/sdk/docs/install?hl=pt-br) and trying to authenticate raises the SSL
error.

## Fixing Problems

1. Run `pip install python-certifi-win32 truststore --index-url https://pypi.org/ --trusted-host pypi.org --trusted-host files.pythonhosted.org`
2. Add `use-feature = truststore` to the pip.ini file
3. Configure the REQUESTS_CA_BUNDLE environment variable to the right path of the certificate file.
4. Configure the SSL_CERT_FILE environment variable to the right path of the certificate file.
5. Configure gcloud (after
   installed) `gcloud config set core/custom_ca_certs_file “%ProgramData%\Netskope\STAgent\data\nscacert.pem”`

More information about the problem can be
found [here](https://docs.netskope.com/en/netskope-help/data-security/netskope-secure-web-gateway/configuring-cli-based-tools-and-development-frameworks-to-work-with-netskope-ssl-interception/#configuring-cli-based-tools-and-development-frameworks-to-work-with-netskope-ssl-interception).