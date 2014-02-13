'use strict'

define [], ->
	LoginController = ($scope, $http, $location) ->
		$scope.user = {
			username: '',
			password: ''
		}

		$scope.requestLogin = ->
			$http.post('/u/login', {username: $scope.user.username, password: $scope.user.password})
			    .success (data, status, headers, config) ->
			    	console.log 'success y',data["type"]
			    	# data = $.param(data)
			    	$scope.user.username = ''
		    		$scope.user.password = ''
			    	if data["type"] == 1
			    		window.location.href = data.url
			    .error (data, status, headers, config) ->
			    	console.log 'error',data["type"]

		$http.get('/u/login')
		    .success (data, status, headers, config) ->
		    	console.log 'success x',data["type"]
		    	if data["type"] == 1
		    		if data.url == '/#/login'
		    			$scope.user.username = ''
		    			$scope.user.password = ''
		    			return
		    		window.location.href = data.url
	return LoginController