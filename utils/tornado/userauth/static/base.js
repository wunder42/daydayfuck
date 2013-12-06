// Generated by CoffeeScript 1.6.3
(function() {
  var $, getcookie;

  $ = jQuery;

  $(function() {
    $("#ttt").click(function(e) {
      return $.get('/u', {
        name: 'knife'
      }, function(data) {
        return console.log(data);
      });
    });
    $("#sm").click(function(e) {
      e.preventDefault();
      return $.ajaxFileUpload({
        url: '/',
        secureuri: false,
        fileElementId: 'uf',
        dataType: 'json',
        success: function(data, status) {
          return console.log(data);
        },
        error: function(data, status, e) {
          return console.log(data);
        }
      });
    });
    $("#login").click(function(e) {
      var args;
      e.preventDefault();
      args = ("_xsrf=" + (getcookie("_xsrf")) + "&") + $("#loginForm").formSerialize();
      return $.post('/login', args, function(data, textStatus, xhr) {
        data = $.parseJSON(data);
        if (data['successful']) {
          return location.href = '/';
        } else {
          return console.log('login error');
        }
      });
    });
    return $("#register").click(function(e) {
      var args;
      e.preventDefault();
      args = ("_xsrf=" + (getcookie("_xsrf")) + "&") + $("#registerForm").formSerialize();
      return $.post('/register', args, function(data, textStatus, xhr) {
        data = $.parseJSON(data);
        if (data['successful']) {
          return location.href = '/login';
        } else {
          return console.log('register error');
        }
      });
    });
  });

  getcookie = function(name) {
    var r;
    r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    if (r) {
      return r[1];
    } else {
      return null;
    }
  };

}).call(this);
