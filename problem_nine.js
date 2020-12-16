// Runrate  

var currR =225
var currO = "30.4"
var target = 331
function requiredRunrate(currR,currO,target){
    var run = target - currR
    var over = currO.split(".")
    var ball = parseInt(over[0]*6)+ parseInt(over[1])
    var rball = 300 - ball
    var currentRunrate =(currR/ball)*6
    var requiredRRate =(run/rball)*6
    console.log("Current Runrate:",currentRunrate.toFixed(2))
    console.log("Requried Runrate:", requiredRRate.toFixed(2))
}
requiredRunrate(currR,currO,target)




