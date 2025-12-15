from os import getenv
from data import THE_ALTS


#----------------------------------- REQUIRED CODES --------------------------------------#

API_ID = int(getenv("API_ID", "21750155"))
API_HASH = getenv("API_HASH", "b6de6d142818b53e796b9a6ea570d2a7")
SESSION1 = getenv("BAGCdMkAlXGEITuudCOEPZhl2jYikf6Y9Y9SNZcRv8yOjZqfx9M3k-mHJg1m4o7Kz7hbFdJ8OBPwC9AMFF-o44tXDqYbONlVxXx6gliqrN1tcCu0vCf9Fh2DateIK2-ZKNpXe9ibULZ3eI791PZRk2xP0-qV79RUHleXLcDwBpPHj9n38U18vf-2paVsRmKOohkT1RNoCkMvq22G5-F2RtKs1GYmjO7WzxXu1skCwP2dO9mWnZZ673tkzxk2VzY9e5Ef_gf8N7v56YOclpT5IOMwRWsvBPudRQZNUShAqHHVkEJS1dRCpgXefCCJ0lri7pmEDPd23CfQ4TA9QB000eDDX_hu3QAAAAHEWVRoAA")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/dfe3bf37f969e4464393b.jpg")
OWNER_ID = int(getenv("OWNER_ID", "6474527080"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", "5655003867").split(" ")))
SUDO_USERS.append(OWNER_ID)

for x in THE_ALTS:
    SUDO_USERS.append(x)

SESSIONS = [SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10]
