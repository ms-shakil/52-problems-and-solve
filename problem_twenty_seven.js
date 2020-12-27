// checking sorted arr
arr =[1,2,3,4,5,9,7]
function myFunction(arr){
    var count = 1
    for(var i =0 ;arr.length -1>i;i++){
        if(arr[i]<arr[i+1]){
            count +=1
        }
        else{
            console.log("No this arry not sorted")
        }
    }
    if (count == arr.length){
        console.log("Yes this arry sorted")
    }
}
myFunction(arr)