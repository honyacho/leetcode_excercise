import "fmt"

type LRUCache struct {
    impl map[int]*Node
    first *Node
    last *Node
    capacity int
}

type Node struct {
    Key int
    Value int
    Next *Node
    Before *Node
}


func Constructor(capacity int) LRUCache {
    return LRUCache{map[int]*Node{}, nil, nil, capacity}
}

func (this *LRUCache) drop(key int, fromMap bool) {
    if val, ok := this.impl[key]; ok {
        // 最後尾
        if val.Next == nil {
            if val.Before == nil {
                // 最後尾かつ最前
                this.last = nil
                this.first = nil
            } else {
                // 最後尾かつ最前ではない
                this.last = val.Before
                val.Before.Next = nil
            }
        } else {
            // 最前 
            if val.Before == nil {
                val.Next.Before = nil
                this.first = val.Next
            // 最後尾でないかつ最前でない
            } else {
                bf := val.Before
                nx := val.Next
                nx.Before = bf
                bf.Next = nx
            }
        }
        if fromMap {
            delete(this.impl, key)
        }
    }
}

func (this *LRUCache) push(key int, value int) {
    var nd *Node
    if this.first != nil {
        nd = &Node{key, value, this.first, nil}
        this.impl[key] = nd
        this.first.Before = nd
    } else {
        nd = &Node{key, value, nil, nil}
        this.impl[key] = nd
        this.last = nd
    }
    this.first = nd
}

func (this *LRUCache) Get(key int) int {
    if v, ok := this.impl[key]; ok {
        this.drop(key, true)
        this.push(key, v.Value)
        this.Debug("get")
        return v.Value
    } else {
        return -1
    }
}

func (this *LRUCache) Debug(str string) {
//     fmt.Println("debg - " + str)
//     fmt.Println(fmt.Sprintf("fst %v lst %v", this.first, this.last))

//     for ptr := this.first; ptr != nil; ptr = (*ptr).Next {
//         fmt.Println(fmt.Sprintf("%v next: %v, before: %v", ptr, (*ptr).Next, (*ptr).Before))
//     }

//     fmt.Println("----")
}

func (this *LRUCache) Put(key int, value int) {
    if this.Get(key) != -1 {
        this.first.Value = value
        return
    }
    this.push(key, value)

    // キャパオーバードロップ
    if len(this.impl) > this.capacity && this.last != nil {
        this.drop(this.last.Key, true)
    }
    this.Debug("put")
    return
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
