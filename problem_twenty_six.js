// 1 st ways
var number = 371
function Myfunction(number){
    var lst =[]
    while (number > 9){
        var mod = number % 10
        lst.push(Math.floor(mod))
        var div = number/ 10
        number = div
    }
    lst.push(Math.floor(number))
    var len = lst.length
    var count = 0
    for(var i =0; lst.length>i;i++){
        count += lst[i]**len
    }
    return count
}
if (number == Myfunction(number)){
    console.log(number,"is an armstrong number!")

}else{
    console.log(number,"is not an armstrong number!")
}



//  2nd ways
var number = 311
function arMsTrong(number){
   var num= number.toString().split("")
   var len = num.length
   var count = 0
   for(var i = 0; len> i;i++){
      count+= (num[i]**len)
   }
   return count
}
if(number == arMsTrong(number)){
    console.log(number,"is an armstron number !")
}else{
    console.log(number,'is not an armstrong number !')
}






