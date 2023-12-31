# coding: utf-8

# flake8: noqa
"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Contact: christopher.queen@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

# import models into model package
from usemotion_api_client.models.auto_scheduled_info import AutoScheduledInfo
from usemotion_api_client.models.comment import Comment
from usemotion_api_client.models.comment_post import CommentPost
from usemotion_api_client.models.daily_schedule import DailySchedule
from usemotion_api_client.models.label import Label
from usemotion_api_client.models.list_comments import ListComments
from usemotion_api_client.models.list_projects import ListProjects
from usemotion_api_client.models.list_recurring_tasks import ListRecurringTasks
from usemotion_api_client.models.list_tasks import ListTasks
from usemotion_api_client.models.list_users import ListUsers
from usemotion_api_client.models.list_workspaces import ListWorkspaces
from usemotion_api_client.models.meta_result import MetaResult
from usemotion_api_client.models.move_task import MoveTask
from usemotion_api_client.models.project import Project
from usemotion_api_client.models.project_post import ProjectPost
from usemotion_api_client.models.recurring_task import RecurringTask
from usemotion_api_client.models.recurring_tasks_post import RecurringTasksPost
from usemotion_api_client.models.recurring_tasks_post_duration import RecurringTasksPostDuration
from usemotion_api_client.models.schedule import Schedule
from usemotion_api_client.models.schedule_breakout import ScheduleBreakout
from usemotion_api_client.models.status import Status
from usemotion_api_client.models.task import Task
from usemotion_api_client.models.task_duration import TaskDuration
from usemotion_api_client.models.task_patch import TaskPatch
from usemotion_api_client.models.task_patch_duration import TaskPatchDuration
from usemotion_api_client.models.task_post import TaskPost
from usemotion_api_client.models.user import User
from usemotion_api_client.models.workspace import Workspace
