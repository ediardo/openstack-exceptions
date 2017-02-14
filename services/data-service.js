/**
 * Created by rsmathew on 2/13/17.
 */
(function () {
    angular
        .module("OSExceptions")
        .factory("DataService", DataService);

    function DataService($http) {
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

        var api = {
            getAllData : getAllData,
            getExceptionData : getExceptionData123
        };

        return api;

        function getAllData() {
            return service.data;
        }

        function getExceptionData123(projectName, errorName) {
            var errors = service.data[projectName].filter(function (obj) {
                return obj.name === errorName;
            });

            return errors[0];
        }
    }
})();