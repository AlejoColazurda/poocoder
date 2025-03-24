from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clientes_ecommerce",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Sistema de gestión de clientes para e-commerce con POO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/tu-repositorio",
    packages=find_packages(include=["clientes", "clientes.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.8",
    install_requires=[],  # Agrega dependencias si las tienes
    entry_points={
        "console_scripts": [
            "gestion-clientes=clientes.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "clientes": ["*.txt", "data/*.json"],  # Incluir archivos adicionales
    },
    project_urls={
        "Documentación": "https://github.com/tu-usuario/tu-repositorio/wiki",
        "Soporte": "https://github.com/tu-usuario/tu-repositorio/issues",
    },
    keywords="POO clientes ecommerce educación python",
)

"""
De acá saqué las ideas para construir el setup.py


https://www.freecodecamp.org/espanol/news/como-construir-tu-primer-paquete-de-python/
"""