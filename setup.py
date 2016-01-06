from setuptools import setup


setup(
    name='pygments-lexer-babylon',
    description='A javascript lexer for Pygments that uses the babylon parser',
    version='1.0',
    install_requires=[
        'Pygments >= 2.0'
    ],
    data_files=[('node_modules/.bin', ['pygmentslexerbabylon/ode_modules/.bin/babylon'])],
    license='MIT',
    packages=['pygmentslexerbabylon']
)
