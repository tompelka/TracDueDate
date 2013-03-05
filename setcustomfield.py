# -*- coding: utf-8 -*-
#Copyright (C) 2012 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator
from trac.env import Environment
import logging
from customfieldadmin.api import CustomFields

myenv = Environment('/srv/trac/myproject')
mycfcomp = CustomFields(myenv)
myenv.log.setLevel(logging.DEBUG)

class FillInTheDefault(Component):
    implements(ITicketManipulator)

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        fields = mycfcomp.get_custom_fields()
        myenv.log.debug("fields = %s", fields)
        for k, v in fields.iteritems():
            if k == "name" and v == "userfinish":
                fields[k]['value'] == ticket.milestone.due_date
