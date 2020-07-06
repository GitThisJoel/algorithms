val lines = scala.io.Source.fromFile("C:\\Users\\Joel\\Code\\Project_Euler\\pe42Words.txt").getLines.toVector(0).split(',').map(x => x.slice(1, x.length-1)).toVector

//theoretical max number in lines are 364
var triangelNbr = Set[Int](0)
var index = 1
while(triangelNbr.max < 364){
  triangelNbr += index*(index+1)/2
  index += 1
}

var amount = 0
for(i <- lines.indices){
  if(triangelNbr(letterSum(lines(i)))) amount += 1
}
println(s"Number of $amount")

def letterSum(word: String): Int = {
  var sum = 0
  for(i <- word.indices){
    sum += (word(i).toInt - 64)
    }
    sum
}
