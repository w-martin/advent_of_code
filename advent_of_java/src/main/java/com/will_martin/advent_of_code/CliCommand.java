package com.will_martin.advent_of_code;

import lombok.SneakyThrows;
import lombok.val;
import picocli.CommandLine;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.MessageFormat;
import java.util.concurrent.Callable;

@CommandLine.Command(name = "advent-of-code", mixinStandardHelpOptions = true, version = "advent-of-code 1.0",
        description = "Solve Advent of Code challenges")
public class CliCommand implements Callable<Integer> {

    @CommandLine.Option(names={"--day"}, description="Day of the Advent of Code challenge", type = Integer.class)
    private Integer day;

    @CommandLine.Option(names={"--year"}, description="Year of the Advent of Code challenge", type = Integer.class)
    private Integer year;

    @CommandLine.Option(names={"--part"}, description="Part of the Advent of Code challenge", type = Integer.class)
    private Integer part;

    @CommandLine.Option(names={"--data-root"}, description="Directory containing the input data")
    private Path dataRoot;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new CliCommand()).execute(args);
        System.exit(exitCode);
    }

    @SneakyThrows
    @Override
    public Integer call() {
        System.out.printf(MessageFormat.format("Year: {0}, Day: {1}, Part: {2}, Data Root: {3}\n", year, day, part, dataRoot));
        val data = java.nio.file.Files.readString(Paths.get(dataRoot.toAbsolutePath().toString(), year.toString(), String.format("day_%02d.txt", day)));
        switch (year) {
            case 2015 -> {
                switch (day) {
                    case 1 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day01Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 2 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day02Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 3 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day03Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 4 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day04Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 5 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day05Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 6 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day06Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 7 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day07Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 8 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day08Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 9 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day09Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                    case 10 -> {
                        var solver = new com.will_martin.advent_of_code.year_2015.Day10Solver();
                        switch (part) {
                            case 1 -> System.out.println(solver.solvePart1(data));
                            case 2 -> System.out.println(solver.solvePart2(data));
                        }
                    }
                }
            }
        }
        return 0;
    }
}
