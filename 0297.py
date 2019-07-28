# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Encodes a tree to a single string.
#
# @param {TreeNode} root
# @return {string}

REG = /[\d-]/

def serialize(root)
    return "n" if root.nil?
    res = "#{root.val}(#{serialize(root.left)}#{serialize(root.right)})"
    p res
    res
end

# Decodes your encoded data to tree.
#
# @param {string} data
# @return {TreeNode}
def deserialize(data)
    des(data, 0)[0]
end

def des(data, pos)
    node = nil
    if data[pos] == "n"
        if data[pos+1] == ","
            return [nil, pos+1]
        else
            return [nil, pos+1]
        end
    elsif data[pos].nil?
        return [node, pos]
    else
        str = ""
        while data[pos] and data[pos].match(REG)
            str += data[pos]
            pos += 1
        end
        node = TreeNode.new str.to_i
        pos += 1
        node.left, pos = des(data, pos)
        node.right, pos = des(data, pos)
        pos += 1
    end
    [node, pos]
end


# Your functions will be called as such:
# deserialize(serialize(data))
