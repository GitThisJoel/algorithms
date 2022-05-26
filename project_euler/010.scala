//summera alla primtal under max
var prime: List[Int] = List()
for(i <- 1 to 2000000 by 2){
  if(isPrime(i)) prime :+ i
}

def isPrime(nmbr: Int): Boolean = {
  var result = true
  val sqrt = Math.sqrt(nmbr).toInt
  for(i <- 2 to sqrt by 2){
    if(nmbr % i == 0) result = false
  }
  result
}
