
require.config { paths: {
    jquery: '/static/js/jquery-1.8.3.min.js'
    angular: '/static/js/angular.js'
}}

require ['jquery', 'angular'], (_, e) -> 
    console.log 'ok'