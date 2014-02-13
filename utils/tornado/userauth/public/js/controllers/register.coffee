'use strict'

define [], ->
	RegisterController = ($scope, $http, $location) ->
		$scope.user = {
			username: 'tt',
			password: '9090'
		}
		$scope.requestRegister = ->
			$http.post('/u/register', {username: $scope.user.username, password: $scope.user.password})
			    .success (data, status, headers, config) ->
			    	console.log 'success',data["type"], data.url
			    	# data = $.param(data)
			    	if data["type"] == 1
			    		window.location.href = data.url
			    # .error (data, status, headers, config) ->
			    # 	console.log 'error'

	return RegisterController