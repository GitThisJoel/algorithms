val strLines = scala.io.Source.fromFile("pe18Tri.txt").getLines.toVector
val lines = strLines.map(_.split(' ').map(_.toInt).toVector)
//kan kolla samma index och samma index+1
var sum = lines(0)(0)
var lastIndex = 0

for(i <- 1 to lines.length - 1) {
    if(lines(i)(lastIndex + 1) > lines(i)(lastIndex)) lastIndex += 1
    sum += lines(i)(lastIndex)
}
