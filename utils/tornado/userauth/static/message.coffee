
$ = jQuery

updater = {
	socket: null,

	start: ->
		url = 'ws://' + location.host + '/message'
		updater.socket = new WebSocket(url)
		updater.socket.onmessage = (e) ->
			console.log e
			updater.showMessage JSON.parse(e.data)

	showMessage: (msg) ->
		console.log msg
		if msg.type == 1
			console.log '1'
			$(".online-num").text parseInt($(".online-num").text()) + msg.addNum
		else if msg.type == 2
		    console.log '2'
		    $(".sysinfo").text msg.msg

}

# class update
# 	socket: null
# 	start: ->
# 		console.log 'xx'
# 	showMessage: (msg) ->
# 		console.log 'yy'

$ ->
	console.log 'message in...'
	$("#send").click (e) ->
		updater.socket.send JSON.stringify({type:1})
	updater.start()


