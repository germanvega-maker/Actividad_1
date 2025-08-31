from setuptools import setup, find_packages

setup(
    name="Actividad_1",
    version="0.0.1",
    author="German Vega",
    author_email="German.vega@est.iudigital.edu.co",
    description="ETL para análisis de datos del dólar",
    py_modules=["actividad1", "actividad2"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib"
    ]
)