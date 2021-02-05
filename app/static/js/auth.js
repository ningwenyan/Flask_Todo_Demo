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

$(function () {
    $('#personalRename').click(function(e){
        // 阻止默认新闻
        e.preventDefault();
        swal.fire({
            icon: 'info',
            title: '更改用户名',
            confirmButtonText: '确定',
            showCancelButton: true,
            cancelButtonText:'取消',
            input: 'text',
            inputPlaceholder: '用户名',
            allowOutsideClick: false,
        }).then(function(result){
            if (result.isConfirmed && result.value.length > 0){
                const Uid = $('#showID').data('user-id');
                const update_URL= '/api/v1/userUpdateUsername/' +  Uid  + '/' ;
                $.getJSON(update_URL, function(rst){
                    rst.username = result.value;
                    rst.url = '/api/v1/userUpdateUsername/';
                    csrfAjax.ajax({
                        url: update_URL,
                        type: 'POST',
                        contentType : 'application/json',
                        data : JSON.stringify(rst),
                        success: function (e) {
                            console.log(e);
                            if (e.flag){
                                swal.fire({
                                    icon: 'success',
                                    title : '添加成功'
                                    });
                            } else{
                                swal.fire({
                                    'icon': 'info',
                                    'title': '你没有权限'
                                })
                            }

                            setTimeout(function(){
                                location.reload();
                            }, 3000)
                        }
                    })
                })
            }
        });
    });

    // 修改邮箱
    $('#personalReEmail').click(function(e){
        e.preventDefault();
        swal.fire({
            icon : 'warning',
            title: '修改邮箱?',
            inputLabel: '点击确定将发送一份邮件到您的新邮箱.',
            input: 'email',
            inputPlaceholder : '新邮箱',
            inputAttributes: {
                autocapitalize: 'off'
            },
            confirmButtonText: '确定',
            showCancelButton: true,
            cancelButtonText:'取消',
            showLoaderOnConfirm: true,
            preConfirm:  (raw_email) => {
                showValidataflag = true; //全局变量
                csrfAjax.ajax({
                    async:false,
                    url : `http://api.kwenyan.online:8080/email/${raw_email}/`,
                    type: 'GET',
                    contentType: 'application/json',
                    success: function (rst) {
                        if (rst != null){
                            Swal.showValidationMessage('此邮箱已存在!');
                            showValidataflag = false;
                        }
                    }
                });
                if (showValidataflag){
                    return raw_email;
                }else{
                    return false;
                }
            },
            allowOutsideClick: () => !Swal.isLoading()
        }).then(function(rst){
            console.log(rst);
            if (rst.isConfirmed){
                const Uid = $('#showID').data('user-id');
                const updateURL = '/api/v1/userUpdateEmail/' + Uid + '/';
                $.getJSON(updateURL, function(result){
                    result.email = rst.value;
                    result.url = '/api/v1/userUpdateEmail/';
                    csrfAjax.ajax({
                        url : updateURL,
                        type: 'POST',
                        contentType : 'application/json',
                        data : JSON.stringify(result),
                        success: function(e){
                            if (e.success){
                                const Toast = Swal.mixin({
                                    toast: true,
                                    position: 'top-end',
                                    showConfirmButton: false,
                                    timer: 3000,
                                    timerProgressBar: true,
                                    didOpen: (toast) => {
                                      toast.addEventListener('mouseenter', Swal.stopTimer);
                                      toast.addEventListener('mouseleave', Swal.resumeTimer);
                                    }
                                    });
                                    Toast.fire({
                                      icon: 'success',
                                      title: '发送成功,请在5分钟之内完成修改!'
                                    })
                            }else{
                                const Toast = Swal.mixin({
                                    toast: true,
                                    position: 'top-end',
                                    showConfirmButton: false,
                                    timer: 3000,
                                    timerProgressBar: true,
                                    didOpen: (toast) => {
                                      toast.addEventListener('mouseenter', Swal.stopTimer);
                                      toast.addEventListener('mouseleave', Swal.resumeTimer);
                                    }
                                    });
                                    Toast.fire({
                                      icon: 'info',
                                      title: '你没有权限!'
                                    })
                            }

                        }
                    })
                })
            }
        })
    })
});