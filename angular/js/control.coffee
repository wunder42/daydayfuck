

#class NewCtl
 #   constructor: ->
  #      @news = [{'id':1, 'content':'u are shit man'}, {'id':2, 'content':'good evening'}]

angular.module('newst', []).config ['$routeProvider', ($routeProvider) -> 
    $routeProvider.
        when('/new', {templateUrl: 'new/new-list.html', controller: NewsCtrl}).
        when('/new/:newid', {templateUrl: 'new/new-detail.html', controller: NewsDetailCtrl}).
        otherwise {redirectTo: '/new'}
    ]

NewsCtrl = ($scope, $http) ->
    $http.get("data/t.json").success (data) ->
        $scope.news = data
    #$scope.news = [{'name':1, 'content':'u are shit man'}, {'name':2, 'content':'good evening'}]

NewsDetailCtrl = ($scope, $routeParams) ->
    $scope.id = $routeParams.newid
