import datetime
import pytz

d = datetime.date(2019, 8, 1)
tday = datetime.date.today()

# print(tday.weekday())  # Monday = 0; Sunday = 6
# print(tday.isoweekday())  # Monday = 1; Sunday = 7

tdelta = datetime.timedelta(days=7)
# print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

birthday = datetime.date(2019, 12, 25)
till_bday = birthday - tday

# print(till_bday.days)

# t = datetime.time(9, 30, 45, 100000)
# dt = datetime.datetime(2019, 7, 26, 9, 30, 45, 100000, tzinfo=pytz.UTC)

# print(dt + tdelta)

# dt_today = datetime.datetime.today()  # current local datetime with time zone of none
# dt_now = datetime.datetime.now()  # we can pass in time zone
# dt_utcnow = datetime.datetime.utcnow()  # current UTC time; not time zone aware

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_cst = dt_utcnow.astimezone(pytz.timezone("US/Central"))
# print(dt_cst)

# for tz in pytz.all_timezones:
#     print(tz)

# dt_local = datetime.datetime.now()  # naive datetime
# cst_tz = pytz.timezone("US/Central")
# dt_local = cst_tz.localize(dt_local)  # make it time zone aware

dt_cst = datetime.datetime.now(tz=pytz.timezone("US/Central"))
print(dt_cst.strftime("%B %d, %Y"))

dt_str = "August 07, 2019"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
