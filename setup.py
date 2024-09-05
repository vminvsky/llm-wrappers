from setuptools import setup, find_packages

setup(
    name='llm_wrappers',
    version='0.1',
    packages=find_packages('src'),  # Finds all packages inside 'src'
    package_dir={'': 'src'},        # Tells setuptools that packages are under 'src'
    install_requires=[],             # Add any dependencies if necessary
)