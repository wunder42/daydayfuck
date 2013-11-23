

#class NewCtl
 #   constructor: ->
  #      @news = [{'id':1, 'content':'u are shit man'}, {'id':2, 'content':'good evening'}]

datas = {
    "problem0": 'a5b7cb5528dfcf3c941e9d80ca0605e2_a',
    "problem1": 'a5b7cb5528470996034bddef327f71bb_a',
    "problem2": 'a5b7cb5528470996034bddef327f71bb_a',
    "problem3": 'a5b7cb55286cd5a8df1fb477bf0cd6c2_a',
    "problem4": 'a5b7cb552888a4786b3615535d250d77_a'
}

angular.module('guide', []).config ['$routeProvider', ($routeProvider) -> 
    $routeProvider.
        when('/nav', {templateUrl: 'template/nav.html', controller: NavCtrl}).
        when('/nav/:pid', {templateUrl: 'template/problem.html', controller: ProblemCtrl, resolve: ProblemCtrl.resolve}).
        otherwise {redirectTo: '/nav'}
    ]

NavCtrl = ($scope, $http) ->
    $scope.mood = 'daydayfuck'

ProblemCtrl = ($scope, $routeParams) ->
    $scope.pid = datas[$routeParams.pid]

ProblemCtrl.resolve = {
    delay: ($q) ->
        delay = $q.defer()
        load = -> 
            $.getScript 'js/problem.js', ->
                delay.resolve()
        load()
        delay.promise
}
