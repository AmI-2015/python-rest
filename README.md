Flask Music Server
=======================

A Simple REST music server for introducing REST and Flask in Python. It can be run from the command line by typing:

```python flask_music_server.py```

or

```./flask_music_server.py```

It provides basic support to single track and playlists.

### API


**Resource:** tracks
**Url:** /music/api/v1.0/tracks
**Description:** Returns the list of all tracks currently available on the server, without paging
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