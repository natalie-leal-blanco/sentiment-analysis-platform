try:
    import fastapi
    import pydantic
    import uvicorn

    print("Installed versions:")
    print(f"FastAPI: {fastapi.__version__}")
    print(f"Pydantic: {pydantic.__version__}")
    print(f"Uvicorn: {uvicorn.__version__}")
    print("\nImport test successful!")
except Exception as e:
    print(f"Error: {e}")
