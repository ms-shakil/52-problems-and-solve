// stirng to number
var value = "AAZ"
function stringToNumber(value){
    var val = value.split("")
    var lst = []
    for(var i = 0; val.length> i;i++){
        if(val[i]=="A"){
            val[i]=1
        }else if(val[i]=="B"){
            val[i]=2
        }else if(val[i]=="C"){
            val[i]=3
        }else if(val[i]=="D"){
            val[i]=4
        }else if(val[i]=="E"){
            val[i]=5
        }else if(val[i]=="F"){
            val[i]=6
        }else if(val[i]=="G"){
            val[i]=7
        }else if(val[i]=="H"){
            val[i]=8
        }else if(val[i]=="I"){
            val[i]=9
        }else if(val[i]=="J"){
            val[i]=10
        }else if(val[i]=="K"){
            val[i]=11
        }else if(val[i]=="L"){
            val[i]=12
        }else if(val[i]=="M"){
            val[i]=13
        }else if(val[i]=="N"){
            val[i]=14
        }else if(val[i]=="O"){
            val[i]=15
        }else if(val[i]=="P"){
            val[i]=16
        }else if(val[i]=="Q"){
            val[i]=17
        }else if(val[i]=="R"){
            val[i]=18
        }else if(val[i]=="S"){
            val[i]=19
        }else if(val[i]=="T"){
            val[i]=20
        }else if(val[i]=="U"){
            val[i]=21
        }else if(val[i]=="V"){
            val[i]=22
        }else if(val[i]=="W"){
            val[i]=23
        }else if(val[i]=="X"){
            val[i]=24
        }else if(val[i]=="Y"){
            val[i]=25
        }else if(val[i]=="Z"){
            val[i] = 26
        }
        lst.push(val[i].toString())

    }
    console.log(lst.join(""))
}

stringToNumber(value)