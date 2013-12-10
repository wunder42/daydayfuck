
$ = jQuery

angular.module('profile', []).config [
	'$routeProvider', ($routeProvider) ->
		$routeProvider.
		    when('/', {templateUrl: 'templates/home.html', controller: HomeCtrl}).
		    when('/movie', {templateUrl: 'templates/movie.html', controller: BookCtrl}).
		    when('/music', {templateUrl: 'templates/music.html', controller: MusicCtrl}).
		    when('/profile', {templateUrl: 'templates/profile.html', controller: ProfileCtrl}).
		    otherwise {redirectTo: '/'}
]

HomeCtrl = ($scope) ->

BookCtrl = ($scope) ->

MusicCtrl = ($scope) ->

ProfileCtrl = ($scope) ->

$ ->
	console.log 'start'

	$(".content").css {height:$(document).height()}