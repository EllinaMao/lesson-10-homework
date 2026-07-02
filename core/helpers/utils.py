from dotenv import load_dotenv
import os

load_dotenv()

def get_creds():

    AZURE_URL = os.getenv("AZURE_URL")
    AZURE_KEY = os.getenv("AZURE_KEY")
    AZURE_REGION = os.getenv("AZURE_REGION")

    if (AZURE_KEY) == None:
        print("There no AZURE_KEY")
    if (AZURE_URL) == None:
        print("There no AZURE_URL")
    if (AZURE_REGION) == None:
        print("There no AZURE_REGION")

    return (AZURE_URL, AZURE_KEY, AZURE_REGION)

def file_to_bytes(path: str) -> bytes:
    try:
        with open(path, "rb") as file:
            file_bytes = file.read()
            return file_bytes
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("Unexpected error", e)
    return None
