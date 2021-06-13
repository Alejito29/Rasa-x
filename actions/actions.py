# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

import os, shutil
import sqlalchemy as sa
from typing import Dict, Text, Any, List
from rasa_sdk.interfaces import Action
from rasa_sdk import Tracker
import logging

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)
from actions.profile_db import create_database, ProfileDB

from faker import Faker

PROFILE_DB_NAME = os.environ.get("PROFILE_DB_NAME", "profile")
PROFILE_DB_URL = os.environ.get("PROFILE_DB_URL", f"sqlite:///{PROFILE_DB_NAME}.db")
ENGINE = sa.create_engine(PROFILE_DB_URL)
create_database(ENGINE, PROFILE_DB_NAME)

profile_db = ProfileDB(ENGINE)
import datetime as dt
from pprint import pprint

logger = logging.getLogger(__name__)

NEXT_RESERVATION_NAME = {
    "pay_cc": "reservation_field_form",
}
import webbrowser

path_file = 'C:/Users/wilso/Desktop/rasa/Formularios/'


class SaveReservationInDataBaseForSlotAction(Action):

    def name(self) -> Text:
        return "action_save_data_in_storage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:

        data_factory = Faker()
        first_name = tracker.get_slot("first_name")
        last_name = tracker.get_slot("last_name")
        phones = tracker.get_slot("phones")
        niif = tracker.get_slot("niif")
        room = tracker.get_slot("room")
        category = tracker.get_slot("category")

        if not isinstance(category, int) and (int(category) < 0 or int(category) > 3):
            dispatcher.utter_message(text=f"Your category is filled wrong, "
                                          f"also it should be minor to 4, it must be major to 0."
                                          f"PLease try again to take the reservation ")
            return []

        if not isinstance(room, int) and (int(room) <= 0):
            dispatcher.utter_message(text=f"The room number must be number,"
                                          f"also it must be major to 0"
                                          f"PLease try again to take the reservation ")
            return []

        if not bool(first_name and first_name.isspace()) or not bool(last_name and last_name.isspace()):
            dispatcher.utter_message(text=f"Your lastname and name can not be empty, please try again")
            return []

        niif_all = list(filter(lambda x: x.NIIF == niif,
                               profile_db.get_all_niif()))
        if len(niif_all) == 0:
            profile_db.add_niif(data_factory.sentence(nb_words=50), niif)

        niif_all = list(filter(lambda x: x.NIIF == niif,
                               profile_db.get_all_niif()))

        user_all = list(filter(lambda x: x.NAME == first_name and x.LAST_NAME == last_name,
                               profile_db.get_all_user()))
        if len(user_all) == 0:
            profile_db.add_user(first_name, last_name)

        user_all = list(filter(lambda x: x.NAME == first_name and x.LAST_NAME == last_name,
                               profile_db.get_all_user()))

        ticket = data_factory.random_int(0, 600)
        profile_db.add_reservation(niif_all[0].id, phones, user_all[0].id, int(room), ticket)

        rooms_reservation = len(profile_db.get_all_rooms()) - 1
        for i in range(int(room)):
            rooms_reservation = rooms_reservation + 1
            rooms_number = "A" + str(rooms_reservation)
            profile_db.add_rooms(rooms_number, 1, False, ticket)

        dispatcher.utter_message(text=f"We saved the information in our system, the ticket was {ticket} "
                                      f", it permits to cancel, update or add extra expense, not forget it")
        return []


class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_last_name"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        first_name = tracker.get_slot("first_name")
        dispatcher.utter_message(text=f"So {first_name}, what is your last name?")
        return []


class ActionRestartForms(Action):
    """Executes after restart of a session"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_restart"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Executes the custom action"""
        return [Restarted(), FollowupAction("action_session_start")]


class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class AskForSlotActionDelivery(Action):
    def name(self) -> Text:
        return "action_ask_ticket_reservation"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text=f"What is the ticket?  ")
        return []


class AskForSlotActionExpense(Action):
    def name(self) -> Text:
        return "action_ask_expense"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        ticket = int(tracker.get_slot("ticket_reservation").strip())
        total = 0

        delivery = profile_db.get_all_delivery()
        for item in delivery:
            if ticket == item.TICKET:
                total = item.VALOR + total

        dispatcher.utter_message(text=f"Our system calculate that you should pay the next {total} "
                                      f"with the next ticket {ticket}")
        return []


class AskForSlotActionRoomReport(Action):
    def name(self) -> Text:
        return "action_ask_the_report_room"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        open(path_file + "Pagina/report.html", 'w').close()
        content_header = open(path_file + "Plantilla/encabezado.txt", "r")
        content_file_header = content_header.read()

        content_footer = open(path_file + "Plantilla/footer.txt", "r")
        content_file_footer = content_footer.read()

        rooms = profile_db.get_all_rooms()

        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>ROOM_NUMBER</th>" \
                  "<th>KIND_OF_ROOM</th>" \
                  "<th>ROOM_STATE</th>" \
                  "<th>TICKET_RESERVATION</th>" \
                  "</tr>"
        html_content = ''
        for item in rooms:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.ROOM_NUMBER + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.KIND_OF_ROOM + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.ROOM_STATE + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET_RESERVATION) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        f = open(path_file + "Pagina/report.html", "a")
        f.write(content_file_header + '\n')
        f.write(html_td + '\n')
        f.write(html_content + '\n')
        f.write(content_file_footer)
        f.close()
        url = path_file + "Pagina/report.html"
        webbrowser.open(url)
        dispatcher.utter_message(text=f"We are going to page the report")
        return []


class AskForSlotActionUserReport(Action):
    def name(self) -> Text:
        return "action_ask_the_report_user"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        open(path_file + "Pagina/report.html", 'w').close()
        content_header = open(path_file + "Plantilla/encabezado.txt", "r")
        content_file_header = content_header.read()

        content_footer = open(path_file + "Plantilla/footer.txt", "r")
        content_file_footer = content_footer.read()

        rooms = profile_db.get_all_user()
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>NAME</th>" \
                  "<th>LAST_NAME</th>" \
                  "</tr>"
        html_content = ''
        for item in rooms:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.NAME + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.LAST_NAME + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        f = open(path_file + "Pagina/report.html", "a")
        f.write(content_file_header + '\n')
        f.write(html_td + '\n')
        f.write(html_content + '\n')
        f.write(content_file_footer)
        f.close()
        url = path_file + "Pagina/report.html"
        webbrowser.open(url)
        dispatcher.utter_message(text=f"We are going to page the report")
        return []


class AskForSlotActionReservationReport(Action):
    def name(self) -> Text:
        return "action_ask_the_report_reservation"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        open(path_file + "Pagina/report.html", 'w').close()
        content_header = open(path_file + "Plantilla/encabezado.txt", "r")
        content_file_header = content_header.read()

        content_footer = open(path_file + "Plantilla/footer.txt", "r")
        content_file_footer = content_footer.read()

        reservation = profile_db.get_all_reservation()
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>ID_USER</th>" \
                  "<th>PHONES</th>" \
                  "<th>ID_NIIF</th>" \
                  "<th>ROOMS</th>" \
                  "<th>TICKET</th>" \
                  "</tr>"
        html_content = ''
        for item in reservation:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ID_USER) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.PHONES + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ID_NIIF) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ROOMS) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        f = open(path_file + "Pagina/report.html", "a")
        f.write(content_file_header + '\n')
        f.write(html_td + '\n')
        f.write(html_content + '\n')
        f.write(content_file_footer)
        f.close()
        url = path_file + "Pagina/report.html"
        webbrowser.open(url)
        dispatcher.utter_message(text=f"We are going to page the report")
        return []


class AskForSlotActionExpenseReport(Action):
    def name(self) -> Text:
        return "action_ask_the_report_expense"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        open(path_file + "Pagina/report.html", 'w').close()
        content_header = open(path_file + "Plantilla/encabezado.txt", "r")
        content_file_header = content_header.read()

        content_footer = open(path_file + "Plantilla/footer.txt", "r")
        content_file_footer = content_footer.read()

        expense = profile_db.get_all_expense()
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>DESCRIPTION</th>" \
                  "<th>VALOR</th>" \
                  "<th>TICKET</th>" \
                  "</tr>"
        html_content = ''
        for item in expense:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.DESCRIPTION + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.VALOR) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        f = open(path_file + "Pagina/report.html", "a")
        f.write(content_file_header + '\n')
        f.write(html_td + '\n')
        f.write(html_content + '\n')
        f.write(content_file_footer)
        f.close()
        url = path_file + "Pagina/report.html"
        webbrowser.open(url)
        dispatcher.utter_message(text=f"We are going to page the report")
        return []


class AskForSlotActionAllReport(Action):
    def name(self) -> Text:
        return "action_ask_the_report_all"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        open(path_file + "Pagina/report.html", 'w').close()

        content_header = open(path_file + "Plantilla/encabezado.txt", "r")
        content_file_header = content_header.read()

        expense = profile_db.get_all_expense()
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>DESCRIPTION</th>" \
                  "<th>VALOR</th>" \
                  "<th>TICKET</th>" \
                  "</tr>"
        html_content = html_td
        for item in expense:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.DESCRIPTION + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.VALOR) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp + '\n'

        html_content = html_content + "</table>" + '\n'

        reservation = profile_db.get_all_reservation()

        html_content = html_content + "<div style=height: 32px;><span style=height: 32px;>Contenido de reservaciones</span></div>" + '\n'
        html_content = html_content + "<table>"
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>ID_USER</th>" \
                  "<th>PHONES</th>" \
                  "<th>ID_NIIF</th>" \
                  "<th>ROOMS</th>" \
                  "<th>TICKET</th>" \
                  "</tr>"
        html_content = html_content + html_td
        for item in reservation:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ID_USER) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.PHONES + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ID_NIIF) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.ROOMS) + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        html_content = html_content + "</table>" + '\n'

        rooms = profile_db.get_all_user()
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>NAME</th>" \
                  "<th>LAST_NAME</th>" \
                  "</tr>"

        html_content = html_content + "<div style=height: 32px;><span style=height: 32px;>Contenido de usuarios</span></div>" + '\n'
        html_content = html_content + "<table>"
        html_content = html_content + html_td
        for item in rooms:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.NAME + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.LAST_NAME + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        html_content = html_content + "</table>" + '\n'

        rooms = profile_db.get_all_rooms()
        html_content = html_content + "<div style=height: 32px;><span style=height: 32px;>Contenido de cuartos</span></div>" + '\n'
        html_content = html_content + "<table>"
        html_td = "<tr>" \
                  "<th>ID</th>" \
                  "<th>ROOM_NUMBER</th>" \
                  "<th>KIND_OF_ROOM</th>" \
                  "<th>ROOM_STATE</th>" \
                  "<th>TICKET_RESERVATION</th>" \
                  "</tr>"
        html_content = html_content + html_td
        for item in rooms:
            item_html_tmp = "<tr><td> " + str(item.id) + "</td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.ROOM_NUMBER + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.KIND_OF_ROOM + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + item.ROOM_STATE + " </td>" + '\n'
            item_html_tmp = item_html_tmp + "<td> " + str(item.TICKET_RESERVATION) + " </td></tr>" + '\n'
            html_content = html_content + item_html_tmp

        html_content = html_content + "</table>" + '\n'

        html_content = html_content + "</body></html>" + '\n'
        f = open(path_file + "Pagina/report.html", "a")
        f.write(content_file_header + '\n')
        f.write(html_content + '\n')
        f.close()
        url = path_file + "Pagina/report.html"
        webbrowser.open(url)
        dispatcher.utter_message(text=f"We are going to page the report")
        return []


class AskForSlotActionExpense(Action):
    def name(self) -> Text:
        return "action_ask_delivery_room"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        ticket_reservation = str(tracker.get_slot("ticket_reservation"))

        if ticket_reservation.isdigit():
            room_filter = list(filter(lambda x: x.TICKET_RESERVATION == int(ticket_reservation),
                                      profile_db.get_all_rooms()))
            for item in room_filter:
                profile_db.updateRoom(item.TICKET_RESERVATION, 'LIBRE')
            dispatcher.utter_message(text=f"Now your room was free")
        else:
            dispatcher.utter_message(text=f"El ticket must be numeric and kind of real")

        return []
