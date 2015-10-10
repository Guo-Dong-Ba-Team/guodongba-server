$().ready(function() {
 $("#phone-form").validate({
        rules: {
   p_username: {
    required:true,
    minlength:11,
    maxlength:11
   },

   p_password: {
    required: true,
    minlength: 7,
    maxlength:20
   },
   p_re_password: {
    required: true,
    minlength: 7,
    maxlength:20,
    equalTo: "#p_password"
   }
  },
        messages: {
   p_username: {
    required:"手机号不能为空",
    minlength:"请输入11位手机号码",
    maxlength:"请输入11位手机号码"
   },
   p_password: {
    required: "密码不能为空",
    minlength: "密码不能小于{0}个字符",
    maxlength:"密码不能大于{0}个字符"
   },
   p_re_password: {
    required: "请再次输入密码",
    minlength: "确认密码不能小于{0}个字符",
    maxlength:"密码不能大于{0}个字符",
    equalTo: "两次输入密码不一致"
   }
  }
    });


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
    email:"请输入正确的电子邮箱"，
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