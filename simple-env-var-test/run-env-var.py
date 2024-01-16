import os

REQUIRED_ENV_VARS = {
    "REQUESTS_CA_BUNDLE": ".pem",  # For requests
    "SSL_CERT_FILE": ".pem",  # For httpx
    "SSL_CERT_DIR": None,  # For httpx
}

if __name__ == "__main__":
    print("Loaded environment variables:")
    for k, v in os.environ.items():
        print(f'{k}: {v}')

    print("\n\n#######################\n")

    for k, v in REQUIRED_ENV_VARS.items():
        if k not in os.environ:
            print(f"Missing required environment variable: {k}")
            raise RuntimeError(f"Missing required environment variable: {k}")
        env_var = os.environ[k]
        if v is not None and not os.path.exists(env_var):
            print(f"Environment variable {k} points to non-existent file: {os.environ[k]}")
            raise RuntimeError(f"Environment variable {k} points to non-existent file: {os.environ[k]}")
        if v is not None and not env_var.endswith(v):
            print(f"Environment variable {k} does not point to a {v} file: {env_var}")
            raise RuntimeError(f"Environment variable {k} does not point to a {v} file: {env_var}")

    print("\n\n#######################\n")
    print("Test Passed!")
