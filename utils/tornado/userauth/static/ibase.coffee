$ = jQuery

$("#note-add").click -> $("#note-add-dialog").fadeIn "fast"

$("#note-add-cancel").click (e) ->
	$("#note-add-content").val ""
	$("#note-add-dialog").fadeOut "slow"
	e.preventDefault()

getcookie = (name) ->
    r = document.cookie.match "\\b" + name + "=([^;]*)\\b"
    if r then r[1] else null
    

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

$(".ilists").mCustomScrollbar {
    verticalScroll:true
    advanced: {
        updateOnContentResize: true
    }
}

$(".load-more").click (e) ->
    console.log mcs.top, mcs.draggerTop
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for d in data
        $(".mCSB_container").prepend '<div class="delta inote"><div class="msg"><a href="#">'+d+'</a></div></div>'
    $(".ilists").mCustomScrollbar "scrollTo", "top"
    console.log 'load-more end'






