from distutils.core import setup

with open('README.md') as f:
    data = f.read()
try:
    import pypandoc
    description = pypandoc.convert(data, 'rst', format='markdown')
except ImportError:
    print("pypandoc conversion failed, readme will not be rendered on PyPI")
    print("(You can ignore this if you're only doing local development)")
    description = data


setup(
    name='scat',
    version='0.2.0',
    py_modules=['scat'],
    license='BSD',
    author='Paul Ivanov',
    entry_points={'console_scripts': [ 'scat=scat:main']},
    author_email='pi@berkeley.edu',
    url='https://github.com/ivanov/scat',
    description="Schrödinger's cat",
    long_description=description
)
