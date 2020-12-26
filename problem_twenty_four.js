// LCM
var a = 15
var b = 5
function myFunction(a,b){
    if(a>b){
        t = a
        a = b
        b = t
    }
    var lst =[]
    for(var i = a; i>1;i--){
        Z = b % i
        X = a % i
        if(Z== 0 && X == 0){
            lst.push(i)
            k = b / i
            y = a / i
            b = k
            a = y
        }
    }
    lst.push(a)
    lst.push(b)
    var value = 1
    for (var j =0; lst.length> j;j++){
        value *= lst[j]
    }
    console.log("LCM = ",value)
}
myFunction(a,b)