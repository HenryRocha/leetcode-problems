## Running Python tests:

If you have [just](https://github.com/casey/just) installed you can simply run (inside the `lc-python` directory):

### Testing interview solutions
```bash
just ti 01 # 01 is the interview number
# or
just test-interview 01 # 01 is the interview number
# or
just ti 01 example1 # 01 is the interview number, example1 is a filter for which tests to run
# or
just test-interview 01 example1 # 01 is the interview number
```

### Testing mandatory assignments solutions
```bash
just tm search # search is the mandatory assignment name
# or
just test-mandatory search # search is the mandatory assignment name
# or
just tm search example1 # search is the mandatory assignment name, example1 is a filter for which tests to run
# or
just test-mandatory search example1 # search is the mandatory assignment name
```
