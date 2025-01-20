from setuptools import setup, find_packages

setup(
    name="empire-chain",
    version="0.2.13",
    description="An orchestration framework for all your AI needs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Manas Chopra",
    author_email="manaschopra95826@gmail.com",
    url="https://github.com/manas95826/empire-chain",
    packages=find_packages(),
    install_requires=[
        "openai",
        "anthropic",
        "groq",
        "qdrant-client",
        "chromadb",
        "sentence-transformers",
        "PyPDF2",
        "python-docx",
        "yfinance",
        "duckduckgo-search",
        "phidata",
        "streamlit",
        "numpy",
        "Pillow",
        "matplotlib",
        "docling",
        "tqdm",
        "soundfile",
        "kokoro_onnx",
        "python-dotenv",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)