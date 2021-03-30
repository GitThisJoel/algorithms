//a < b < c
//a^2 + b^2 = c^2

//a + b + c = 1000
//abc = ?

//c = 1000 - a - b = math.sqrt(a^2 + b^2)

var a: Double = 0; var b: Double = 0; var c: Double = 0; var abc: Double = 0
var found = false
while(!found){
  while(a <= b){
    if(math.sqrt(a*a + b*b) + a + b == 1000){
      c = math.sqrt(a*a + b*b)
      abc = a*b*c
      print(s"$a * $b * $c = $abc \n")
      found = true
    }
    a += 1
  }
  b += 1; a = 0
}



//aa = cc - bb
