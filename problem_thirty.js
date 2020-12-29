// perfect number 2
var value = 500
function perfectNumber(value){
    var arr =[]
    for(var i = 1 ; i< value ;i++){
        var count = 0
        for (var j = 1 ; j<i ; j++){
            if(i% j ==0){
                count += j
            }
        }
        if (count == i){
            arr.push(i)
        }

    }
    return arr
}
console.log(perfectNumber(value))