//word count by input somplex sentence;
var str = "hello , payer bhai ! . what are you doing "
function myFunction(val){
    var res = val.replace(/[.!, ]+/g, " ").trim().split(" ");
    console.log("count = ",res.length)
}
myFunction(str)

