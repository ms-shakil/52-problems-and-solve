
var number= 40.0
function MyFunciton(number){
    var count = 0
    while(number > 1){
        count+=1
        var num = number /2
        number = num
    }  
    console.log(count,"dayes") 

}
MyFunciton(number)