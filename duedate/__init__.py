# -*- coding: utf-8 -*-
#Copyright (C) 2012 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator
from trac.env import Environment
import logging
from customfieldadmin.api import CustomFields

myenv = Environment('/srv/trac/desktopqe-backlog-test')
mycfcomp = CustomFields(myenv)
myenv.log.setLevel(logging.DEBUG)

class FillInTheDefaultDueDate(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        fields = mycfcomp.get_custom_fields()
        myenv.log.debug("**duedate plugin** fields = %s", fields)
	myenv.log.debug("**duedate plugin** ticket /n %s", dir(ticket))
	for group in fields:
        	for key, val in group.iteritems():
            		if key == "name" and val == "userfinish":
                		#group['value'] == ticket.milestone.due_date
				group['value'] == u'2013-03-06'
