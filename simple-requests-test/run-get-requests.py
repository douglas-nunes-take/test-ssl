import certifi
import requests

URL = "https://httpbin.org/get"

if __name__ == "__main__":
    certificates_path = certifi.where()
    print(f"Loaded certificates: {certificates_path}")

    print("\n\n#######################\n")
    response = requests.get(URL)
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        print("For requests to succeed, you must set the REQUESTS_CA_BUNDLE "
              "environment variable to point to a valid CA bundle file.")
        raise e
    print("Test Passed!")
