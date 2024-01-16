import certifi
import httpx

URL = "https://httpbin.org/get"

if __name__ == "__main__":
    # Not sure if httpx use this certificate
    certificates_path = certifi.where()
    print(f"Loaded certificates: {certificates_path}")

    print("\n\n#######################\n")
    with httpx.Client() as client:
        response = client.get(URL)
        try:
            response.raise_for_status()
        except Exception as e:
            print(f"Request failed: {e}")
            print("For requests to succeed, you must set the SSL_CERT_FILE "
                  "and/or the SSL_CERT_DIR environment variable.")
            raise e
        print("Test Passed!")
