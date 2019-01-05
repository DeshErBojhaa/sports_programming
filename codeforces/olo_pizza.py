# Handle json formating issue
# NOTE: Not using external libraries for implementing Backoff was intentional
from collections import Counter
import datetime
import functools
import json
import sys
import time
import urllib


_TOPPING_API_ENDPOINT = 'http://files.olo.com/pizzas.json'

def _log_giveup(details):
    target = details['target']
    tries = details['tries']

    msg = f'Giving up {target} (...) after {tries} tries'
    exception_detail = details['exception']

    # Two small string concatenation does not have any performance impact
    #TODO: Implement Logging in production
    print(msg + exception_detail)


def _get_sleep_time(tries, elapsed, max_time):
    expected_wait = 2 ** tries
    return max(min(expected_wait, max_time - elapsed), 0)


def backoff(func=None, *, max_tries=2, max_time=10):
    if func is None:
        return functools.partial(backoff, max_tries=max_tries, max_time=max_time)

    @functools.wraps(func)
    def retry(*args, **kwargs):
        tries = 0
        start = datetime.datetime.now()
        while True:
            tries += 1
            time_delta = datetime.datetime.now() - start
            elapsed = time_delta.total_seconds()
            details = {'target': func.__name__, 'tries': tries}

            try:
                ret = func(*args, **kwargs)
                return ret
            except Exception:
                max_tries_exceeded = (tries == max_tries)
                max_time_exceeded = (max_time is not None and
                                     elapsed >= max_time)

                if max_tries_exceeded or max_time_exceeded:
                    details.update({'exception': ' could not connect to the server'})
                    _log_giveup(details)
                    return []

                seconds = _get_sleep_time(tries -1, elapsed, max_time)
                print(f'Attempet# {tries} Failed. Retrying after {seconds} seconds.')
                time.sleep(seconds)
            
        return []
    return retry


@backoff(max_tries=4, max_time=60)
def get_topping_from_api():
    with urllib.request.urlopen(_TOPPING_API_ENDPOINT) as api:
        return json.load(api)
    

_TOPPINGS = get_topping_from_api()
cnt = Counter()

for topping in _TOPPINGS:
    # Toping order does not matter. (Beef, Ham) and (Ham, Beef) are equivalent.
    # Observing the dataset it's clear that case folding is not necessary
    sorted_toppings = sorted(topping.get('toppings', []))
    if not sorted_toppings:
        raise ValueError('Topping does not exists')

    cnt[tuple(sorted_toppings)] += 1

max_len = -1
topping_stat = []
for i, val in enumerate(cnt.most_common(20)):
    toppings = ', '.join(x for x in val[0])
    count = val[1]
    max_len = max(max_len, len(toppings))
    topping_stat.append((i, toppings, count))

print(f'Rank {i+1:3}  Topping {toppings:30} Count {val[1]:>4}')
print(f'| Rank |{:^max_len}| Count |')
