
$ = jQuery
dragManager = []
curItem = null
itemCopy = null
isMouseDown = false
mouseOffset = null
mousePosition = null
activeManager = null
activeItem = null

initManager = (obj) ->
	dragManager.push($(x)) for x in obj.children()
	console.log dragManager


startDrag = (obj) ->
	itemCopy.append obj.clone(true)
	obj.css 'opacity', 0
	itemCopy.css {opacity: 0.5, left: obj.attr('startLeft'), top: obj.attr('startTop'), display: 'block'}
	console.log 'startDrag', itemCopy

drag = (obj, pos) ->
	itemCopy.css 'left', pos.x - mouseOffset.offsetLeft
	itemCopy.css 'top', pos.x - mouseOffset.offsetTop

mouseOffsetElement = (obj, e) ->
	return {
		offsetLeft: e.pageX - obj.offsetLeft,
		offsetTop: e.pageY - obj.offsetTop
	}

mouseCoords = (e) ->
	return {
		x: e.pageX,
		y: e.pageY
	}

mouseDown = (e) ->
	t = $(e.target)	
	console.log t.attr 'class'
	if t.attr('class')== 'dragItem'
		curItem = t
		mouseOffset = mouseOffsetElement curItem, e
		startDrag curItem
	isMouseDown = true
	return false if t.attr('class') == 'itemCopy'

updatePosition = ->
	for item in dragManager
		item.attr {startLeft: item.css('offsetLeft'), startTop: item.css('offsetTop'), startWidth: item.css('offsetWidth'), startHeight: item.css('offsetHeight')}
		for i in item.children()
			i = $(i)
			i.attr {startLeft: i.css('offsetLeft'), startTop: i.css('offsetTop'), startWidth: i.css('offsetWidth'), startHeight: i.css('offsetHeight')}

mouseMove = (e) ->
	activeManager = null
	activeItem = null
	updatePosition()

	if isMouseDown and curItem
		mousePosition = mouseCoords e
		drag curItem, mousePosition

$ ->
	console.log 'start'
	initManager($("#dragContainer"))
	itemCopy = $("<div></div>")
	$("body").append itemCopy
	console.log itemCopy

	$(document).mousedown(mouseDown).mousemove(mouseMove)
