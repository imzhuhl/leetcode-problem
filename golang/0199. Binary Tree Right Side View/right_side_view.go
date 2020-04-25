package main

import "fmt"

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var rst []int
	floor := []*TreeNode{root}
	p, q := floor[0], floor[0]

	for {
		p = floor[0]
		floor = floor[1:]
		if p.Left != nil {
			floor = append(floor, p.Left)
		}
		if p.Right != nil {
			floor = append(floor, p.Right)
		}
		if p == q {
			rst = append(rst, p.Val)
			if len(floor) > 0 {
				q = floor[len(floor)-1]
			} else {
				break
			}
		}
	}
	return rst
}

// build a binary tree from array
func createTree(lst []int) *TreeNode {
	if len(lst) == 0 {
		return nil
	}
	var root *TreeNode = nil
	deque := []*TreeNode{}
	flag := 0 // status
	for _, val := range lst {
		var node *TreeNode = nil
		if val != -1 {
			node = &TreeNode{Val: val, Left: nil, Right: nil}
			deque = append(deque, node)
		}
		if root == nil {
			root = node
		} else {
			p := deque[0]
			if flag == 0 { // build left child
				p.Left = node
				flag = 1
			} else if flag == 1 {
				p.Right = node
				flag = 0
				deque = deque[1:]
			}
		}
	}
	return root
}

func main() {
	lst := []int{1, 2, 3, -1, 5, -1, 4}
	root := createTree(lst)
	rst := rightSideView(root)
	fmt.Println(rst)

}
