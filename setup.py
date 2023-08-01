from setuptools import find_namespace_packages, setup

setup(
    name="django_typesense",
    author="Siege Software",
    author_email="info@siege.ai",
    version="0.0.1",
    install_requires=[
        "django",
        "typesense",
    ],
    setup_requires=["wheel"],
    packages=find_namespace_packages(),
    include_package_data=True,
)
