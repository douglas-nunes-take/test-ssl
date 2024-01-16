import os

import certifi
import httpx

URL = "https://httpbin.org/get"

if __name__ == "__main__":
    print("Loaded environment variables:")
    for k, v in os.environ.items():
        print(f'{k}: {v}')

    print("\n\n#######################\n")

    certificates_path = certifi.where()
    print(f"Loaded certificates: {certificates_path}")

    print("\n\n#######################\n")
    with httpx.Client() as client:
        response = client.get(URL)
        response.raise_for_status()
        print("Test Passed!")
