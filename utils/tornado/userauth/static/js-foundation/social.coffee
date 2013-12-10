
$ = jQuery

angular.module('social', []).config [
	'$routeProvider', ($routeProvider) ->
		$routeProvider.
		    when('/', {templateUrl: '/static/htmls/friend.html', controller: FriendCtrl}).
		    when('/chat', {templateUrl: '/static/htmls/chat.html', controller: ChatCtrl}).
		    when('/love', {templateUrl: '/static/htmls/love.html', controller: LoveCtrl}).
		    when('/game', {templateUrl: '/static/htmls/game.html', controller: GameCtrl}).
		    when('/app', {templateUrl: '/static/htmls/app.html', controller: AppCtrl}).
		    otherwise {redirectTo: '/'}
	] 

FriendCtrl = ($scope) ->

ChatCtrl = ($scope) ->
	$scope.chageit ->
		console.log 'dayday..'

LoveCtrl = ($scope) ->

GameCtrl = ($scope) ->

AppCtrl = ($scope) ->

chageit = ->
	console.log 'daydayfuck'


$ ->
	console.log 'social start'

	$(".left-off-canvas-toggle").click (e) ->
		e.preventDefault()
		$(".off-canvas-wrap").toggleClass 'move-right'
	$(".exit-off-canvas").click (e) ->
		e.preventDefault()
		$(".off-canvas-wrap").toggleClass 'move-right'

	$(".content-main").css 'height', $(window).height() - $(".tab-bar").height()
	console.log 'yyyy'
	$(".chat-item").click (e) ->
		console.log 'xx'
		e.preventDefault()

