from setuptools import setup, find_packages
setup(
    name = 'calculator_app',
    version= '0.1.0',
    description='GUI app to do simple calculations',
    author='Canrong Qiu (Jackey)',
    author_email='canrong.qiu@desy.de',
    url='https://github.com/jackey-qiu/pyCalculator',
    classifiers=['Topic :: pyQt application',
                 'Programming Language :: Python'],
    license='MIT',
    install_requires=['PyQt5','qdarkstyle','PyYAML'],
    packages=find_packages(),
    # packages=find_packages(where='library_manager'),
    # package_dir={'': 'library_lanager'},
    package_data={'calculator_app.res':['config/*','icons/*.*','ui/*']},
    scripts=['./calculator_app/bin/main_gui.py'],
    entry_points = {
        'console_scripts' : [
            'cal = calculator_app.bin.main_gui:main'
        ],
    }
)