
$ = jQuery

checkItem = (e) ->
	


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
	$(".itembb").mousedown((e) ->
		e.preventDefault()
		t = $(this)
		$(this).css {position:'fixed', cursor:"move", "-webkit-transform":"rotate(10deg)"}

		x = event.pageX
		y = event.pageY
		a = $(this).offset().top
		b = $(this).offset().left
		
		console.log 'mousedown', x, y, a, b, t
		if e.which == 1
			$("html").mousemove (e) ->
				t.css 'top', e.pageY - y + a
				t.css 'left', e.pageX - x + b
	).mouseup((e) ->
		console.log 'mouseup'
		$(this).css {"-webkit-transform":"rotate(0deg)"}
		$("html").unbind 'mousemove'
	)	