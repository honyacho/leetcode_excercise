object Solution {
    def palindromePairs(words: Array[String]): List[List[Int]] = {
        var ls = List[List[Int]]()
        for (i <- 0 until words.length) {
            for (j <- 0 until words.length) {
                if (i != j) {
                    var res = true
                    val test = words(i)+words(j)
                    val len = test.length
                    for (k <- 0 until (test.length / 2 + 1)) {
                        res = res && test(k) == test(len-1-k)
                    }
                    if (res) ls = List(i,j) :: ls
                }
            }
        }
        return ls.reverse
    }
}
