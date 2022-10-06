#!/usr/bin/env python3
'''SessionAuth class'''

import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    '''SessionAuth'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Return the Session ID'''
        if user_id is None or type(user_id) is not str:
            return None
        Session_ID = str(uuid.uuid4())
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on a Session ID'''
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''returns a User instance based on a cookie value'''
        return User.get(self.user_id_for_session_id(
                self.session_cookie(request)))
