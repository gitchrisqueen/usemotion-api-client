# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.status import Status

class TestStatus(unittest.TestCase):
    """Status unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Status:
        """Test Status
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Status`
        """
        model = Status()
        if include_optional:
            return Status(
                name = '',
                is_default_status = True,
                is_resolved_status = True
            )
        else:
            return Status(
                name = '',
                is_default_status = True,
                is_resolved_status = True,
        )
        """

    def testStatus(self):
        """Test Status"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
