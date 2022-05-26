val lines = scala.io.Source.fromURL("https://projecteuler.net/project/resources/p022_names.txt").getLines.toVector

val sumNames = lines(0).split(',').map(i => i.tail.dropRight(1)).sorted.map(_.toCharArray.map(_.toInt - 64)).map(_.sum).toVector
val sum = (for(i <- sumNames.indices) yield sumNames(i)*(i+1)).sum

println(s"The sum equals $sum")
