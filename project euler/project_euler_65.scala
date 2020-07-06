val xs = Array.fill[Int](100)(1)
var index = 1

for(i <- xs.indices){
  if(((i + 2) % 3) == 0){ xs(i) = 2*index; index += 1}
}
val ys = xs.toVector

/**t(1) = xsR(0)*xsR(1) + 1
  *n(0) = xsR(0)
  *t{n} = xsR{n} * t{n-1} + n{n-1}
  *n{n} = t{n-1}
  *
  */

def fraction(xs: Vector[Int]): (Int, Int) = {
  val xsR = xs.reverse
  var t = xsR(1)*xsR(0) + 1
  var n = xsR(0)
  println(s"$t och $n")

  for(i <- 1 until xsR.length){
    val temp = t
    t = xsR(i)*n + t
    n = temp
  }
  println(s"$t och $n")

  var sum = 0
  for(i <- 0 until t.toString.length) sum += t.toString.apply(i).toString.toInt
  println(sum)

  (t, n)
}
