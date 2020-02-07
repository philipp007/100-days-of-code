use std::collections::HashMap;

fn main() {
    let tree = vec![0, 1, 2, 2];

    println!("Max count: {}", fruit_tree(tree));
}

fn fruit_tree(tree: Vec<i32>) -> i32 {
    let mut map: HashMap<i32, i32> = HashMap::new();
    let mut max: i32 = 0;
    let mut i = 0;
    let mut j = 0;

    while j < tree.len() {
        if map.len() <= 2 {
            map.insert(tree[j], j as i32);
            j += 1;

            let count: i32 = j as i32 - i as i32;

            if count > max {
                max = count;
            }
        }

        if map.len() > 2 {
            map.remove(&tree[i]);
            let mut min_index = 999;

            for (k, v) in map.iter() {
                if *v < min_index {
                    min_index = *k;
                }
            }

            i = map[&min_index] as usize;
        }
    }

    return max;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tree() {
        let tree = vec![3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4];
        let tree2 = vec![1, 2, 3, 2, 2];

        assert_eq!(fruit_tree(tree), 5);
        assert_eq!(fruit_tree(tree2), 4);
    }
}
