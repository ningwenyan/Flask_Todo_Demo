/**
 * Created by kning on 20-12-14.
 */



$(function () {
   $(':button').click(function(){
       console.log($(this));
       const Uid = $(this).data('user-id');
       console.log(Uid);
       $('#hiddenTag').attr('data-user-id', Uid) ;

   });

   $('#EditRoleModal').on('show.bs.modal',function(){
       const roleURL = '/api/v2/roleApi/';
       csrfAjax.ajax({
           url:roleURL,
           type : 'GET',
           contentType : 'application/json',
           success : function (rst) {
               console.log(rst);
               if (rst.info) {
                   swal.fire({
                       icon: 'info',
                       title : '你没有权限.'
                   })

               }else{
                    for (i = 0; i < rst.roles.length; i++) {
                       console.log(rst.roles[i]);
                       $('#roleOption').append('<div class="form-check">' + '<label class="form-check-label"> <input class="form-check-input" type="checkbox" value="' + rst.roles[i] + '" name="header">' + rst.roles[i] + '</label>' + '</div>');
                   }
               }
           }
       });
   });
       // 禁止默认行为
       //e.preventDefault();

       // const Uid = $(this).data('user-id');
       // $('#roleOption').append()
    $('#saveRole').click(function(){
        const headers = [];
        $('input[name="header"]:checked').each(function(i){
            headers.push($(this).val())
        });
        console.log(headers);

        const updateURL = '/api/v2/UpdateUserRole/' + $('#hiddenTag').data('user-id') + '/';
        $.getJSON(updateURL, function(rst){
            console.log(rst);
            rst.roles = headers;
            csrfAjax.ajax({
                url: updateURL,
                type: 'POST',
                contentType : 'application/json',
                data : JSON.stringify(rst),
                success: function(e){
                    swal.fire({
                        icon: 'success',
                        title : '添加成功'
                    });
                    setTimeout(function(){
                        location.reload();
                    }, 3000)
                }
            })
        })
    });

});