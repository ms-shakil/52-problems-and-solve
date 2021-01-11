// 2 array item console sortly in one list
var lst =[3,5,6,3,3,64,64,34,64,88]
var lst1 = [8,7,9,1,2]
function soRt(arr,arr1){
    var array = arr.concat(arr1)
    for (var i =0;i<array.length;i++){
        for(var j= i; j<array.length; j++){
            if(array[i]> array[j]){
                T = array[i]
                array[i]=array[j]
                array[j]= T
            }
        }
    }
    return array  
}

print(Sort_list(lst1,lst2))

