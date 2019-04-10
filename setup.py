from setuptools import setup, find_packages

setup(
    name='riptide_cli',
    version='0.1',
    packages=find_packages(),
    description= 'TODO',  # TODO
    long_description='TODO - Project will be available starting May',  # TODO
    url='https://riptide-docs.readthedocs.io/en/latest/',
    author='Marco "Parakoopa" Köpcke',
    license='MIT',
    install_requires=[
        'riptide_lib == 0.1',
        'Click >= 7.0',
        'colorama >= 0.4',
        'click-help-colors >= 0.5',
        'tqdm >= 4.29',
    ],
    # TODO
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points='''
        [console_scripts]
        riptide=riptide_cli.main:cli
    ''',
)