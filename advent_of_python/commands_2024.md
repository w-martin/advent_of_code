# Commands for 2024

## Pre compile

```sh
poetry run python3 -m compileall -o 2 src/
export PYTHONPATH=src
```

## Day 1

```sh
command="poetry run python -OO -m cli 2024 1 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 1 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 2

```sh
command="poetry run python -OO -m cli 2024 2 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 2 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 4

```sh
command="poetry run python -OO -m cli 2024 4 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 4 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 5

```sh
command="poetry run python -OO -m cli 2024 5 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 5 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 6

```sh
command="poetry run python -OO -m cli 2024 6 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 6 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

## Day 8

```sh
command="poetry run python -OO -m cli 2024 8 1"
bash -c "$command" && hyperfine -N -r 5 "$command"
```

```sh
command="poetry run python -OO -m cli 2024 8 2"
bash -c "$command" && hyperfine -N -r 5 "$command"
```
