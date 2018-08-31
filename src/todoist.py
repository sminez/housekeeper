'''
Super simple todoist client.
'''
import json
import uuid
from datetime import datetime

from requests import get, post, HTTPError


class TodoistAPI:
    url = 'https://beta.todoist.com/API/v8/{}'

    def __init__(self, token):
        self.token = token

    def _query(self, req_func, endpoint, params={}, data=None, headers=None):
        '''
        Query the Todoist REST API using an api token
        '''

        params['token'] = self.token
        resp = req_func(
            self.url.format(endpoint),
            params=params,
            data=data,
            headers=headers
        )

        if 200 <= resp.status_code < 400:
            try:
                return resp.json()
            except json.JSONDecodeError:
                # TODO: confirm that this is the correct error
                return resp.text

        raise HTTPError(resp.reason)

    @staticmethod
    def today():
        '''
        Return today's date as a mm/dd/yyyy formatted string.
        Most APIs are American...
        '''
        td = datetime.now()
        return '{}/{}/{}'.format(td.month, td.day, td.year)

    def all_tasks(self):
        '''Get all open tasks'''
        return self._query(get, 'tasks')

    def all_projects(self):
        '''Get all active projects'''
        return self._query(get, 'projects')

    def all_labels(self):
        '''Get all active labels'''
        return self._query(get, 'labels')

    def all_comments(self, task_id=None, project_id=None):
        '''Get all comments for a given task or project'''
        both = task_id and project_id
        neither = task_id is None and project_id is None

        if both or neither:
            raise ValueError('Must pass one of task_id or project_id')

        if task_id:
            return self._query(get, 'comments', {'task_id': task_id})
        return self._query(get, 'comments', {'project_id': project_id})

    def today_and_overdue(self):
        '''Get tasks that need to be done today'''
        return self._query(
            get, 'tasks', {'filter': '(overdue|{})'.format(self.today())})

    def close_task(self, task_id):
        '''Close a task by ID'''
        return self._query(post, 'tasks/{}/close'.format(task_id))

    def new_task(self, content, priority=1):
        '''Create a new task'''
        data = json.dumps({
            'content': content,
            'due_string': self.today(),
            'due_lang': 'en',
            'priority': 1
        })
        headers = {
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
        }

        return self._query(post, 'tasks', data=data, headers=headers)
