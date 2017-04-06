(function () {

    var app = angular.module("OSExceptions", ['ui.router', 'ui.bootstrap']);

    app.controller('tabController', function(){
        this.tab = 'keystone';
        this.setTab = function(tab){
            this.tab = tab;
        };
        this.isSet = function(checkTab){
          return this.tab == checkTab;
        };
        this.getTab = function(){
            return this.tab;
        }
    });

    app.controller('serviceController', ['$http', '$scope', 'DataService', function ($http, $scope, DataService) {
        var service = this;
        service.data = DataService.getAllData();

        this.getService = function (projectName) {
            return service.data[projectName];
        };
        this.getCount = function (tab) {
            return getService(tab).length;
        };

        $scope.sort = function(keyname){
            $scope.thisname = "Heyda";
            $scope.sortKey = keyname; //set key to selected col
            $scope.reverse = !$scope.reverse; //toggle true false
        }
    }]);

})();
