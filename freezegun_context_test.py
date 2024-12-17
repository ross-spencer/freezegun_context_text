"""Freezegun test"""

import os
from datetime import timezone as dt_tz
from datetime import datetime
import freezegun
from multiprocessing import Pool

def test_patched_time(d):
    import freezegun
    from datetime import datetime
    from django.utils import timezone
    with freezegun.freeze_time(d):
        print(d, '|', datetime.now(dt_tz.utc), '|', timezone.now())


test_data = [
    "2020-01-01",
    "2019-02-01",
    "2018-01-01",
    "2017-01-01",
    "2016-01-01",
    "2015-01-01",
    "2014-01-01",
    "2013-01-01",
    "2012-01-01",
]


print("Out of freezegun context")
p = Pool(8)
p.map(test_patched_time, test_data)
p.close()
p.join()

print("\nIn freezegun context")
with freezegun.freeze_time(None):
    p = Pool(8)
    p.map(test_patched_time, test_data)
    p.close()
    p.join()
