from setuptools import setup

setup(
    name='spotipy',
    version='0.1',
    description='A  rudimentary interface to the Spotify player on OS X',
    author='Steve Winton',
    author_email='stevewinton@gmail.com',
    url='http://github.com/swinton/spotipy',
    packages=['spotipy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "License :: Free For Home Use",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Topic :: Desktop Environment",
    ],
    keywords='apple osx spotify desktop',
    license='GPL',
    install_requires=[
        'setuptools',
    ],
)