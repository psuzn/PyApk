from setuptools import setup, find_packages

setup(
    name='pyapk',
    packages=find_packages(),
    version='0.1',
    description='A simple program to install apks from a directory to android phone via adb',
    author='Sujan Poudel',
    author_email='psuzzn@gmail.com',
    url='https://github.com/psuzn/PyApk',
    download_url='https://github.com/psuzn/PyApk',
    keywords=['adb', 'apk', 'install', 'android'],  # arbitrary keywords
    install_requires=[
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'pyapk = pyapk.pyapk:pyapkInit'
        ]},
)
