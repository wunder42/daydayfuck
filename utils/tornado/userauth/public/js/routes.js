/**
 * Created with IntelliJ IDEA.
 * User: Mateusz
 * Date: 14.11.12
 * Time: 20:21
 */

'use strict';

define(['app', 'utils/route-config'], function (app, routeConfig) {

    return app.config(function ($routeProvider) {
        $routeProvider.when('/tasks', routeConfig.config('../partials/tasks.html', 'controllers/tasks', ['directives/version']));

        $routeProvider.when('/login', routeConfig.config('../partials/login.html', 'controllers/login'));
        $routeProvider.when('/register', routeConfig.config('../partials/register.html', 'controllers/register'));

        $routeProvider.otherwise({redirectTo:'/login'});
    });

    return app;
});
