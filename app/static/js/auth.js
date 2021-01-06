/**
 * Created by kning on 20-12-13.
 */

$(function(){
    const Uid = $('#showID').data('user-id');
    const UserApi = '/api/v1/userApi/' + Uid + '/';
    csrfAjax.ajax({
        url: UserApi,
        type : 'GET',
        contentType : 'application/json',
        success: function(rst){
            console.log(rst);
            console.log(rst.email);
            $('#personalUsername').html(rst.username);
            $('#personalMe').html(moment(rst.member_since).format('LLL'));
            $('#personalLast').html(moment(rst.last_seen).format('LLL'));
            $('#personalGen').html(rst.gender);
            if (rst.avatar == null){
                console.log('1')
            } else{
                $('#avatar_img').attr('src', rst.avatar);
            }
            $('#personalEmail').html(rst.email);
            if (rst.confirmed){
                $('#personalConfirm').html('已激活');
            } else{
                $('#personalConfirm').html('未激活 ');
            }

            console.log(rst.email);
        }
    })
});