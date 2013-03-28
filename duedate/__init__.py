# -*- coding: utf-8 -*-
#Copyright (C) 2012 Red Hat, Inc.

from trac.core import Component, implements
from trac.ticket.api import ITicketManipulator
from trac.config import Option
from trac.ticket.model import Milestone
import datetime

class FillInTheDefaultDueDate(Component):
    implements(ITicketManipulator)

    field = Option('ticket-duedate', 'field', 'userfinish',
                   doc="Ticket field that contains the ticket due date.")

    ### ITicketManipulator methods

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        max_timestamp = 253402290000
        if not ticket.exists and ticket['milestone']:
            milestone = Milestone(self.env, ticket.values['milestone'])
            if milestone and milestone.due and \
                self.field in ticket.values and not ticket.values[self.field]:
                ticket.values[self.field] = milestone.due.strftime('%Y-%m-%d')
            if milestone and self.field in ticket.values and not ticket.values[self.field]:
                ticket.values[self.field] = datetime.datetime.fromtimestamp(max_timestamp)

        return []

class FillInTheDefaultStartDate(Component):
    implements(ITicketManipulator)

    field = Option('ticket-startdate', 'field', 'userstart',
                   doc="Ticket field that contains the ticket start date.")

    ### ITicketManipulator methods

    def prepare_ticket(self, req, ticket):
        pass

    def validate_ticket(self, req, ticket):
        if not ticket.exists:
            if self.field in ticket.values and not ticket.values[self.field]:
                ticket.values[self.field] = datetime.datetime.now().strftime('%Y-%m-%d')

        return []
