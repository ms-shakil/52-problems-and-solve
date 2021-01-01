//The coordinate point is inside or outside the circle find
var val1 = 1
var val2 =1
var basarddo = 4
var val3 = 10
var val4 = -14
function MyFunction(inp,inp2,inp3,inp4,bas){
    var value = Math.sqrt(((inp3-inp)**2 +(inp4-inp2)**2))
    
    if (value <= bas){
        console.log("The point is inside the circle.")
    }else{
        console.log("The point is not inside the circle.")
    }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
}
MyFunction(val1,val2,val3,val4,basarddo)