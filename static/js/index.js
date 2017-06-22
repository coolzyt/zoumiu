angular.module('myApp', []).controller('indexCtrl', function($scope) {
$scope.tools = [
{id:1, name:"我的IP",url:"myip"},
{id:2, name:'今日新闻',url:"news.html" }
];
$scope.jump = function(url){
    window.location= url;
}
}
);
