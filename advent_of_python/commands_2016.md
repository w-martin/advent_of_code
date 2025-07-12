# Commands for 2016

## Pre compile

```sh
poetry run python3 -m compileall -o 2 src/
export PYTHONPATH=src
```

## Day 1

```sh
command="poetry run python -OO -m cli 2016 1 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2016 1 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 2

```sh
command="poetry run python -OO -m cli 2016 2 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2016 2 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 3

```sh
command="poetry run python -OO -m cli 2016 3 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2016 3 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 4

```sh
command="poetry run python -OO -m cli 2016 4 1"
bash -c "$command" && hyperfine -N -r 2 "$command"
```

```sh
command="poetry run python -OO -m cli 2016 4 2"
bash -c "$command" && hyperfine -N -r 2 "$command"
```

## Day 9

```sh
command="poetry run python -OO -m cli 2016 9 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2016 9 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```
