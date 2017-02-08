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
            .state('home', {
                url: '/',
                template: '',
                controller: function ($http) {
                    var service = this;
                }
            })
            .state('modal', {
                abstract: true,
                parent: 'home',
                url: '',
                onEnter: ['$modal', '$state', function($modal, $state) {

                    $modal.open({
                        template: '<div ui-view="modal"></div>',
                        backdrop: false,
                        windowClass: 'right fade'
                    }).result.finally(function() {
                        $state.go('home');
                    });
                }]
            })
            .state('view', {
                url: 'exception/:id',
                parent: 'modal',
                params : { exceptionData: null, tabData: null },
                views: {
                    'modal@': {
                        templateUrl: './html-components/modal-template.html',
                        controller: function($scope, $stateParams) {
                            vm = this;

                            vm.tab = $stateParams.tabData;
                            vm.exp = $stateParams.exceptionData;

                        },
                        controllerAs: 'model'
                    }
                }
            });


    }

})();