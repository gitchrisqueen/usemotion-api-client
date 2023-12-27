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

from openapi_client.models.list_recurring_tasks import ListRecurringTasks

class TestListRecurringTasks(unittest.TestCase):
    """ListRecurringTasks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListRecurringTasks:
        """Test ListRecurringTasks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListRecurringTasks`
        """
        model = ListRecurringTasks()
        if include_optional:
            return ListRecurringTasks(
                tasks = [
                    openapi_client.models.recurring_task.RecurringTask(
                        workspace = openapi_client.models.workspace.Workspace(
                            id = '', 
                            name = '', 
                            team_id = '', 
                            statuses = [
                                openapi_client.models.status.Status(
                                    name = '', 
                                    is_default_status = True, 
                                    is_resolved_status = True, )
                                ], 
                            labels = [
                                openapi_client.models.label.Label(
                                    name = '', )
                                ], 
                            type = '', ), 
                        id = '', 
                        name = '', 
                        description = '', 
                        creator = null, 
                        assignee = openapi_client.models.user.User(
                            id = '', 
                            name = '', 
                            email = '', ), 
                        project = openapi_client.models.project.Project(
                            id = '', 
                            name = '', 
                            description = '', 
                            workspace_id = '', ), 
                        status = openapi_client.models.status.Status(
                            name = '', 
                            is_default_status = True, 
                            is_resolved_status = True, ), 
                        priority = 'ASAP', 
                        labels = [
                            openapi_client.models.label.Label(
                                name = '', )
                            ], )
                    ],
                meta = openapi_client.models.meta_result.MetaResult(
                    next_cursor = '', 
                    page_size = 1.337, )
            )
        else:
            return ListRecurringTasks(
                tasks = [
                    openapi_client.models.recurring_task.RecurringTask(
                        workspace = openapi_client.models.workspace.Workspace(
                            id = '', 
                            name = '', 
                            team_id = '', 
                            statuses = [
                                openapi_client.models.status.Status(
                                    name = '', 
                                    is_default_status = True, 
                                    is_resolved_status = True, )
                                ], 
                            labels = [
                                openapi_client.models.label.Label(
                                    name = '', )
                                ], 
                            type = '', ), 
                        id = '', 
                        name = '', 
                        description = '', 
                        creator = null, 
                        assignee = openapi_client.models.user.User(
                            id = '', 
                            name = '', 
                            email = '', ), 
                        project = openapi_client.models.project.Project(
                            id = '', 
                            name = '', 
                            description = '', 
                            workspace_id = '', ), 
                        status = openapi_client.models.status.Status(
                            name = '', 
                            is_default_status = True, 
                            is_resolved_status = True, ), 
                        priority = 'ASAP', 
                        labels = [
                            openapi_client.models.label.Label(
                                name = '', )
                            ], )
                    ],
        )
        """

    def testListRecurringTasks(self):
        """Test ListRecurringTasks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()