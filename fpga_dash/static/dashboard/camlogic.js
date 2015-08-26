
easyrtc.setStreamAcceptor( function(callerEasyrtcid, stream) {
	var video = document.getElementById('remoteVideo');
	easyrtc.setVideoObjectSrc(video, stream);
});

easyrtc.setOnStreamClosed( function (callerEasyrtcid) {
	easyrtc.setVideoObjectSrc(document.getElementById('remoteVideo'), "");
});

function init_video(app_id, is_linkage) {
	easyrtc.setSocketUrl(":8080");
	easyrtc.setRoomOccupantListener( roomListener);

	if (!is_linkage) {
		easyrtc.enableAudio(false);
		easyrtc.enableVideo(false);
	}

	var connectSuccess = function(myId) {
	    console.log("My easyrtcid is " + myId);
	}

	var connectFailure = function(errorCode, errText) {
		console.log(errText);
	}

	easyrtc.initMediaSource(
		function(){        // success callback
			var selfVideo = document.getElementById("localVideo");
			easyrtc.setVideoObjectSrc(selfVideo, easyrtc.getLocalStream());
			easyrtc.connect(app_id, connectSuccess, connectFailure);
		},
		connectFailure
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
