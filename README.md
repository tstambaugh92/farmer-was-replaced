# The Farmer Was Replaced

I use foo to type up whatever I'm doing now, main to run it as a leaderboard run.

## Times (as of 2026-01-04)

Lots of code cleaning to be done, but my times:

| Challenge | Time | Rank |
|-----------|------|------|
| Cactus Single | 00:24.674 | #36 |
| Cactus | 00:41.878 | #55 |
| Dinosaur | 17:45.008 | #68 |
| Maze | 01:53.476 | #9 |
| Maze Single | 02:41.476 | #22 |
| Pumpkins | 07:33.905 | #41 |
| Fastest Reset | 3:37:49.491 | #95 |

## Cactus Single

This algorithm is one I came up with from trial and error. I have no mathematical reason to know it works. It just hasn't failed. It's sort of like if an insertion sort carried light items to the bottom left, heavy items to the top right.

## Cactus

If the bottom left quadrant has cacti >= level 5, or the top right quadrant < 5,
I kill it and replant it. If you try to reroll a cacti before it's fully grown, it keeps
the same level, so this slows down this method a bit. It still saved me 10 seconds.

## Maze

Winning combo was 25 5x5 mazes, 7 7x7 mazes. Cut down on wasted space, which was
much better than cramming two drones in the same maze.

Putting two drones in the same maze often ended up with them in sync so the 2nd didn't
really add much. Not nothing, but not much.

## Maze Single

Still BFS

## Pumpkins

16 patches of 6x6 pumpkins with 2 drones each. The amount of water and fertilizer to use was just trial and error.

## Fastest Reset

I really just wanted to be done with achivements at this point. There's over an our of trivial savings to do here and obviously much more than that to get a top time. But hey, top 100.