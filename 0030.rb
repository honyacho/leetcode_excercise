# @param {String} s
# @param {String[]} words
# @return {Integer[]}
def find_substring(s, words)
    return [] if s.size == 0 || words.size == 0
    find(words, s, (words.first || "").size)
end

def find(words, s, size)
    sol = []
    mp = {}
    words.each do |w|
        mp[w] ||= 0
        mp[w] += 1
    end

    return sol if s.size < size
    (0..(s.size - size*words.size)).each do |i|
        set = mp.clone
        sol.push(i) if rec_search(set, s.slice(i, s.length), size)
    end
    sol
end

def rec_search(words, str, len)
    return true if words.size == 0
    cand = str.slice(0, len)
    if words.include?(cand) && words[cand] > 0
        words[cand] -= 1
        words.delete(cand) if words[cand] == 0
        rec_search(words, str.slice(len, str.size), len)
    else
        false
    end
end
