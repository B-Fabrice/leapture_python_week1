from pytz import timezone, country_names
from datetime import datetime

format = "%Y-%m-%d %H:%M:%S %Z%z"

#current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))

#current time in London
s = now_utc.astimezone(timezone('Europe/London'))
print(s.strftime(format))

# country code
for x in country_names:
    print(x)

