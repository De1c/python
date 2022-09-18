from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Cleaning tool',
    url='https://github.com/De1c/python/tree/main/clean_folder',
    author='Yehor Serdiuk',
    author_email='denpro8350@gmail.com',
    license='GOIT',
    packages=find_namespace_packages(),
    install_requires=['send2trash'],
    entry_points={'console_scripts': [
        'clean_folder = clean_folder.clean:start']}
)
