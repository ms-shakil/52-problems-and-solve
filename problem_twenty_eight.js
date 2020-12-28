// Character check 
var inp = a
function myFunction(inp){
    if (inp >="a"&& inp<="z"){
         console.log("Lowercase Character")
      }else if(inp >="A" && inp <="Z"){
        console.log("Uppercase Character")   
      }else if(inp >=0 && inp <=9){
        console.log("Numberical Character")
      }else{
        console.log("Speial Character")
      }
}
myFunction(inp)


