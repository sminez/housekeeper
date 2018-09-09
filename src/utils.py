'''
Utility functions for housekeeper
'''
import concurrent.futures
from datetime import date, timedelta
from calendar import Calendar, monthcalendar


def run_many(func, args_list, max_threads=10, fail_quiet=False):
    '''
    Run a function multiple times with different inputs,
    each on its own thread.
    Intended for use with blocking IO
    '''
    results = []
    max_workers = min([max_threads, len(args_list)])

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = (
            ex.submit(func, *args)
            for args in args_list
        )

        for f in concurrent.futures.as_completed(futures):
            try:
                res = f.result()
                if res:
                    results.append(res)
            except Exception as e:
                if fail_quiet:
                    pass
                else:
                    raise e

    return results


def run_many_tagged(func, tag_args, max_threads=10, fail_quiet=False):
    '''
    Run a function multiple times with different inputs,
    each on its own thread.
    Intended for use with blocking IO
    '''
    def tagged(tag, func):
        '''Helper to maintain tags'''
        def _inner(*args):
            return tag, func(*args)
        return _inner

    results = {}
    max_workers = min([max_threads, len(tag_args)])

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = (
            ex.submit(tagged(tag, func), *args)
            for (tag, args) in tag_args
        )

        for f in concurrent.futures.as_completed(futures):
            try:
                tag, res = f.result()
                if res:
                    results[tag] = res
            except Exception as e:
                if fail_quiet:
                    pass
                else:
                    raise e

    return results


def parse_amazon_date_to_range(d):
    '''
    Convert an AMAZON.DATE into a start/end date pair.

    the payload from Amazon is one of the following:
      specific date  -->  20XX-XX-XX
      week           -->  20XX-WXX   (i.e year-week_number)
      month          -->  20XX-XX    (i.e. year-month_number)
    '''
    d = d.split('-')

    if len(d) == 3:
        # Specific date
        d = map(int, d)
        start = date(d[0], d[1], d[2])
        return start, start + timedelta(hours=24)

    if d[1].startswith('W'):
        # A week number
        c = Calendar()
        # A list of weeks. Each week is a list of datetime.date instances
        weeks = sum(c.yeardatescalendar(int(d[0]), 55)[0], [])
        week_num = int(d[1][1:])
        w = weeks[week_num]
        return w[0], w[-1]
    else:
        # A month
        y, m = map(int, d)
        month_cal = sum(monthcalendar(y, m))
        end = len([d for d in month_cal if d != 0])
        return date(y, m, 1), date(y, m, end)
