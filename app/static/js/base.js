/**
 * Created by kning on 20-12-12.
 */

$(function () {
    $('#ver_code').click(function(){
        $(this).attr('src', "/commons/graph_captcha/" + '?' + Math.random());
    });
});