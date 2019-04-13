$(function(){

    let references = {
        /* Login/Register references */
        form_element: 'form',
        form_toggle: '.message a',
        form_login_container: '#form-login',
        form_register_container: '#form-register',
        form_error: '.form-feedback',

        /* Login specific form references */
        login_usr_input: '#login_email',
        login_pw_input: '#login_pw',

        /* Register specific form references */
        register_usr_input: "#register_email",
        register_pw_input: "#register_pw",
        register_pw_confirmed_input: "#register_pw_confirm",

        ajax_url_login: 'account-login',
        ajax_url_register: 'account-register'
    };

    function test_mail(email_input){
        let regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email_input);
    }

    function show_feedback(message, color='#FF6464') {
        let element = $(references.form_error);

        element.fadeIn(500);
        element.css('color', color);
        element.html(message);
    }

    $(references.form_toggle).click(function () {
        $(references.form_error).hide();
        // noinspection JSCheckFunctionSignatures
        $(references.form_element).animate(
            {
                height: "toggle",
                opacity: "toggle"
            }, "slow");
    });

    $(references.form_login_container).submit(function (event) {
        event.preventDefault();

        new AjaxCall(references.ajax_url_login)
            .add('email', $(references.login_usr_input).val())
            .add('password', $(references.login_pw_input).val())
            .send(function(){
                location.href='/map';
            }, show_feedback
        );
    });

    $(references.form_register_container).submit(function (event) {
        event.preventDefault();

        let email = $(references.register_usr_input).val();
        if(!test_mail(email)){
            show_feedback('Invalid email address');
            return;
        }

        new AjaxCall(references.ajax_url_register)
            .add('email', email)
            .add('password', $(references.register_pw_input).val())
            .add('password_confirmed', $(references.register_pw_confirmed_input).val())
            .send(function(response){
                show_feedback(response.message, '#658C4C');
            }, show_feedback
        );
    });
});

$(document).ready(function(){
    $(document).on("click", "#login-btn", function(){
        var form = $(this).closest("form");
        form.submit();
    });

    $(document).on("click", "#register-btn", function(){
        var form = $(this).closest("form");
        form.submit();
    });
});