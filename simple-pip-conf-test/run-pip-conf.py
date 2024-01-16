import subprocess

required_pip_conf = {
    "nexus",  # For nexus
    "truststore",  # To use system Certificate stores (better)
    # "cert",  # To use custom Certificate stores (worst)
}

if __name__ == "__main__":
    cfg_out = subprocess.check_output(['pip', 'config', 'list']).decode('utf-8')

    if len(cfg_out) == 0:
        print("No pip configuration found!")
        raise RuntimeError("No pip configuration found!")

    print("Loaded pip configuration:")
    print(cfg_out)

    for conf in required_pip_conf:
        if conf not in cfg_out:
            print(f"Missing required pip configuration: {conf}")
            print("For pip to succeed, you must set the right pip configuration ")
            raise RuntimeError(f"Missing required pip configuration: {conf}")

    print("\n\n#######################\n")
    print("Test Passed!")
