# src/main.py
import os

def main():
    GITHUB_ENV = os.environ.get("GITHUB_ENV")
    print(GITHUB_ENV)

if __name__ == "__main__":
    main()