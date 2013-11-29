$ = jQuery

$ ->
	$("#ttt").click((e) ->
		# this.preventDefault()
		# $.post "/upload", {name: 'kknife'}
		$.get '/u', {name: 'knife'}, (data) ->
			console.log data
	)
# $("#sm").ajaxStart(-> $(this).show()).ajaxComplete -> $(this).hide()



	$("#sm").click((e) ->
		e.preventDefault()
		$.ajaxFileUpload {
			url: '/',
			secureuri: false,
			fileElementId:'uf',
			dataType: 'json',
			success: (data, status) ->
		    	console.log data
		    error: (data, status, e) ->
		    	console.log data
		}
	)
	# args = {
	# 	_xsrf: getcookie("_xsrf")
	# }
	# $.post "/", args, ((data) -> console.log data)




getcookie = (name) ->
	r = document.cookie.match("\\b" + name + "=([^;]*)\\b")
	if r then r[1] else null