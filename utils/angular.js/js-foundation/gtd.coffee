
$ = jQuery


$ ->
	console.log 'gtd start'

	$(".left-off-canvas-toggle").click (e) ->
		e.preventDefault()
		$(".off-canvas-wrap").toggleClass 'move-right'
	$(".exit-off-canvas").click (e) ->
		e.preventDefault()
		$(".off-canvas-wrap").toggleClass 'move-right'

	### init min-height ###
	$(".content-main").css 'height', $(window).height() - $(".tab-bar").height()

	### deal with drag action ###
	$(".item").mousedown((e) ->
		t = $(this)
		$(this).css {position:'absolute', cursor:"pointer", "-webkit-transform":"rotate(10deg)"}

		x = event.pageX
		y = event.pageY
		a = $(this).offset().top
		b = $(this).offset().left
		
		console.log 'mousedown', x, y, a, b, t
		if e.which == 1
			$("html").mousemove (e) ->
				console.log e.pageX, e.pageY
				t.css 'top', e.pageY - y + a
				t.css 'left', e.pageX - x + b
	).mouseup((e) ->
		$(this).css {"-webkit-transform":"rotate(0deg)"}
		$("html").unbind 'mousemove'
	)	