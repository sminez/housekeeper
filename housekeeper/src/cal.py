'''
Check calendars
'''
from datetime import datetime, date, timedelta

import requests
from pytz import utc
from icalendar import Calendar

DEFAULT_QUERY_LENGTH = timedelta(days=7)
DEFAULT_ENCODING = 'utf-8'


def events(url=None, start=None, end=None, encoding=DEFAULT_ENCODING):
    '''
    Get all events form the given iCal URL occurring in the given time range.
    '''
    if url.startswith('webcal://'):
        url = url.replace('webcal://', 'http://', 1)

    resp = requests.get(url)

    if not resp.ok:
        raise ConnectionError(
            'Unable to fetch data from {}'.format(url)
        )

    content = resp.content.decode(encoding)
    content = content.replace('\r', '')

    # Fix Apple tzdata bug.
    content = content.replace('TZOFFSETFROM:+5328', 'TZOFFSETFROM:+0053')

    return parse_events(content, start=start, end=end)


def parse_events(content, start=None, end=None):
    '''
    Fetch all events in the given time range.
    '''
    if start is None:
        start = utc.localize(datetime.utcnow())

    if end is None:
        end = start + DEFAULT_QUERY_LENGTH

    start, end = map(normalize, [start, end])
    calendar = Calendar.from_ical(content)
    found = []

    for component in calendar.walk():
        if component.name == "VEVENT":
            evt = Event(component)

            if evt.start <= end and evt.end >= start:
                # Event is in range so keep it
                found.append(evt)

    # Sort into ascending order
    return sorted(found)


def normalize(dt):
    '''
    Convert date or datetime to datetime with timezone.
    '''
    if not isinstance(dt, datetime):
        # convert the date to a datetime
        dt = datetime.combine(dt, datetime.min.time())

    if not dt.tzinfo:
        dt = utc.localize(dt)

    return dt


class Event:
    '''A single calendar event'''

    def __init__(self, component):
        '''
        Create a new event occurrence from an iCal component.
        '''
        self.all_day = False

        event_start = component.get('dtstart')
        if event_start is None:
            raise ValueError('Event must have a start date')

        if type(event_start.dt) is date:
            self.all_day = True

        event_start = normalize(event_start.dt)

        event_end = component.get('dtend')
        if event_end is not None:
            event_end = normalize(event_end.dt)
        else:
            # This is a single day all day event
            event_end = event_start + timedelta(days=1)
            self.all_day = True

        if component.get('rrule'):
            rule = component.get('rrule')
            freq = str(rule.get('FREQ')[0])
            recurring = True
        else:
            recurring = False
            freq = None

        self.start = event_start
        self.end = event_end
        self.summary = str(component.get('summary'))
        self.description = str(component.get('description'))
        self.recurring = recurring
        self.freq = freq

    def __lt__(self, other):
        '''
        Sort by start time
        '''
        if type(other) is not Event:
            raise TypeError('Can only compare events with each other.')
        else:
            return self.start < other.start

    def __str__(self):
        now = utc.localize(datetime.utcnow())
        time_left = self.start - now

        # Get a string repr of the time remaining on the event
        if self.start < now < self.end:
            msg = 'ongoing'
        elif self.start > now:
            # In the future
            if self.all_day:
                msg = '{} days left'.format(time_left.days)
            elif time_left.days > 0:
                msg = '{} days left'.format(time_left.days)
            else:
                hours = time_left.seconds // (60 * 60)
                s = 's' if hours == 1 else ''
                msg = '{} hour{} left'.format(hours, s)
        else:
            msg = 'ended'

        # Mark recurring events
        recur = ''
        if self.recurring:
            recur = ': recurring [{}]'.format(self.freq)

        start = self.start.strftime('%Y-%m-%d (%H:%M)')

        return '{}: {} ({}{})'.format(start, self.summary, msg, recur)
