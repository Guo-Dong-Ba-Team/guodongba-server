$(document).ready(function(){
 $("#mail-form").validate({
        rules: {
   m_username: {
    required:true,
    email:true
   },

   m_password: {
    required: true,
    minlength: 7,
    maxlength:20
   },
   m_re_password: {
    required: true,
    minlength: 7,
    maxlength:20,
    equalTo: "#m_password"
   }
  },
        messages: {
   m_username: {
    required:"邮箱地址不能为空",
    email:"请输入正确的电子邮箱"
   },
   m_password: {
    required: "密码不能为空",
    minlength: "密码不能小于{0}个字符",
    maxlength:"密码不能大于{0}个字符"
   },
   m_re_password: {
    required: "请再次输入密码",
    minlength: "确认密码不能小于{0}个字符",
    maxlength:"密码不能大于{0}个字符",
    equalTo: "两次输入密码不一致"
   }
  }
    });

});