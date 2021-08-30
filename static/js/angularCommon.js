var commonApp = angular.module('AppCommon', []);
commonApp.controller('CtrlCommon', ['$scope', function($scope) {}]);
commonApp.controller('DialogController', ['$scope', '$mdDialog', 'SerCommon', '$filter','dialogData', function($scope, $mdDialog,
  SerCommon,$filter, dialogData) {

}]);
commonApp.service("SerCommon", function($http) {

});

