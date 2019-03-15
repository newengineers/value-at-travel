$(function(){

    $('#account-login').submit(function(event){
        event.preventDefault();

        let user_name = $("#username-login").val();
        let password = $("#username-password").val();

        console.log(user_name);
        $.get(window.location.origin+'/ajax/request-login', {
            user: user_name,
            password: password
        }, function(response){
            alert('Login resultaat: '+response);

            if(response === '200'){
                window.location.href = window.location.origin + '/map';
            }
        });
    })
});