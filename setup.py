
# petlink - Decode and encode PETlink streams. 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from setuptools import setup, Extension, Library
from glob import glob 

petlink32_c_module = Library('petlink.petlink32_c', ['petlink/petlink32_c.c']) 

setup(
    name='petlink',
    version='0.1.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['petlink', 'petlink.examples', 'petlink.tests'], 
    ext_modules=[petlink32_c_module, ],
    test_suite = "petlink.tests", 
    url='http://niftyrec.scienceontheweb.com/',
    license='LICENSE.txt',
    description='Decode and encode PETlink streams.',
    long_description=open('README.txt').read(),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.6.0", 
        "simplewrap >= 0.1.0", 
    ], 
)

