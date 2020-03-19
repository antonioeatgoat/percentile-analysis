import setuptools

setuptools.setup(
    name="stockcacl",
    version="0.1.0",
    author="Antonio Mangiacapra",
    description="Stock Calculator - Percentile Analysis",
    long_description="A simple python module to perform percentile analysis on stock data",
    long_description_content_type="text/markdown",
    url="https://github.com/antonioeatgoat/percentile-analysis",
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)