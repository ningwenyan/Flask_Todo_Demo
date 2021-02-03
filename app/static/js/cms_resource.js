/**
 * Created by kning on 20-12-15.
 */
$(function () {
   $(':button').click(function(){
       const Rid = $(this).data('role-id');
       console.log(Rid);
       $('#hiddenResource').attr('data-role-id', Rid) ;

   });

   $('#EditResourceModal').on('show.bs.modal',function(){
       const roleURL = '/api/v2/resourceApi/';
       csrfAjax.ajax({
           url:roleURL,
           type : 'GET',
           contentType : 'application/json',
           success : function (rst) {
               console.log(rst);
               console.log(rst.resources);
               for(i=0; i < rst.resources.length; i++){
                   $('#resourceOption').append( '<div class="form-check">'  + '<label class="form-check-label"> <input class="form-check-input" type="checkbox" value="'+rst.resources[i]+'" name="header">'+ rst.resources[i] +'</label>' + '</div>');
               }
           }
       });
   });
       // 禁止默认行为
       //e.preventDefault();

       // const Uid = $(this).data('user-id');
       // $('#roleOption').append()
    $('#saveResource').click(function(){
        const headers = [];
        $('input[name="header"]:checked').each(function(i){

            headers.push($(this).val().split(',')[0]);
            console.log(typeof $(this).val())
        });
        console.log(headers);

        const updateURL = '/api/v2/UpdateRoleResource/' + $('#hiddenResource').data('role-id') + '/';
        $.getJSON(updateURL, function(rst){
            console.log(rst);
            rst.resources = headers;
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
    $('#saveRoleModal').click(function () {
        const UpdateURL = '/api/v2/roleApi/';
        $.getJSON(UpdateURL, function(rst){
            rst.name = $('#modalRoleName').val();
            rst.description = $('#modalRoleDes').val();
            csrfAjax.ajax({
                url: UpdateURL,
                type: 'POST',
                contentType : 'application/json',
                data: JSON.stringify(rst),
                success: function(e){
                    swal.fire({
                        icon: 'success',
                        title : '添加成功'
                    });
                    setTimeout(function(){
                        location.reload();
                    }, 1000)
                }
            })
        })
    })
});