#!/usr/bin/env python

from setuptools import setup

setup(
        name='zimply',
        packages=['zimply'],
        version='1.0.0',
        description="ZIMply is an easy to use, offline reader for Wikipedia which provides access "
                    "to the offline Wikipedia through any ordinary browser.",
        long_description="ZIMply is an easy to use, offline reader for Wikipedia which provides access to the "
                         "offline Wikipedia through any ordinary browser. ZIMply is written entirely in Python 3 and, "
                         "as the name implies, relies on ZIM files. Each ZIM file is a bundle containing thousands "
                         "of articles, images, etc. as found on websites such as Wikipedia. ZIMply does all the "
                         "unpacking for you, and allows you to access the offline Wikipedia right from your "
                         "web browser by running its own web server.",
        author="Kim Bauters",
        author_email="kim.bauters@gmail.com",
        license='MIT',
        url="https://github.com/kimbauters/ZIMply",
        download_url='https://github.com/kimbauters/ZIMply/tarball/1.0.0',
        keyword=['zim', 'wiki', 'wikipedia'],
        py_modules=["zimply"],
        install_requires=["gevent", "falcon"],
        classifiers=[
            'Programming Language :: Python :: 3.4',
            'License :: OSI Approved :: MIT License',
            'Development Status :: 5 - Production/Stable',
        ],
        package_data={
            'sample': ['wiki.zim'],
        },
)
