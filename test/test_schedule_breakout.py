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

from openapi_client.models.schedule_breakout import ScheduleBreakout

class TestScheduleBreakout(unittest.TestCase):
    """ScheduleBreakout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleBreakout:
        """Test ScheduleBreakout
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleBreakout`
        """
        model = ScheduleBreakout()
        if include_optional:
            return ScheduleBreakout(
                monday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                tuesday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                wednesday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                thursday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                friday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                saturday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                sunday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ]
            )
        else:
            return ScheduleBreakout(
                monday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                tuesday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                wednesday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                thursday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                friday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                saturday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
                sunday = [
                    openapi_client.models.daily_schedule.DailySchedule(
                        start = '08:30', 
                        end = '18:00', )
                    ],
        )
        """

    def testScheduleBreakout(self):
        """Test ScheduleBreakout"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
