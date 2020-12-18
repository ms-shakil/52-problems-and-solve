// count vowels
var inp ="i am a programer"
function myFunction(inp){
    var value =inp.split(/\s/).join('').split("")
    var count = 0
    for(var i = 0; i < value.length;i++){
        if(value[i ]=="a" || value[i]=="e" || value[i]=="i" || value[i]=="o" || value[i]=="u" ){
            count+=1
        }
       }
    return count   
}
console.log("Number of vowels",myFunction(inp))