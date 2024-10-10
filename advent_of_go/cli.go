package main

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
	"will-martin.com/advent_of_go/solvers_2015"
)

var Year uint16
var Day uint8
var Part uint8
var DataPath string

var cmd = &cobra.Command{
	Use:   "cli",
	Short: "Advent of Code go CLI",
	Run: func(cmd *cobra.Command, args []string) {
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
				switch Part {
				case 1:
					fmt.Println(solvers_2015.SolvePart1(data))

				case 2:
					fmt.Println(solvers_2015.SolvePart2(data))
				}

			}
		}

	},
}

func init() {
	cmd.Flags().Uint16P(&Year, "year", "y", uint16(2015), "year of the puzzle")
	cmd.Flags().Uint8P(&Day, "day", "d", uint8(1), "day of the puzzle")
	cmd.Flags().Uint8P(&Part, "part", "p", uint8(1), "part of the puzzle")
	cmd.Flags().String(&DataPath, "dataPath", "<data_path>", "path to the data files")

	cmd.MarkFlagRequired("year")
	cmd.MarkFlagRequired("day")
	cmd.MarkFlagRequired("part")
	cmd.MarkFlagRequired("dataPath")
}

func main() {
	if err := cmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
