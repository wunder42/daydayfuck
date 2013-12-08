
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