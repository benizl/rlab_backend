
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

	easyrtc.connect(app_id, 
		function(myId) {
	    	console.log("My easyrtcid is " + myId);}, 
	    function(errorCode, errText) {
			console.log(errText);}
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
