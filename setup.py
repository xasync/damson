import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lupin",
    version="0.1.0",
    author="xasync",
    author_email="ixasync@outlook.com",
    description="Lupin is a concise python library which aims to simplify the field validation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xasync/lupin",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
