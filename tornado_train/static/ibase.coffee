$ = jQuery

$("#note-add").click -> $("#note-add-dialog").fadeIn "fast"

$("#note-add-cancel").click (e) ->
	$("#note-add-content").val ""
	$("#note-add-dialog").fadeOut "slow"
	e.preventDefault()

getcookie = (name) ->
    r = document.cookie.match "\\b" + name + "=([^;]*)\\b"
    if r[1] then r else 0
    

$("#note-add-submit").click (e)->
    e.preventDefault()
    args = {"_xsrf": getcookie("_xsrf"), "content": $("#note-add-content").val()}
    $.post '/n/add', args, (data, textStatus, xhr) ->
        $("#note-add-cancel").click()
        data = $.parseJSON data
        console.log data, textStatus
        if data.status
            $(".mCSB_container").prepend '<div class="delta inote"><div class="msg"><a href="#">'+'X'+'</a></div></div>'
            $(".ilists").mCustomScrollbar "scrollTo", "top"

$(".ilists").mCustomScrollbar {verticalScroll:true}





