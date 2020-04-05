let fl_app = angular.module("flwApp",[]);

fl_app.controller('flwController',function($scope, $http){
    $scope.form = [
        {
            label:'Sepal Length',
            type:'text'
        },{
            label:'Sepal Width',
            type:'text'
        },{
            label:'Petal Length',
            type:'text'
        },{
            label:'Petal Width',
            type:'text'
        }
    ]
    

    
    $scope.onSubmit = function(){
        
        $http.post()
    }
})





$(function() {
    var sumbit = ()=>{
        var sep_len = $('#sepal_length').text();
        var sep_wid = $('#sepal_width').text();
        var pet_len = $('#petal_length').text();
        var pet_wid = $('#petal_width').text();
        
        var data = {'sepal_legth':sep_len,
                    'sepal_width': sep_wid,
                    'petal_length': pet_len,
                    'pet_wid': pet_wid
                    }
        $.post("predict", data,function( data ) {
            $( ".result" ).html( data );
        });
    }
 });