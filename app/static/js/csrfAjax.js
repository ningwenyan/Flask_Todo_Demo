/**
 * Created by kning on 20-11-22.
 */
// csrfAjax.js
// create JavaScript object

var csrfAjax={
 get: function (args) {
     args['type'] = 'GET';
     this.ajax(args);
 },
 post: function(args){
     args['type'] = 'POST';
     this.ajax(args);
 },
 ajax: function (args) {
     // 添加csrf_token
     this._ajaxSetup();
     $.ajax(args);
 },
 _ajaxSetup: function () {
     $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                 // 获取 csrf_token,
                 // 需要注意的是 base.html 必须添加 meta 标签
                 var csrf_token = $("meta[name='csrf-token']").attr('content');
                 xhr.setRequestHeader("X-CSRFToken", csrf_token);
         }
     }
 });
 }
};