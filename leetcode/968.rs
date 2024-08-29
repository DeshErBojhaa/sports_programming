use std::cell::RefCell;
use std::rc::Rc;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

enum NodeKind {
    Leaf,
    Camera,
    Other,
    Null,
}

struct Solution {}

impl Solution {
    pub fn min_camera_cover(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut ans = 0;
        let nk = Solution::solve(root, &mut ans);
        if matches!(nk, NodeKind::Other) {
            ans += 1;
        }
        ans
    }

    fn solve(cur: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> NodeKind {
        if let Some(cur) = cur {
            let l = Solution::solve(cur.borrow().left.clone(), ans);
            let r = Solution::solve(cur.borrow().right.clone(), ans);
            match (l, r) {
                (NodeKind::Leaf, _) | (_, NodeKind::Leaf) => {
                    *ans += 1;
                    NodeKind::Camera
                }
                (NodeKind::Camera, _) | (_, NodeKind::Camera) => NodeKind::Other,
                (NodeKind::Other, _) | (_, NodeKind::Other) => NodeKind::Leaf,
                _ => NodeKind::Other,
            }
        } else {
            NodeKind::Other
        }
    }
}

fn main() {}
