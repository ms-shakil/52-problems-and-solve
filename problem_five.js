// addition first first number and last number
var number = 2345678
var msd = number % 10
while ( number =>10){
    number1 = number / 10
    number = number1
   if (number <= 10){
       break
   }
}
var lsd = Math.floor(number)
var value = msd + lsd
console.log(value)

// same problem solved but different code
var nam =5556561
var name  = String(nam)
name1 = name.split('')
var msd = name1[0]
var lsd = name1[name1.length -1]
var msd1 = parseInt(msd)
var lsd1 = parseInt(lsd)
var add = msd1 + lsd1
console.log(add)
