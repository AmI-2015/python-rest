Flask Music Server
=======================

A Simple REST music server for introducing REST and Flask in Python. It can be run from the command line by typing:

``` python flask_music_server.py ```
or

```./flask_music_server.py ```

It provides basic support to single track and playlists.

### API
-------

**Resource:** tracks

**Url:** /music/api/v1.0/tracks

**Description:** The tracks currently available on the server, without paging

**Method:** GET - Retrieves the list of available tracks

**Example Response:**

```
{"tracks": [
	{
	"id": 0,
	"metadata": 
		{"album": "NRJ Hit Music Only 2014",
		"artist": "Clean Bandit feat. Jess Glynne",
		"genre": "Top 40",
		"title": "Rather Be"},
	"path": "/home/bonino/Music/204. Clean Bandit feat. Jess Glynne - Rather Be.flac"},
	{
	"id": 1,
	"metadata": 
		{"album": "You A Lie",
		"artist": null,
		"genre": "Unknown",
		"title": "A pair of glasses"},
	"path": "/home/bonino/Music/Comaneci - You A Lie/Comaneci - You A Lie/01-A pair of glasses.mp3"},
	{
	"id": 2,
	"metadata": 
		{"album": "You A Lie",
		"artist": null,
		"genre": "Unknown",
		"title": "Green"},
	"path": "/home/bonino/Music/Comaneci - You A Lie/Comaneci - You A Lie/04-Green.mp3"},
...
}
```

-------

**Resource:** player

**Url:** /music/api/v1.0/player

**Description:** The Flask Music Player

**Method:** GET - Get the current player status

**Example Response:**

```
{
"current": {
	"id": 3,
	"metadata": 
		{"album": "You A Lie",
		"artist": null,
		"genre": "Unknown",
		"title": "Not"},
	"path": "/home/bonino/Music/Comaneci - You A Lie/Comaneci - You A Lie/03-Not.mp3"},
"queue": [
	{
	"id": 55,
	"metadata": 
		{"album": "Ricks Road",
		"artist": "Texas",
		"genre": "Pop",
		"title": "Winter's End"},
	"path": "/home/bonino/Music/Texas/1993 Texas-Ricks Road/12 Texas-Winter's End.mp3"},
	{
	"id": 63,
	"metadata": 
		{"album": "The all time greatest Christma",
		"artist": null,
		"genre": "Pop",
		"title": "Silent Night, Holy Night"},
	"path": "/home/bonino/Music/Various/The All Time Greatest Christmas Songs/223-va_-_mahalia_jackson_-_silent_night_holy_night-mip.mp3"},
	{
	"id": 77,
	"metadata": 
		{"album": "The all time greatest Christma",
		"artist": null,
		"genre": "Pop",
		"title": "this is the Time"},
	"path": "/home/bonino/Music/Various/The All Time Greatest Christmas Songs/108-va_-_michael_bolton_(duet_with_wynonna)_-_this_is_the_time-mip.mp3"}
	],
"status": "playing"}
```

**Method:** PUT - send a command to the player

**Allowed commands**: play, stop, next

**Example command**:

```
{
	"command" : "play",
	"playlist" : {"tracks":[3, 55, 63, 77]}
}

-- or --

{
	"command" : "play",
	"track" : "39"
}

-- or --

{
	"command" : "stop"
}

-- or --

{
	"command" : "next"
}
```
