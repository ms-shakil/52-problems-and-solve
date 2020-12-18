// count vawels and onsonats  
var inp ="hello payer bhai"
function myFunction(inp){
    var value =inp.split(/\s/).join('').split("")
    var count = ""
    var count1 = ""
    for(var i = 0; i < value.length;i++){
        if(value[i ]=="a" || value[i]=="e" || value[i]=="i" || value[i]=="o" || value[i]=="u" ){
            count+=value[i]
        }else{
            count1 +=value[i]
        }
       }
    console.log("Vowels ->",count)
    console.log("Cosoants ->",count1)
}
myFunction(inp)