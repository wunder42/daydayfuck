'use strict'

define [], ->
	LoginController = ($scope, $http, $location) ->
		$scope.user = {
			username: '',
			password: ''
		}

		$scope.requestLogin = ->
			$http.post('/u/login', {username: $scope.user.username, password: $scope.user.password, _xsrf: getcookie('_xsrf')})
			    .success (data, status, headers, config) ->
			    	console.log 'success login post'
			    	$scope.user.username = ''
		    		$scope.user.password = ''
			    	if data.status == 'OK'
			    		window.location.href = '/#/tasks'
			    .error (data, status, headers, config) ->
			    	console.log 'error'

		$http.get('/u/login')
		    .success (data, status, headers, config) ->
		    	console.log 'success login get', data
		    	if data.status == 'OK'
		    		window.location.href = '/#/tasks'

		getcookie = (name) ->
		    r = document.cookie.match "\\b" + name + "=([^;]*)\\b"
		    if r then r[1] else null
	return LoginController