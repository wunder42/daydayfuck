'use strict'

define [], ->
	LoginController = ($scope, $http, $location) ->
		$scope.user = {
			username: 'tt',
			password: '9090'
		}
		$scope.requestLogin = ->
			$http.post('/u/login', {men: 'cike'})

	return LoginController