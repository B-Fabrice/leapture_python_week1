from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

now = parse("Sat Oct 11 17:13:46 UTC 2003")
today = now.date()
year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
rdelta = relativedelta(easter(year), today)
print("Today is: %s" % today)
#Today is: 2003-10-11
print("Year with next Aug 13th on a Friday is: %s" % year)
#Year with next Aug 13th on a Friday is: 2004
print("How far is the Easter of that year: %s" % rdelta)
#How far is the Easter of that year: relativedelta(months=+6)
print("And the Easter of that year is: %s" % (today+rdelta))
