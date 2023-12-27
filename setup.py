# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Contact: christopher.queen@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "usemotion_api_client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Motion REST API",
    author="Christopher Queen",
    author_email="christopher.queen@gmail.com",
    url="https://github.com/gitchrisqueen/usemotion-api-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Motion REST API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    &lt;!-- theme: warning --&gt;  &gt; ### Rate Limit Information &gt; &gt; The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times &gt; in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  &lt;!-- theme: info --&gt;  &gt; ### Note on Date Formats &gt; &gt; All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 
    """,  # noqa: E501
    package_data={"usemotion_api_client": ["py.typed"]},
)
