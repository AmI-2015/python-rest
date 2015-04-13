'''
Created on Apr 13, 2015

@author: bonino
'''
import signal
from flask import Flask, jsonify, abort, request, render_template
from musiclib import TrackList, Player

app = Flask(__name__)
track_list = TrackList()
player = Player()

# handle sigterm
def cleanup_on_term():
    player.exit()

# attach cleanup
signal.signal(signal.SIGTERM, cleanup_on_term)

# --------- SIMPLE WEB APP ----------------------------

@app.route('/')
def index():
    return render_template('index.html')

# ---------  REST SERVER ------------------------------

@app.route('/music/api/v1.0/tracks', methods=['GET'])
def get_tracks():    
        
    # return the track data
    return jsonify({'tracks': [track.jsonifiable() for track in track_list.tracks]})

@app.route('/music/api/v1.0/tracks/<int:track_id>', methods=['GET'])
def get_track(track_id):
    
    # get the track
    track = track_list.getTrack(track_id)
    
    # if no track has the given id return 404 not found
    if track == -1:
        abort(404)
    # convert the track in its json representation
    return jsonify({'track': track.jsonifiable()})

@app.route('/music/api/v1.0/player', methods=['PUT'])
def control_player():
    # get the request body
    play_request = request.json
    
    if('command' in play_request):        
        
        #get the command
        command = play_request['command']
            
        # PLAY
        if command.lower() == 'play':          
            # check direct track if any
            if "track" in play_request:
                
                # get the track id
                track_id = play_request["track"]
               
                # get the track
                track = track_list.getTrack(track_id)
               
                if(track != -1):
                    # debug
                    print ("playing file: \"%s\"\n" % track.path)
               
                    # play the track
                    player.load_and_play(track)  
                
            # check playlist if any
            elif "playlist" in play_request:
                # no multiple playlist supported...just play it
                
                # get the playlist
                playlist = play_request["playlist"];
               
                # check for tracks
                if playlist["tracks"] != None:
                    # prepare the playlist holding full track information
                    full_playlist = []
                    
                    # for all tracks
                    for track in playlist["tracks"]:
                        # get the track
                        full_track_data = track_list.getTrack(int(track))
                        
                        # if valid add to the play list
                        if(full_track_data != -1):
                            # add the track
                            full_playlist.append(full_track_data)
                        
                    if(len(full_playlist) > 0):
                        # switch playlist
                        player.load_playlist(full_playlist) 
                        
            elif len(player.current_playlist) > 0:
                
                #play existing playlist
                if(player.currently_playing_id < len(player.current_playlist)):
                    #get the current id
                    target_id = player.currently_playing_id
                    
                    #get the current playlist
                    target_playlist = [track for track in player.current_playlist]
                    
                    #reschedule track playing
                    player.load_playlist(target_playlist)
                    
                    #skip to the right track
                    while (player.currently_playing_id != target_id):
                        player.next()
                else:
                    # load and start from the beginning
                    player.load_playlist(player.current_playlist)
                
                
        # STOP  
        elif command.lower() == 'stop':
            # stop playing
            player.stop()
        # NEXT
        elif command.lower() == 'next':
            # skip to next track
            if(len(player.current_playlist)>0):
                player.next()
            else:
                abort(404)
                
                
                
    return  jsonify({"status":player.status, "current" : player.currently_playing.jsonifiable(), "queue":[track.jsonifiable() for track in player.current_playlist[(player.currently_playing_id+1):]]})

if __name__ == '__main__':
    # initialize the available tracks
    track_list.addTracks(track_list.scan("/home/bonino/Music"))
    
    # run flask
    app.run(debug=True)
    pass
