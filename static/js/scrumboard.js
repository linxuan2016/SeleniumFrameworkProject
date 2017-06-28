var app = angular.module('Scrumboard.demo', ['ngRoute']);

app.controller('ScrumboardController', function($scope, $http, $location, Login){
    $scope.addItem = function(list, title){
        var card = {
            list: list.id,
            title: title,


            };

         $http.post('/scrumboard/cards/', card)
            .then(function(response){
                list.cards.push(response.data);
            },
            function(){
                alert('could not create card.');
            });

    };

/*    $scope.login = function() {
        $http.post('/auth_api/login/',
          {username: 'linxuan', password: 'flxyjrpa'});
    };*/

/*    $scope.logout = function() {
        $http.get('/auth_api/logout/')
            .then(function() {
                $location.url('/login');
            });
    }*/


    Login.redirectIfNotLoggedIn();
    $scope.logout = Login.logout;

    $scope.data=[];
    $http.get("/scrumboard/lists/").then(function(response){
        $scope.data = response.data;
    });

    $scope.showFilters = false;
    $scope.reverse = true;
    $scope.sortBy = 'story_points';


 });