import fastapi
import pydantic
import uvicorn
print('Package versions:')
print(f'FastAPI: {fastapi.__version__}')
print(f'Pydantic: {pydantic.__version__}')
print(f'Uvicorn: {uvicorn.__version__}')