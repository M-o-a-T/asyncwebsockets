import sys
from pathlib import Path

from setuptools import setup

exec(open("trio_websockets/_version.py", encoding="utf-8").read())

if sys.version_info[0:2] < (3, 6):
    raise RuntimeError("This package requires Python 3.6+.")

setup(
    name="trio-websockets",
    version=__version__,  # noqa: F821
    use_scm_version={
        "version_scheme": "guess-next-dev",
        "local_scheme": "dirty-tag"
    },
    packages=[
        "trio_websockets"
    ],
    url="https://github.com/M-o-a-T/trio-websockets",
    license="MIT",
    author="Matthias Urlichs",
    author_email="matthias@urlichs.de",
    description="A websocket library for trio",
    long_description=Path(__file__).with_name("README.rst").read_text(encoding="utf-8"),
    setup_requires=[
        "setuptools_scm",
        "pytest-runner"
    ],
    install_requires=[
        "trio",
        "wsproto>=0.11.0"
    ],
    extras_require={},
    python_requires=">=3.6",
)
