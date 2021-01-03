// palindrome 
inp ="civic"
function MyFunction(inp){
    var value = inp.split("").reverse().join("")
    if (inp == value ){
        console.log("Yes! It is Palindrome !")
    }else{
        console.log("Sorry! It is not Palindrome !")
    }
}
MyFunction(inp)