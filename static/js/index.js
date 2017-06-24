angular.module('myApp', []).controller('indexCtrl', function($scope) {
$scope.tools = [
{id:1, name:"我的IP",url:"myip"},
{id:2, name:"ocr识别",url:"ocr.html" },
{id:3, name:"车牌提取",url:"carnum.html" }
];
$scope.jump = function(url){
    window.location= url;
}
}
);
