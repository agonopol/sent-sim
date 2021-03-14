from os import path
from glob import glob
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
sentence-sim does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='sentsim',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A small sentence similarity library using lemmatization and word2vec",
    long_description=readme,
    author="Alex Gonopolskiy",
    author_email='agonopol@gmail.com',
    url='https://github.com/agonopol/sent-sim',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
    },
    include_package_data=True,
    data_files=[('assets/tokenizers/punkt/PY3', glob('assets/tokenizers/punkt/PY3/*')),
                ('assets/tokenizers/punkt', glob('assets/tokenizers/punkt/*.pickle')),
                ('assets/corpora/stopwords', glob('assets/corpora/stopwords/*', recursive=True)),
                ('assets/corpora/wordnet', glob('assets/corpora/wordnet/*', recursive=True)),
                ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
