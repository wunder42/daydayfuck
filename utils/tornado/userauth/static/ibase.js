// Generated by CoffeeScript 1.6.3
(function() {
  var $, getcookie;

  $ = jQuery;

  $("#note-add").click(function() {
    return $("#note-add-dialog").fadeIn("fast");
  });

  $("#note-add-cancel").click(function(e) {
    $("#note-add-content").val("");
    $("#note-add-dialog").fadeOut("slow");
    return e.preventDefault();
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

  $("#note-add-submit").click(function(e) {
    var args;
    e.preventDefault();
    args = {
      "_xsrf": getcookie("_xsrf"),
      "content": $("#note-add-content").val()
    };
    return $.post('/n/add', args, function(data, textStatus, xhr) {
      $("#note-add-cancel").click();
      data = $.parseJSON(data);
      console.log(data, textStatus);
      if (data.status) {
        $(".mCSB_container").prepend('<div class="delta inote"><div class="msg"><a href="#">' + 'X' + '</a></div></div>');
        return $(".ilists").mCustomScrollbar("scrollTo", "top");
      }
    });
  });

  $(".ilists").mCustomScrollbar({
    verticalScroll: true,
    advanced: {
      updateOnContentResize: true
    }
  });

  $(".load-more").click(function(e) {
    var d, data, _i, _len;
    console.log(mcs.top, mcs.draggerTop);
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    for (_i = 0, _len = data.length; _i < _len; _i++) {
      d = data[_i];
      $(".mCSB_container").prepend('<div class="delta inote"><div class="msg"><a href="#">' + d + '</a></div></div>');
    }
    $(".ilists").mCustomScrollbar("scrollTo", "top");
    return console.log('load-more end');
  });

}).call(this);
