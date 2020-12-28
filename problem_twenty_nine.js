// Perfect number !
var inp = 30
function perFect_Number(value){
    var count = 0
    for(var i = 1 ; i< value;i++){
        if (value % i == 0){
            count+=i
        }
    }
    if (count == value){
        console.log(value,"is perfect number!")
    }else{
        console.log(value,"is not perfect number!")
    }
}
perFect_Number(inp)