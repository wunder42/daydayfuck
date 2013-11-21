$ = jQuery

for x in [0..48]
    $(".snake").append "<div class='cell' id=#{x+1}></div>"

$("#8").css "background", "rgba(63, 76, 78, 0.54)"
$("#8").addClass "sn-head"

remove_sn_head = (o) ->
    console.log o
    o.removeClass "sn-head"
    o.attr "style", ""

add_sn_head = (o) ->
    console.log o
    o.addClass "sn-head"
    o.css "background", "rgba(63, 76, 78, 0.54)"

is_dir_ok = (id, x_, y_) ->
    y = Math.floor (id-1) / 7
    x = (id-1) % 7
    console.log x+x_, y+y_
    return x+x_>=0 and x+x_<=6 and y+y_>=0 and y+y_<=6

$(document).keydown (e) ->
    tmp_id = parseInt $(".sn-head").attr "id"
    console.log tmp_id
    if e.keyCode == 38
        console.log 'down up'
        if is_dir_ok tmp_id, 0, -1
            console.log 'dir ok'
            remove_sn_head $("#"+tmp_id)
            _id = tmp_id - 7
            add_sn_head $("#"+_id)
            
    else if e.keyCode == 40
        console.log 'key down'
        if is_dir_ok tmp_id, 0, 1
            console.log 'dir ok'
            remove_sn_head $("#"+tmp_id)
            _id = tmp_id + 7
            add_sn_head $("#"+_id)

    else if e.keyCode == 37
        console.log 'down left'
        if is_dir_ok tmp_id, -1, 0
            console.log 'dir ok'
            remove_sn_head $("#"+tmp_id)
            _id = tmp_id - 1
            add_sn_head $("#"+_id)

    else if e.keyCode == 39
        console.log 'down right'
        if is_dir_ok tmp_id, 1, 0
            console.log 'dir ok'
            remove_sn_head $("#"+tmp_id)
            _id = tmp_id + 1
            add_sn_head $("#"+_id)

