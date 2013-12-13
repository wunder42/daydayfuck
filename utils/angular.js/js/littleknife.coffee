
$ = jQuery

angular.module('gtd', []).config [
	'$routeProvider', ($routeProvider) ->
		$routeProvider.
		    when('/', {templateUrl: 'templates/task.html', controller: TaskCtrl, resolve: TaskCtrl.resolve}).
		    when('/movie', {templateUrl: 'templates/movie.html', controller: BookCtrl}).
		    when('/music', {templateUrl: 'templates/music.html', controller: MusicCtrl}).
		    when('/profile', {templateUrl: 'templates/profile.html', controller: ProfileCtrl}).
		    otherwise {redirectTo: '/'}
]

TaskCtrl = ($scope) ->

TaskCtrl.resolve = {
	delay: ($q) ->
    	delay = $q.defer()
    	load = ->
	        $.getScript 'js-foundation/drag-drop.js', ->
	        	delay.resolve()
    	load()
    	delay.promise
}

BookCtrl = ($scope) ->

MusicCtrl = ($scope) ->

ProfileCtrl = ($scope) ->

$ ->
	console.log 'gtd, start'