from setuptools import setup, find_packages

# Function to read requirements.txt
def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="orphanet_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),  # Read dependencies from requirements.txt
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your package",
    url="https://github.com/yourusername/your-repo",
)