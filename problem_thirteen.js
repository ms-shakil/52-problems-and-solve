// how many inp caraacter have in  there sentence
var value ="hello payer bhai"
var inp = "x"
function find_character(value,inp){
    var val = value.split(/\s/).join('')
    var lst = val.split("")
    var count = 0
    for(var i = 0 ; i < lst.length; i++){
        if(lst[i] == inp){
            count +=1
        }
    }
    if (count == 0){
        console.log(inp,"is not present.")
    }
    else{
        console.log("Occurrence of",inp,"in",value,"=",count)
    }
}

find_character(value,inp)


