val xs = Array.fill[Int](100)(1)
var index = 1

for(i <- xs.indices){
  if(((i + 2) % 3) == 0){ xs(i) = 2*index; index += 1}
}
val ys = xs.toVector

//2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
//1, 2,   1,    1,    4,     1,      1,      1,        1,        1, ...

val t = Array.fill[Int](100)(1)
val n = Array.fill[Int](100)(1)

t(0) = 2; t(1) = 3; t(2) = 8; t(3) = 11
for(i <- 4 until t.length){
  t(i) = t(i - 1)*ys(i - 1) + t(i - 2)
}
