from setuptools import setup, find_packages

setup(
    name="syndemics_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "networkx",
        "scipy",
        "statsmodels",
        "jupyter",
        "notebook"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A machine learning and network analysis approach to identifying syndemics in healthcare data.",
    url="https://github.com/your-username/syndemics-analysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
