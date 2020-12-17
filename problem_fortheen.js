// how many singal caraacter have this sentence
var value ="hello payer bhai"
function find_character(value){
    var val = value.split(/\s/).join('')
    var lst = val.split("")
    var dic ={}
    for (var i =0 ; i<lst.length; i++){
        if (lst[i] in dic){
            dic[lst[i]]+=1
        }
        else{
            dic[lst[i]] =1
        }
    }
    return dic
}
console.log(find_character(value))