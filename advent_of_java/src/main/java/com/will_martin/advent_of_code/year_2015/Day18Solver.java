package com.will_martin.advent_of_code.year_2015;

import com.will_martin.advent_of_code.Solver;
import lombok.val;

public class Day18Solver implements Solver {

    @Override
    public String solvePart1(String data) {
        return String.valueOf(getNumLightsOnAfter(100, data, 100, false));
    }

    @Override
    public String solvePart2(String data) {
        return String.valueOf(getNumLightsOnAfter(100, data, 100, true));
    }

    public int getNumLightsOnAfter(final int numSteps, final String data, final int gridSize, final boolean stickyCorners) {
        boolean[][] lights = parseLights(data, gridSize);
        boolean[][] nextLights = new boolean[gridSize][gridSize];
        if (stickyCorners) {
            lights[0][0] = true;
            lights[0][gridSize - 1] = true;
            lights[gridSize - 1][0] = true;
            lights[gridSize - 1][gridSize - 1] = true;
        }
        for (int i = 0; i < numSteps; i++) {
            step(lights, nextLights, stickyCorners);
        }
        return countLightsOn(lights);
    }

    private void step(boolean[][] lights, boolean[][] nextLights, final boolean stickyCorners) {
        int gridSize = lights.length;
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                int numNeighboursOn = 0;
                boolean lightIsOn = lights[i][j];
                boolean leftEdge = i == 0;
                boolean rightEdge = i == gridSize - 1;
                boolean topEdge = j == 0;
                boolean bottomEdge = j == gridSize - 1;

                if (stickyCorners) {
                    if ((leftEdge && topEdge) || (leftEdge && bottomEdge) || (rightEdge && topEdge) || (rightEdge && bottomEdge)) {
                        nextLights[i][j] = true;
                        continue;
                    }
                }

                if (!leftEdge && !topEdge && lights[i - 1][j - 1]) {
                    numNeighboursOn++;
                }
                if (!topEdge && lights[i][j - 1]) {
                    numNeighboursOn++;
                }
                if (!rightEdge && !topEdge && lights[i + 1][j - 1]) {
                    numNeighboursOn++;
                }
                if (!leftEdge && lights[i - 1][j]) {
                    numNeighboursOn++;
                }
                if (!rightEdge && lights[i + 1][j]) {
                    numNeighboursOn++;
                }
                if (!leftEdge && !bottomEdge && lights[i - 1][j + 1]) {
                    numNeighboursOn++;
                }
                if (!bottomEdge && lights[i][j + 1]) {
                    numNeighboursOn++;
                }
                if (!rightEdge && !bottomEdge && lights[i + 1][j + 1]) {
                    numNeighboursOn++;
                }
                nextLights[i][j] = lightIsOn ? (numNeighboursOn == 2 || numNeighboursOn == 3) : numNeighboursOn == 3;
            }
        }
        for (int i = 0; i < gridSize; i++) {
            System.arraycopy(nextLights[i], 0, lights[i], 0, gridSize);
        }
    }

    private int countLightsOn(boolean[][] lights) {
        int count = 0;
        for (val row : lights) {
            for (val light : row) {
                if (light) {
                    count++;
                }
            }
        }
        return count;
    }

    private static boolean[][] parseLights(final String data, final int gridSize) {
        var lights = new boolean[gridSize][gridSize];
        var lightRow = 0;
        for (var line : data.trim().split("\n")) {
            line = line.trim();
            if (line.isEmpty()) {
                continue;
            }
            for (int characterIndex = 0; characterIndex < line.length(); characterIndex++) {
                lights[lightRow][characterIndex] = line.charAt(characterIndex) == '#';
            }
            lightRow++;
        }
        return lights;
    }
}
