function keyLogin(event) {
    var browser = navigator.appName;
    var userAgent = navigator.userAgent;
    var code;
    if(browser.indexOf('Internet')>-1)
        code = window.event.keyCode;
    else if(userAgent.indexOf("Firefox")>-1)
        code = event.which;
    else
        code = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
/*
    if( code == 13)
        document.getElementById("btn_login").click();  //enter调用登录按钮
*/
}
window.onload = function() {
    var btn_login = this.document.getElementById('btn_login');

    btn_login.onclick = function login() {
        var username = document.getElementById("username");
        var password = document.getElementById("password");

        if(username.value == "") {
            alert("请输入用户名");
        }else if (password.value == '') {
            alert("请输入密码");
        }
        
    }
}
