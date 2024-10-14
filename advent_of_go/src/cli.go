package main

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
	"will-martin.com/advent_of_go/src/solvers_2015"
)

var cmd = &cobra.Command{
	Use:   "cli",
	Short: "Advent of Code go CLI",
	Run: func(cmd *cobra.Command, args []string) {
		Year, _ := cmd.Flags().GetUint16("year")
		Day, _ := cmd.Flags().GetUint8("day")
		Part, _ := cmd.Flags().GetUint8("part")
		DataPath, _ := cmd.Flags().GetString("dataPath")
		fmt.Printf("Running year %d, day %d, part %d with data path %s\n", Year, Day, Part, DataPath)
		rawData, err := os.ReadFile(fmt.Sprintf("%s/2015/day_%02d.txt", DataPath, Day))
		if err != nil {
			panic(err)
		}
		data := string(rawData)
		switch Year {
		case 2015:
			switch Day {
			case 1:
				solver := solvers_2015.Solver01{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))

				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 2:
				solver := solvers_2015.Solver02{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 3:
				solver := solvers_2015.Solver03{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 4:
				solver := solvers_2015.Solver04{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 5:
				solver := solvers_2015.Solver05{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 6:
				solver := solvers_2015.Solver06{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 9:
				solver := solvers_2015.Solver09{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			}
		}

	},
}

func init() {
	cmd.Flags().Uint16P("year", "y", uint16(2015), "year of the puzzle")
	cmd.Flags().Uint8P("day", "d", uint8(1), "day of the puzzle")
	cmd.Flags().Uint8P("part", "p", uint8(1), "part of the puzzle")
	cmd.Flags().String("dataPath", "<data_path>", "path to the data files")

	_ = cmd.MarkFlagRequired("year")
	_ = cmd.MarkFlagRequired("day")
	_ = cmd.MarkFlagRequired("part")
	_ = cmd.MarkFlagRequired("dataPath")
}

func main() {
	if err := cmd.Execute(); err != nil {
		_, _ = fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
