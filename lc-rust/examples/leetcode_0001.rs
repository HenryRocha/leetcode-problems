use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum_hashmap(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut sub_map = HashMap::new();
        for i in 0..nums.len() {
            match sub_map.get(&nums[i]) {
                None => {
                    sub_map.insert(target - nums[i], i as i32);
                }
                Some(&j) => return vec![j, i as i32],
            }
        }

        vec![]
    }

    pub fn two_sum_bruteforce(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in 1..nums.len() {
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }

        vec![]
    }
}

macro_rules! run_tests {
    ($($name:ident[$function_name:ident]: $value:expr,)*) => {
        $(
            paste::item! {
                #[test]
                fn [< test_ $name _ $function_name >] () {
                    let (input, expected) = $value;
                    let (input_vector, input_target) = input;
                    assert_eq!(Solution::$function_name(input_vector, input_target), expected);
                }
            }
        )*
    }
}

run_tests! {
    example_1[two_sum_bruteforce]: ((vec![2, 7, 11, 15], 9), vec![0, 1]),
    example_2[two_sum_bruteforce]: ((vec![3, 2, 4], 6), vec![1, 2]),
    example_3[two_sum_bruteforce]: ((vec![3, 3], 6), vec![0, 1]),

    example_1[two_sum_hashmap]: ((vec![2, 7, 11, 15], 9), vec![0, 1]),
    example_2[two_sum_hashmap]: ((vec![3, 2, 4], 6), vec![1, 2]),
    example_3[two_sum_hashmap]: ((vec![3, 3], 6), vec![0, 1]),
}

fn main() {}
