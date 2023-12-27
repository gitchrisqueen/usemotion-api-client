# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.workspaces_api import WorkspacesApi


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkspacesApi()

    def tearDown(self) -> None:
        pass

    def test_statuses_controller_get(self) -> None:
        """Test case for statuses_controller_get

        List statuses for a workspace
        """
        pass

    def test_workspaces_controller_get(self) -> None:
        """Test case for workspaces_controller_get

        List workspaces
        """
        pass


if __name__ == '__main__':
    unittest.main()