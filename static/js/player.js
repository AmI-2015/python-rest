$(document).ready(function() {
	attachPlayHandler();
	attachStopHandler();
	getStatus();
	setInterval(getStatus, 2000);
	loadTracks();
});

function attachPlayHandler() {
	// attach the handler for the play button
	$("#play").click(function() {

		// get the selected option
		$("#tracks option:selected").each(function() {

			// load the layer data
			playTrack($(this).val());
		});

		// reset the combobox status
		$(".combobox-container .dropdown-toggle").mouseover().click();

		// block the form submission
		return false;
	});
}

function attachStopHandler() {
	// attach the handler for the play button
	$("#stop").click(function() {
		stopTrack();
	});
}

function playTrack(track_id) {
	$.ajax({
		url : 'music/api/v1.0/player',
		type : 'PUT',
		data : '{"command":"play","track":"' + track_id + '"}',
		contentType : 'application/json',
		dataType : 'json',
		success : function(data) {
			showStatus(data);
		}
	});
}

function stopTrack() {
	$.ajax({
		url : 'music/api/v1.0/player',
		type : 'PUT',
		data : '{"command":"stop"}',
		contentType : 'application/json',
		dataType : 'json',
		success : function(data) {
			showStatus(data);
		}
	});
}

function getStatus(){
	$.get("music/api/v1.0/player", function(data) {
		showStatus(data);
	});
}

function loadTracks() {
	$.get("music/api/v1.0/tracks", function(data) {

		// parse json
		// json_tracks = JSON.parse(data);

		// extract and render tracks
		showTracks(data.tracks);
	});
}
/**
 * Renders the given tracks as a searchable combo box
 * 
 * @param tracks
 *            The available tracks
 */
function showTracks(tracks) {

	// get the process selection drop down
	var dropdown = $('#tracks');

	// populate the dropdown
	for ( var i in tracks) {

		// generate the option entry carrying the above extracted processId
		var option = document.createElement("option");
		option.setAttribute("value", tracks[i].id);

		// generate the "readable" process name to use as the option value
		option.innerHTML = (tracks[i].metadata.artist != null ? tracks[i].metadata.artist
				: "no artist")
				+ " - " + tracks[i].metadata.title

		// add the new option to the dropdown list
		dropdown.append(option);
	}

	// at the end, convert the HTML <select> tag into a searchable combobox.
	dropdown.combobox();
}

function showStatus(data) {
	//create the labels (bootstrap) showing the current track and the current status
	var status = "<span class=\"label label-success\">"

	//compose the track information
	if (data.current.metadata != undefined) {
		if (data.current.metadata.artist != null)
			status = status + data.current.metadata.artist + " - ";
		if (data.current.metadata.title != null)
			status = status + data.current.metadata.title
	} else {
		status = status + data.current
	}

	//compose the status information
	status = status + "</span> <span class=\"label label-info\">"
			+ data.status + "</span>";
	
	//show the status
	$("#status").html(status);
}