## Running Rust tests:

If you have [just](https://github.com/casey/just) installed you can simply run (inside the `lc-rust` directory):

### Testing LeetCode problems
```bash
just tl 0001 # 0001 is the leetcode problem number
# or
just test-leetcode 0001 # 0001 is the leetcode problem number
# or
just tl 0001 example_1 # 0001 is the leetcode problem number, example_1 is a filter for which tests to run
# or
just test-leetcode 0001 example_1 # 0001 is the leetcode problem number
```
