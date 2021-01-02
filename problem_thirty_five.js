// string sort
var value = "hello pyear bhai kemon acho tmi"
function MyFunction(value){
    var res = value.replace(/[.!, ]+/g, " ").trim().split(" ");
    var val = res.sort()
    for(var i = 0; i < val.length; i++){
        console.log(val[i])
    }
}
MyFunction(value)
