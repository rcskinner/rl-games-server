package main

import (
	"fmt"

	"github.com/rcskinner/rl-games-server/games"
	"github.com/rcskinner/rl-games-server/games/connect4"
)

func main() {
	fmt.Println("Called from main")
	games.SayHi()
	connect4.Hi()
}
