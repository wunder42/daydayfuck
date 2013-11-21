$ = jQuery

actions = [{top:'200px'}, {left: '200px'}]
console.log typeof(actions[1])
#for action in actions
    #if action instanceof Dictionary
    #$(".t").animate action, 'normal', (e) ->
        #$(".t").css 'background-color', 'red'

$(".t").animate {top:'200px', left:"200px"}, "normal"
#$(".t").animate {left:"200px"}, 'normal'

$(".tt").animate {top:'200px'}, 10000
$(".tt").animate {right:"200px"}, 1000