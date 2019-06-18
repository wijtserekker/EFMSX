import matplotlib.pyplot as plt
import json
import datetime
import numpy as np
import seaborn as sns

FILENAME = 'json/fixed_history.json'

TIMESTAMP = 'ts'
ARTIST_NAME = 'master_metadata_album_artist_name'

ARTIST_THRESHOLD = 500
DAY_RANGE = (1, 366)  # Normally (1, 366)
MON_RANGE = (1, 2)  # Normally (1, 13)
YEAR = 2018
TS_FORMAT = '%Y-%m-%d %H:%M:%S'

TIMESCALE = 0


with open(FILENAME) as file:
    c_data = json.load(file)

data = c_data['data']

x_days = np.array([x for x in range(DAY_RANGE[0], DAY_RANGE[1])])
x_mons = np.array([x for x in range(MON_RANGE[0], MON_RANGE[1])])

artists_dict_days = {}
artists_dict_mons = {}
y_artists = []
y_labels = []


for field in data:

    if ARTIST_NAME in field.keys():
        artist_name = field[ARTIST_NAME]
        timestamp = field[TIMESTAMP][:-4]
        dt = datetime.datetime.strptime(timestamp, TS_FORMAT)
        tt = dt.timetuple()
        year = tt.tm_year
        day = tt.tm_yday
        mon = tt.tm_mon

        if year == YEAR:
            if artist_name not in artists_dict_days.keys():
                if day in range(DAY_RANGE[0], DAY_RANGE[1]):
                    artists_dict_days[artist_name] = np.zeros((DAY_RANGE[1] - 1,), dtype=int)
                if mon in range(MON_RANGE[0], MON_RANGE[1]):
                    artists_dict_mons[artist_name] = np.zeros((MON_RANGE[1] - 1,), dtype=int)
                    print(artist_name)

            artists_dict_days[artist_name][day - 1] += 1
            artists_dict_mons[artist_name][mon - 1] += 1


if TIMESCALE == 0:
    for artist_name in artists_dict_days.keys():
        if sum(artists_dict_days[artist_name]) > ARTIST_THRESHOLD:
            y_artists.append(artists_dict_days[artist_name])
            y_labels.append(artist_name)
if TIMESCALE == 1:
    for artist_name in artists_dict_mons.keys():
        if sum(artists_dict_days[artist_name]) > ARTIST_THRESHOLD:
            y_artists.append(artists_dict_mons[artist_name])
            y_labels.append(artist_name)


y_artists_np = np.vstack(y_artists)
# y_percent = y_artists_np
y_percent = y_artists_np / y_artists_np.sum(axis=0).astype(float) * 100

fig_size = plt.rcParams['figure.figsize']
fig_size[0] = 18
fig_size[1] = 9
plt.rcParams['figure.figsize'] = fig_size
plt.rcParams['figure.dpi'] = 300

# plt.figure(figsize=(16, 9), dpi=200)

sns.set_palette(sns.color_palette('hls', len(y_labels)))

fig, ax = plt.subplots()

if TIMESCALE == 0:
    ax.stackplot(x_days, y_percent, labels=y_labels)
if TIMESCALE == 1:
    ax.stackplot(x_mons, y_percent, labels=y_labels)

chart_box = ax.get_position()
# ax.set_position([chart_box.x0, chart_box.y0, chart_box.x1*0.1, chart_box.y1])
ax.legend(loc='upper center', bbox_to_anchor=(1.06, 1))
plt.show()

# print(artists_dict)







# "ts":"2012-09-23 18:56:13 UTC",                                                       TIMESTAMP
# "username":"1147860656",                                                              USERNAME
# "platform":"iOS 6.0 (iPod4,1)",                                                       PLATFORM
# "ms_played":"4970",                                                                   PLAY TIME ms
# "conn_country":"NL",                                                                  COUNTRY
# "ip_addr_decrypted":"94.215.158.175",                                                 IP ADDRESS
# "user_agent_decrypted":"unknown",                                                     USER AGENT
# "master_metadata_track_name":"Breakeven - Live At The Aviva Stadium, Dublin",         TRACK NAME
# "master_metadata_album_artist_name":"The Script",                                     ARTIST NAME
# "master_metadata_album_album_name":"#3 Deluxe Version",                               ALBUM NAME
# "reason_start":"fwdbtn",                                                              START REASON
# "reason_end":"fwdbtn",                                                                END REASON
# "shuffle":false,                                                                      SHUFFLE true/false
# "skipped":true,                                                                       SKIPPED true/false
# "offline":false,                                                                      OFFLINE true/false
# "offline_timestamp":"0",                                                              OFFLINE TS
# "incognito_mode":false,                                                               INCOGNITO MODE true/false
# "metro_code":"0",                                                                     METRO CODE
# "longitude":0,                                                                        LONGITUDE
# "latitude":0                                                                          LATITUDE

