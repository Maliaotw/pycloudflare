import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name="pycloudflare",
    version="0.0.1",
    author="Maliao",
    author_email="maliaotw@gmail.com",
    description="CLOUDFLARE SDK package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Maliaotw/pycloudflare.git",
    package_dir={'pycloudflare': 'pycloudflare'},
    packages=["pycloudflare"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

install_requires = [
    'requests>=2.12.3',
]

dependency_links=[
]

if __name__ == '__main__':
    setuptools.setup(**setup_args, install_requires=install_requires)
