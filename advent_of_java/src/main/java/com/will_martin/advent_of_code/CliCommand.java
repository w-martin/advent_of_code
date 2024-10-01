package com.will_martin.advent_of_code;

import lombok.SneakyThrows;
import lombok.val;
import picocli.CommandLine;

import java.io.File;
import java.util.concurrent.Callable;

@CommandLine.Command(name = "advent-of-code", mixinStandardHelpOptions = true, version = "advent-of-code 1.0",
        description = "Solve Advent of Code challenges")
public class CliCommand implements Callable<Integer> {

    @CommandLine.Option(names={"-d", "--day"}, description="Day of the Advent of Code challenge", type = Integer.class)
    private Integer day;

    @CommandLine.Option(names={"-y", "--year"}, description="Year of the Advent of Code challenge", type = Integer.class)
    private Integer year;

    @CommandLine.Option(names={"-p", "--part"}, description="Part of the Advent of Code challenge", type = Integer.class)
    private Integer part;

    @CommandLine.Option(names={"-f", "--file"}, description="File containing the input data")
    private File filename;

    public static void main(String[] args) {
        int exitCode = new CommandLine(new CliCommand()).execute(args);
        System.exit(exitCode);
    }

    @SneakyThrows
    @Override
    public Integer call() {
        System.out.println(String.format("Year: %d, Day: %d, Part: %d, File: %s", year, day, part, filename));
        val data = java.nio.file.Files.readString(filename.toPath());
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
                }
            }
        }
        return 0;
    }
}
