$(document).ready(function(e) {
    $("input[placeholder]").placeholder();
    $("#search-block-form .form-item input").focus(function(){
        $("#search-block-form").addClass("focus-active");
        $("div.form-actions").addClass("div-active");
            })
    .blur(function(){
        $("#search-block-form").removeClass("focus-active");
        $("div.form-actions").removeClass("div-active");
    });
});