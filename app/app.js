(function () {

    var app = angular.module("OSExceptions", []);

    app.controller('tabController', function(){
        this.tab = 'keystone';
        this.setTab = function(tab){
            this.tab = tab;
        };
        this.isSet = function(checkTab){
          return this.tab == checkTab;
        };
    });

    app.controller('serviceController', ['$http', function ($http) {
        var service = this;
        service.name = [];

        $http.get('data/keystone.json').success(function (data) {
            service.name['keystone'] = data.keystone;
        });
        $http.get('data/nova.json').success(function (data) {
            service.name['nova'] = data.nova;
        });
        $http.get('data/cinder.json').success(function (data) {
            service.name['cinder'] = data.cinder;
        });

        this.getService = function (tab) {
            return service.name[tab];
        }
        this.getMessages = function () {

        };
    }]);

    // app.directive('serviceTable', ['$http', function($http){
    //    return {
    //        restrict : "E",
    //        templateUrl : "html-components/service-table.html",
    //        controller: function($http){
    //            var service = this;
    //            service.name = [];
    //
    //            $http.get('data/keystone.json').success(function (data) {
    //                 service.name = data.keystone;
    //            });
    //        },
    //        controllerAs: 'service'
    //    };
    // }]);

})();
