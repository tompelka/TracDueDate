# -*- coding: utf-8 -*-
#Copyright (C) 2012 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator
from trac.env import Environment
import logging
from customfieldadmin.api import CustomFields
import datetime
import sys

myenv = Environment('/srv/trac/desktopqe-backlog-test')
mycfcomp = CustomFields(myenv)
myenv.log.setLevel(logging.DEBUG)

class FillInTheDefaultDueDate(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        due_date = ""
        max_timestamp = 253402290000
        fields = mycfcomp.get_custom_fields()
        QUERY = "SELECT due FROM milestone WHERE name='%s'" % ticket['milestone']
        for row in myenv.get_read_db().execute(QUERY):
            if int(row[0]) > 0:
                due_date = datetime.datetime.fromtimestamp(int(row[0])/1000000)
            else:
                due_date = datetime.datetime.fromtimestamp(max_timestamp)
            myenv.log.debug("**duedate plugin** milestone due - %s", due_date)
            myenv.log.debug("**duedate plugin** milestone due type - ", type(due_date))
        for group in fields:
            for key, val in group.iteritems():
                if key == "name" and val == "userfinish":
                    #group['value'] = due_date.strftime('%Y-%m-%d')
                    myenv.log.debug("**duedate plugin** due date - %s", group)
                    group['value'] = due_date
                if key == "name" and val == "usertart":
                    #group['value'] = datetime.datetime.now().strftime('%Y-%m-%d')
                    group['value'] = datetime.datetime.now()
        return []
