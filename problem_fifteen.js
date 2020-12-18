// reverse text element
var value ="hello payer bhai"
function reverSe(val){
    var lst = val.split(" ")
    var arr =[]
    for(var i=0; i <lst.length;i++){
        arr.push(lst[i].split("").reverse().join(""))
    }
    var txt = " "
    for (var j =0; j<arr.length;j++){
        txt +=arr[j]

    }
    return txt
}
console.log(reverSe(value))