// small number to large numbr
var num1=1
var num2 =242
var num3 = 11

function smallNumber(a,b,c){
    if(a>b){
        T = a
        a = b
        b = T
    }
    if(a>c){
        T = a
        a = c
        c = T
    }
    if(b>c){
        T = b
        b = c
        c = T
    }
  console.log(a,b,c)  
}

smallNumber(num1,num2,num3)