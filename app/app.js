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

    app.controller('serviceController', ['$http', 'DataService', function ($http, DataService) {
        var service = this;
        service.data = DataService.getAllData();

        this.getService = function (projectName) {
            return service.data[projectName];
        };
        this.getCount = function (tab) {
            return getService(tab).length;
        };
    }]);

})();
