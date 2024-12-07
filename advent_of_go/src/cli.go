package main

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
	"will-martin.com/advent_of_go/src/solvers_2015"
	"will-martin.com/advent_of_go/src/solvers_2024"
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
		rawData, err := os.ReadFile(fmt.Sprintf("%s/%d/day_%02d.txt", DataPath, Year, Day))
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
			case 7:
				solver := solvers_2015.Solver07{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 8:
				solver := solvers_2015.Solver08{}
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
			case 10:
				solver := solvers_2015.Solver10{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 11:
				solver := solvers_2015.Solver11{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 12:
				solver := solvers_2015.Solver12{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 13:
				solver := solvers_2015.Solver13{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 14:
				solver := solvers_2015.Solver14{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 15:
				solver := solvers_2015.Solver15{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 16:
				solver := solvers_2015.Solver16{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 17:
				solver := solvers_2015.Solver17{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 18:
				solver := solvers_2015.Solver18{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 19:
				solver := solvers_2015.Solver19{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 20:
				solver := solvers_2015.Solver20{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 21:
				solver := solvers_2015.Solver21{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 22:
				solver := solvers_2015.Solver22{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))
				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			}
		case 2024:
			switch Day {
			case 1:
				solver := solvers_2024.Solver01{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))

				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 3:
				solver := solvers_2024.Solver03{}
				switch Part {
				case 1:
					fmt.Println(solver.SolvePart1(data))

				case 2:
					fmt.Println(solver.SolvePart2(data))
				}
			case 7:
				solver := solvers_2024.Solver07{}
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
