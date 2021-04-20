from pypresence import Presence
import sys, time, calendar

try:
	RPC = Presence('CLIENT_ID')
	RPC.connect()
	RPC.update(
		state = "STATE HERE",
		details = "DETAILS HERE",
		start = calendar.timegm(time.gmtime()),
		end = None,
		large_image = "LARGE IMAGE NAME",
		large_text = "LARGE IMAGE TEXT HERE",
		small_image = "SMALL IMAGE NAME",
		small_text = "SMALL IMAGE TEXT HERE",
		buttons = [
			{"label": "Buttons 1", "url": "https://github.com/vincent-coding"},
			{"label": "Buttons 2", "url": "https://github.com/vincent-coding/Custom-Discord-Rich-Presence"}
		],
		party_id = None,
		party_size = None
	)
except:
	sys.exit("For the program to work, Discord must be running!")

while True:
	time.sleep(15)
