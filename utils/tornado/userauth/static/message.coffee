
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
		else if msg.type == 3
			console.log '3'
			_from = if msg.from == $(".username").text() then 'me' else msg.from
			_h = "<div class='alert-box info'>#{msg.content}-->#{_from}</div>"
			$(".msghub").prepend  _h

}

getcookie = (name) ->
	r = document.cookie.match("\\b" + name + "=([^;]*)\\b")
	if r then r[1] else null

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

	$(".close").click (e) ->
		e.preventDefault()
		$(this).parent("div").hide "slow"

	$(".tozoom").click (e) ->
		console.log 'send'
		# e.preventDefault()
		_t = $(".cc").val()
		if not _t
			alert('send error')
			$(".cc").value ""
			return
		# args = "_xsrf=#{getcookie("_xsrf")}&content=#{_t}"
		# console.log args
		# $.post "/z/msg", args, (data, textStatus, xhr) ->
		# 	console.log textStatus, data
		# console.log {content:_t, userid:$.cookie("userid")}
		updater.socket.send JSON.stringify {content:_t, 'userid':$.cookie("userid")}

	$(".msg-send-btn").click (e) ->
		console.log 'msg-send-btn'

		_flag = $(".msg-send-content")
		_content = _flag.val()
		_from = $('#chat').text()
		_to = $("#chat-with").text()
		args = {'_xsrf': getcookie('_xsrf'),'from':_from, 'to':_to, 'content':_content}

		console.log args

		$.post '/chat/c', args, (data, textStatus, xhr) ->
			console.log data, textStatus
			_data = $.parseJSON data
			if not _data['result']
				return
			_ihtml = $("<li>#{_content}</li>")
			$(".msg-content-ul").append _ihtml


