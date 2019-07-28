object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {
        var cnt = 0
        for (i <- (0 until nums.length)) {
            var cum1 = 0
            for (j <- (i until nums.length)) {
                cum1 = cum1 + nums(j)
                if (cum1 == k) cnt = cnt + 1
            }
        }
        return cnt
    }
}
