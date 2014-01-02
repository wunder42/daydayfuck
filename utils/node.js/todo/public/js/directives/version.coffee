define [], ->
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
		console.log 'startDrag', obj, obj.attr('startleft'), obj.attr('starttop')
		itemCopy.append obj.clone(true)
		obj.css 'opacity', 0
		itemCopy.css {opacity: 0.5, left: obj.attr('startleft') + 'px', top: obj.attr('starttop') + 'px', display: 'block'}

	drag = (obj, pos) ->
		itemCopy.css 'left', (pos.x - mouseOffset.offsetLeft)
		itemCopy.css 'top', (pos.y - mouseOffset.offsetTop)

	mouseOffsetElement = (obj, e) ->
		return {
			offsetLeft: e.pageX - obj.offset().left,
			offsetTop: e.pageY - obj.offset().top
		}

	mouseCoords = (e) ->
		return {
			x: e.pageX,
			y: e.pageY
		}

	isIn = (m, n) ->
		center = {
			x: m.offset().left + m.width() / 2,
			y: m.offset().top + m.height() / 2
		}

		return true if center.x > n.offset().left and center.y > n.offset().top and center.x < n.offset().left + n.width() and center.y < n.offset().top + n.height()
		return false

	beforeOrAfter = (m, n) ->
		center = {
			y: m.offset().top + m.height() / 2
		}
		return 'before' if center.y < (n.offset().top + n.height() / 2)
		return 'after'

	nextElement = (n) ->
		return item for item in n.nextAll() when item.nodeType == 1
		return null

	previousElment = (n) ->
		return item for item in n.prevAll() when item.nodeType == 1
		return null

	mouseDown = (e) ->
		t = $(e.target)	
		console.log t.attr 'class'
		if t.hasClass 'dragItem'
			curItem = t
			mouseOffset = mouseOffsetElement curItem, e
			startDrag curItem
		isMouseDown = true
		return false if t.hasClass 'itemCopy'

	mouseUp = (e) ->
		console.log 'mouseup', curItem.attr('class'), curItem.attr('startleft'), curItem.attr('starttop')
		curItem.css 'opacity', 1
		itemCopy.html ''
		itemCopy.css 'display', 'none'
		curItem = null
		isMouseDown = false

	updatePosition = ->
		for item in dragManager
			# console.log item, item.attr('class'), item.offset().left, item.width(), item.height()
			item.attr {startleft: item.offset().left, starttop: item.offset().top, startwidth: item.width(), startheight: item.height()}
			for i in item.children()
				i = $(i)
				# console.log i, i.attr('class'), i.offset().left, i.width(), i.height()
				i.attr {startleft: i.offset().left, starttop: i.offset().top, startwidth: i.width(), startheight: i.height()}

	mouseMove = (e) ->
		activeManager = null
		activeItem = null
		updatePosition()

		if isMouseDown and curItem
			mousePosition = mouseCoords e
			drag curItem, mousePosition

			for item in dragManager
				if isIn itemCopy, item
					activeManager = item
					break

			if activeManager
				for item in activeManager.children()
					item = $(item)
					if curItem.html() != item.html() and isIn itemCopy, item
						console.log curItem.html(), item.html()
						activeItem = item
						break

			if activeItem
				console.log 'abc', curItem.html(), activeItem.html(), beforeOrAfter(itemCopy, activeItem)
				if beforeOrAfter(itemCopy, activeItem) == 'before' and activeItem != nextElement(curItem)# and not activeItem.hasClass 'item-head' #activeItem.attr('class') != 'item-head label-info'
					# activeManager.insertBefore curItem, activeItem
					if activeItem.hasClass 'addCart'
						curItem.insertBefore previousElment(activeItem)
						return
					curItem.insertBefore activeItem
				else if beforeOrAfter(itemCopy, activeItem) == 'after' and activeItem.html() != $(previousElment(curItem)).html() #and not activeItem.hasClass 'addCart' #activeItem.attr('class') != 'addCart btn btn-default'
					# activeManager.insertBefore curItem, nextElement(activeItem)
					console.log 'aa', activeItem, $(previousElment(curItem)), curItem
					curItem.insertBefore nextElement(activeItem)
			else
				console.log 'false'
			# else if activeManager.children().length == 0
			#     activeManager.append curItem

	# $ ->
	stt = ->
		console.log 'start'
		initManager($("#dragContainer"))
		itemCopy = $("<div></div>")
		itemCopy.css {position: 'absolute', display: 'none', zindex: 100}
		$("body").append itemCopy
		console.log itemCopy

		$(document).mousedown(mouseDown).mousemove(mouseMove).mouseup(mouseUp)

		# updatePosition()

	return ['appVersion', ->
		return (scope, elm, attrs) ->
			console.log 'apple'
			stt()
	]

