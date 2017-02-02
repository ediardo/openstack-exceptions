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
        this.getTab = function(){
            return this.tab;
        }
    });

    app.controller('serviceController', ['$http', function ($http) {
        var service = this;
        service.data = [];

        $http.get('data/keystone.json').success(function (data) {
            service.data['keystone'] = data.keystone;
        });
        $http.get('data/nova.json').success(function (data) {
            service.data['nova'] = data.nova;
        });
        $http.get('data/cinder.json').success(function (data) {
            service.data['cinder'] = data.cinder;
        });
        $http.get('data/glance.json').success(function (data) {
            service.data['glance'] = data.glance;
        });

        this.getService = function (tab) {
            return service.data[tab];
        }
        this.getCount = function (tab) {
            return getService(tab).length;
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
