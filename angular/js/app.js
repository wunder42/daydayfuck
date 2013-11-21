  angular.module('newst', []).config([
    '$routeProvider', function($routeProvider) {
      return $routeProvider.when('/new', {
        templateUrl: 'new/new-list.html',
        controller: NewsCtrl
      }).otherwise({
        redirectTo: '/news'
      });
    }
  ]);

//   angular.module('newst', []).
//   config(['$routeProvider', function($routeProvider) {
//   $routeProvider.
//       when('/new', {templateUrl: 'new/new-list.html',   controller: NewsCtrl}).
//       // when('/phones/:phoneId', {templateUrl: 'partials/phone-detail.html', controller: PhoneDetailCtrl}).
//       otherwise({redirectTo: '/new'});
// }]);