
console.log 'in coffee'

Storage::setObj = (key, obj) ->
	@setItem key, JSON.stringify(obj)

Storage::getObj = (key) ->
	JSON.parse @getItem(key)

class TodoApp

	constructor: ->
		console.log 'init TodoApp', @
		@display_items()
		@bind_listening()

	create_todo_item: (content) ->
		console.log 'create_todo_item'
		_timestamp = new Date().getTime()
		tid = Math.floor Math.random() * 1000000
		localStorage.setObj tid, {id: tid, con: content, timestamp:_timestamp, checked:false}
		_item = localStorage.getObj tid
		$('.to-do-header').after "<div><span class='label-info to-do-item' data-id='#{_item.id}'><input type='checkbox' class='to-do-check' checked='\
				#{if _item.checked then 'checked' else ''}'>#{_item.con}</span></div>"

	display_items: ->
		console.log 'display_items'
		for item in Object.keys(localStorage)
			_item = localStorage.getObj item
			$('.to-do-header').after "<div><span class='label-info to-do-item' data-id='#{_item.id}'><input type='checkbox' class='to-do-check' \
				#{if _item.checked then 'checked' else ''}>#{_item.con}</span></div>"

	bind_listening: =>
		pp = @
		$(".btn").click (e) ->
			console.log $(this).attr('data-status'), pp
			
			if $(this).attr('data-status') == 'add'
			    $(".to-do").show()
			    $(this).attr 'data-status', 'edit'
			else if $(this).attr('data-status') == 'edit'
			    console.log 'edit value:', $('.to-do').val() if $('.to-do').val() != ''

			    val = $('.to-do').val()
			    if val != '' then pp.create_todo_item(val)
			    console.log 'hehe'
			    $(".to-do").val('').hide()
			    $(this).attr 'data-status', 'add'

		$(".to-do-check").live 'click', (e) ->
			# if $(this).attr 'checked'
			console.log 'check:',$(this).attr 'checked'
			if $(this).attr('checked') == 'checked'
				$(this).parent().css 'text-decoration', 'line-through'
			else
			    $(this).parent().css 'text-decoration', ''



$ ->
	if not localStorage
		alert 'please use newest '

	app = new TodoApp()
	
