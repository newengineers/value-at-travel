function AjaxCall(target_url) {

    this.url = window.location.origin+'/ajax/'+target_url+'/';
    this.data = {};

    this.add = function(key, value) {
        this.data[key] = value;
        return this;
    };

    this.send = function(success, fail=null){
        let url_ref = this.url;
        // noinspection JSValidateTypes
        $.post(url_ref, this.data)
            .done(function(response){
                let response_code = response.response;

                if(response_code === 200 && success instanceof Function)
                    success(response);
                else if(fail !== null && fail !== undefined && fail instanceof Function)
                    fail(response.message, response_code);
            })
            .fail(function(){
                console.error('Failed to communicate to '+url_ref);
            });
    };
}