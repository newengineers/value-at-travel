$(function(){

    $('#account-login').submit(function(event){
        event.preventDefault();

        let user_name = $("#username-login");
        let password = $("#username-password");

        $.post(window.location.origin+'/ajax/request-login', {
            user: user_name,
            password: password
        }, function(response){
            alert(response);
        });

    })
});