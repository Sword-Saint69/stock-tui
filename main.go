package main

import (
	"log"

	tea "github.com/charmbracelet/bubbletea"

	"github.com/nisarga/stock-tui/internal/app"
	"github.com/nisarga/stock-tui/internal/config"
)

func main() {
	cfg, err := config.Load()
	if err != nil {
		log.Fatal(err)
	}

	a, err := app.New(cfg)
	if err != nil {
		log.Fatal(err)
	}
	defer a.Close()

	p := tea.NewProgram(
		a,
		tea.WithAltScreen(),
		tea.WithMouseCellMotion(),
	)

	if _, err := p.Run(); err != nil {
		log.Fatal(err)
	}
}