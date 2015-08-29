
easyrtc.setStreamAcceptor( function(callerEasyrtcid, stream) {
	var video = document.getElementById('remoteVideo');
	easyrtc.setVideoObjectSrc(video, stream);
});

easyrtc.setOnStreamClosed( function (callerEasyrtcid) {
	easyrtc.setVideoObjectSrc(document.getElementById('remoteVideo'), "");
});

function init_video(room_id, is_linkage) {
	easyrtc.setSocketUrl("//vlab.cecs.anu.edu.au:80");
	easyrtc.setRoomOccupantListener( roomListener);

	if (!is_linkage) {
		easyrtc.enableAudio(false);
		easyrtc.enableVideo(false);
	}

	console.log(room_id);

	var failure = function (err, msg) {
		alert("Can't connect to Video server. Try disabling AdBlock and PrivacyBadger Extensions for this URL.");
		console.log(msg);
	}

	easyrtc.joinRoom(room_id, null,
		function(room) {
			console.log("Joined room " + room);	},
		function(err, msg, room) {
			failure(err, msg);}
	);

	easyrtc.connect('engn8537', 
		function(myId) {
	    	console.log("My easyrtcid is " + myId);},
	    failure
	);
}

function roomListener(roomName, otherPeers) {
    for(var i in otherPeers) {
        performCall(i);
        break;
    }
}

function performCall(easyrtcid) {
	easyrtc.call(
		easyrtcid,
		function(easyrtcid) { console.log("completed call to " + easyrtcid); },
		function(errorMessage) { console.log("err:" + errorMessage); },
		function(accepted, bywho) {
			console.log((accepted?"accepted":"rejected")+ " by " + bywho);
		}
	);
}
