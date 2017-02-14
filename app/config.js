/**
 * Created by rsmathew on 2/6/17.
 */
(function () {
    angular
        .module("OSExceptions")
        .config(RouteConfig);

    function RouteConfig ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('main', {
                url: '/',
                template: ''
            })
            .state('modalContainer', {
                abstract: true,
                parent: 'main',
                url: '',
                onEnter: ['$modal', '$state', function($modal, $state) {

                    $modal.open({
                        template: '<div ui-view="modal"></div>',
                        backdrop: false,
                        windowClass: 'right fade'
                    }).result.finally(function() {
                        $state.go('main');
                    });
                }]
            })
            .state('modelContent', {
                url: "exception?:projectName/:errorName",
                parent: 'modalContainer',
                params : { },
                views: {
                    'modal@': {
                        templateUrl: './html-components/modal-template.html',
                        controller: function($scope, $stateParams, $location, DataService) {
                            vm = this;

                            vm.projectName = $stateParams.projectName;
                            vm.errorName = $stateParams.errorName;

                            vm.exp = DataService.getExceptionData(vm.projectName, vm.errorName);
                        },
                        controllerAs: 'model'
                    }
                }
            });


    }

})();