// Probability 
const Fruits =["apple","banana","blackcurrant","mango","apple","apple","banana","mango","mango","apple"]
const input_fruit = "apple"
function frauitsFrobability(list,item){
    var list_len = list.length
    var count = 0
    for(var i = 0; i< list_len;i++){
        if (list[i]== item){
            count+=1
        }
    }
    var proba = count / list_len
    return proba
}
console.log(frauitsFrobability(Fruits,input_fruit))