document.addEventListener('scroll', function (e) {
    var t = document.documentElement.scrollTop || document.body.scrollTop;
    if (t > 35) {
        //navbar 浮动
    }

    var target = document.getElementById('_float-btn-top');
    if (t <= 0) {
        //返回top
        target.style.opacity = 0;
    } else {
        target.style.opacity = 1;
    }
    var navbar = document.getElementsByClassName('navbar')[0];
    if (t >= 35) {
        //navbar
        navbar.classList.add('navbar-fixed');
    }else{
        navbar.classList.remove('navbar-fixed');
    }

    target.onclick = function () {
        document.documentElement.scrollTop = 0
    }
});

function _addFavorite() {
    var url = window.location;
    var title = document.title;
    var ua = navigator.userAgent.toLowerCase();
    if (ua.indexOf("360se") > -1) {
        alert("由于360浏览器功能限制，请按 Ctrl+D 手动收藏！");
    } else if (ua.indexOf("msie 8") > -1) {
        window.external.AddToFavoritesBar(url, title); //IE8
    } else if (document.all) {//IE类浏览器
        try {
            window.external.addFavorite(url, title);
        } catch (e) {
            alert('您的浏览器不支持,请按 Ctrl+D 手动收藏!');
        }
    } else if (window.sidebar) {//firfox等浏览器；
        window.sidebar.addPanel(title, url, "");
    } else {
        alert('您的浏览器不支持,请按 Ctrl+D 手动收藏!');
    }
}


//设为首页 <a onclick="SetHome(this,window.location)" >设为首页</a>
function SetHome(obj, vrl) {
    //debugger;
    //谷歌下vrl为数组对象非字符串
    var homePage = 'wwww.baidu.com';
    try {
        obj.style.behavior = 'url(#default#homepage)';
        obj.setHomePage(homePage);
    } catch (e) {
        if (window.netscape) {
            try {
                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
            } catch (e) {
                alert("此操作被浏览器拒绝！\n请在浏览器地址栏输入“about:config”并回车\n然后将 [signed.applets.codebase_principal_support]的值设置为'true',双击即可。");
            }
            var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
            prefs.setCharPref('browser.startup.homepage', homePage);
        }
    }
}

