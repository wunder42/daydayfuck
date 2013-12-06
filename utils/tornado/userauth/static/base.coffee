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

	$("#login").click (e) ->
		e.preventDefault()
		# args = {"_xsrf": getcookie("_xsrf")} 
		args = "_xsrf=#{getcookie("_xsrf")}&"+ $("#loginForm").formSerialize()
		$.post '/login', args, (data, textStatus, xhr) ->
			data = $.parseJSON data 
			if data['successful']
				location.href = '/'
			else
			    console.log 'login error'


	$("#register").click (e) ->
		e.preventDefault()
		args = "_xsrf=#{getcookie("_xsrf")}&"+ $("#registerForm").formSerialize()
		$.post '/register', args, (data, textStatus, xhr) ->
			data = $.parseJSON data 
			if data['successful']
				location.href = '/login'
			else
			    console.log 'register error'





getcookie = (name) ->
	r = document.cookie.match("\\b" + name + "=([^;]*)\\b")
	if r then r[1] else null