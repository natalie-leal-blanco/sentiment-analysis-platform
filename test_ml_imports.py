try:
    import torch
    import transformers
    import numpy

    print("PyTorch version:", torch.__version__)
    print("Transformers version:", transformers.__version__)
    print("NumPy version:", numpy.__version__)
    print("\nAll ML packages imported successfully!")
except Exception as e:
    print(f"Error: {e}")
