/**
 * Created with IntelliJ IDEA.
 * User: Mateusz
 * Date: 15.11.12
 * Time: 22:38
 */

'use strict';

define([], function () {

    function TasksController($scope, $http) {

    	$scope.cartBoxState = {
    		show: [false, false, false]
    	};

    	$scope.carBoxContent = ['', '', ''];
        $scope.isLogin = false;

        $scope.addCart = function(e) {
        	// console.log('addcart', this);
        	// jQuery(".addCart").before("<div class='dragItem'>dragItem5</div>");
        	console.log($(e.target).attr('data-id'));
        	$scope.cartBoxState.show[$(e.target).attr('data-id')] = true;
        }

        $scope.addCartAccept = function(e) {
        	var _i = $(e.target).attr('data-id');
        	var _c = $scope.carBoxContent[_i];
        	if (_c) {
        		console.log('addCartAccept', _c);
        		$(e.target).parent().before("<div class='dragItem'>" + _c + "</div>");
                $http.get('/m/add', {params: {content:_c}});
        		// jQuery(".addCart").before("<div class='dragItem'>" + _c + "</div>");
                // $http.get('m/add', {content:_c}).success(function(data, status, headers, config){
                //     console.log 'add success';
                // }).error(function(data, status, headers, config){
                //     console.log 'add error';
                // });

        	}
        	$scope.carBoxContent[_i] = '';
        	$scope.cartBoxState.show[_i] = false;
        };

        $scope.addCartCancel = function(e) {
        	$scope.cartBoxState.show[$(e.target).attr('data-id')] = false;
        };

        $http.get('/d/data').success(function(data, status, headers, config) {
            console.log('success', data);
            if (data.status === 'NG') {
              return window.location.href = '/#/login';
            }
        });
        // console.log($scope.data)
    }

    return TasksController;
});
