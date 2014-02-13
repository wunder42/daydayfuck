'use strict'

define [], ->
	RegisterController = ($scope, $http, $location) ->
		$scope.user = {
			username: '',
			password: ''
		}
		$scope.requestRegister = ->
			$http.post('/u/register', {username: $scope.user.username, password: $scope.user.password})
			    .success (data, status, headers, config) ->
			    	console.log 'success',data
			    	# data = $.param(data)
			    	if data.status == 'OK'
			    		window.location.href = '/#/login'
			    # .error (data, status, headers, config) ->
			    # 	console.log 'error'

	return RegisterController