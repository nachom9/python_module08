#!/usr/bin/env python3

import importlib


def check_dependencies():
    print("Checking dependencies:")
    try:
        pandas = importlib.import_module('pandas')
    except ModuleNotFoundError:
        pandas = None
    try:
        requests = importlib.import_module('requests')
    except ModuleNotFoundError:
        requests = None
    try:
        matplotlib = importlib.import_module('matplotlib')
    except ModuleNotFoundError:
        matplotlib = None
    try:
        numpy = importlib.import_module('numpy')
    except ModuleNotFoundError:
        numpy = None

    install = False
    if pandas:
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    else:
        print("[KO] pandas not found")
        install = True
    if requests:
        print(f"[OK] requests ({requests.__version__}) -"
              f" Data manipulation ready")
    else:
        print("[KO] requests not found")
        install = True
    if matplotlib:
        print(f"[OK] matplotlib ({matplotlib.__version__}) -"
              f" Data manipulation ready")
    else:
        print("[KO] matplotlib not found")
        install = True
    if numpy:
        print(f"[OK] numpy ({numpy.__version__}) - Data manipulation ready")
    else:
        print("[KO] numpy not found")
        install = True

    if install:
        print("\nDetected missing dependencies. Execute: 'pip install -r"
              " requirements.txt' or 'poetry install'")


def main():
    print("\nOPERATOR STATUS: Loading programs...\n")
    check_dependencies()


if __name__ == "__main__":
    main()
