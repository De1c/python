from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Cleaning tool',
    url='http://github.com/dummy_user/useful',
    author='Yehor Serdiuk',
    author_email='denpro8350@gmail.com',
    license='GOIT',
    packages=find_namespace_packages(),
    install_requires=['send2trash'],
    entry_points={'console_scripts': [
        'start = clean_folder.clean:start']}
)
