$(function(){

    $('#account-login').submit(function(event){
        event.preventDefault();

        let user_name = $("#username-login").val();
        let password = $("#username-password").val();

        $.ajax({
            url: window.location.origin+'/ajax/request-login',
            type: 'POST',
            data: {
                user: user_name,
                password: password
            },
            success: function(response){

                alert('Welkom terug!');

                window.location.href = window.location.origin + '/map';
            }
        });
    })
});