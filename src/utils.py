'''
Utility functions for housekeeper
'''
import concurrent.futures


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
