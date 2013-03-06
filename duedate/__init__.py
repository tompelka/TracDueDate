# -*- coding: utf-8 -*-
#Copyright (C) 2012 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator
from trac.env import Environment
import logging
from customfieldadmin.api import CustomFields
import datetime

myenv = Environment('/srv/trac/desktopqe-backlog-test')
mycfcomp = CustomFields(myenv)
myenv.log.setLevel(logging.DEBUG)

class FillInTheDefaultDueDate(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
	due_date = ""
        fields = mycfcomp.get_custom_fields()
	QUERY = "SELECT due FROM milestone WHERE name='%s'" % ticket['milestone']
        myenv.log.debug("**duedate plugin** fields = %s", fields)
	myenv.log.debug("**duedate plugin** ticket milestone - %s", ticket['milestone'])
	for row in myenv.get_read_db().execute(QUERY):
		due_date = datetime.datetime.fromtimestamp(int(row[0])/1000000).strftime('%Y-%m-%d')
		myenv.log.debug("**duedate plugin** milestone due - %s", due_date)
	for group in fields:
        	for key, val in group.iteritems():
            		if key == "name" and val == "userfinish":
                		#group['value'] == ticket.milestone.due_date
				group['value'] == due_date
