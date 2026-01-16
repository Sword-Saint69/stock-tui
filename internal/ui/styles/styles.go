package styles

import "github.com/charmbracelet/lipgloss"

// Theme represents a color scheme for the application
type Theme struct {
	ColorPrimary   lipgloss.Color
	ColorSecondary lipgloss.Color
	ColorSuccess   lipgloss.Color
	ColorError     lipgloss.Color
	ColorText      lipgloss.Color
	ColorSubtext   lipgloss.Color
	ColorHighlight lipgloss.Color
}

// ThemeManager manages the active theme
type ThemeManager struct {
	themes map[string]Theme
	activeTheme string
}

// NewThemeManager creates a new theme manager with predefined themes
func NewThemeManager() *ThemeManager {
	tm := &ThemeManager{
		themes: make(map[string]Theme),
		activeTheme: "default",
	}

	// Register all themes
	tm.themes["default"] = Theme{
		ColorPrimary:   lipgloss.Color("#7D56F4"),
		ColorSecondary: lipgloss.Color("#666666"),
		ColorSuccess:   lipgloss.Color("#04B575"),
		ColorError:     lipgloss.Color("#FF4C4C"),
		ColorText:      lipgloss.Color("#EEEEEE"),
		ColorSubtext:   lipgloss.Color("#999999"),
		ColorHighlight: lipgloss.Color("#2D2D2D"),
	}

	tm.themes["dark"] = Theme{
		ColorPrimary:   lipgloss.Color("#8850EF"),
		ColorSecondary: lipgloss.Color("#555555"),
		ColorSuccess:   lipgloss.Color("#00CC66"),
		ColorError:     lipgloss.Color("#FF3333"),
		ColorText:      lipgloss.Color("#FFFFFF"),
		ColorSubtext:   lipgloss.Color("#AAAAAA"),
		ColorHighlight: lipgloss.Color("#444444"),
	}

	tm.themes["light"] = Theme{
		ColorPrimary:   lipgloss.Color("#5D3FD3"),
		ColorSecondary: lipgloss.Color("#888888"),
		ColorSuccess:   lipgloss.Color("#2E8B57"),
		ColorError:     lipgloss.Color("#DC143C"),
		ColorText:      lipgloss.Color("#000000"),
		ColorSubtext:   lipgloss.Color("#666666"),
		ColorHighlight: lipgloss.Color("#DDDDDD"),
	}

	tm.themes["solarized"] = Theme{
		ColorPrimary:   lipgloss.Color("#268BD2"),
		ColorSecondary: lipgloss.Color("#859900"),
		ColorSuccess:   lipgloss.Color("#859900"),
		ColorError:     lipgloss.Color("#DC322F"),
		ColorText:      lipgloss.Color("#839496"),
		ColorSubtext:   lipgloss.Color("#586E75"),
		ColorHighlight: lipgloss.Color("#073642"),
	}

	tm.themes["monokai"] = Theme{
		ColorPrimary:   lipgloss.Color("#AE81FF"),
		ColorSecondary: lipgloss.Color("#75715E"),
		ColorSuccess:   lipgloss.Color("#A6E22E"),
		ColorError:     lipgloss.Color("#F92672"),
		ColorText:      lipgloss.Color("#F8F8F2"),
		ColorSubtext:   lipgloss.Color("#75715E"),
		ColorHighlight: lipgloss.Color("#49483E"),
	}

	tm.themes["dracula"] = Theme{
		ColorPrimary:   lipgloss.Color("#BD93F9"),
		ColorSecondary: lipgloss.Color("#6272A4"),
		ColorSuccess:   lipgloss.Color("#50FA7B"),
		ColorError:     lipgloss.Color("#FF5555"),
		ColorText:      lipgloss.Color("#F8F8F2"),
		ColorSubtext:   lipgloss.Color("#6272A4"),
		ColorHighlight: lipgloss.Color("#44475A"),
	}

	tm.themes["nord"] = Theme{
		ColorPrimary:   lipgloss.Color("#81A1C1"),
		ColorSecondary: lipgloss.Color("#4C566A"),
		ColorSuccess:   lipgloss.Color("#A3BE8C"),
		ColorError:     lipgloss.Color("#BF616A"),
		ColorText:      lipgloss.Color("#ECEFF4"),
		ColorSubtext:   lipgloss.Color("#D8DEE9"),
		ColorHighlight: lipgloss.Color("#434C5E"),
	}

	tm.themes["gruvbox"] = Theme{
		ColorPrimary:   lipgloss.Color("#83A598"),
		ColorSecondary: lipgloss.Color("#A89984"),
		ColorSuccess:   lipgloss.Color("#98971A"),
		ColorError:     lipgloss.Color("#FB4934"),
		ColorText:      lipgloss.Color("#EBDBB2"),
		ColorSubtext:   lipgloss.Color("#BDAE93"),
		ColorHighlight: lipgloss.Color("#3C3836"),
	}

	tm.themes["tokyo-night"] = Theme{
		ColorPrimary:   lipgloss.Color("#7AA2F7"),
		ColorSecondary: lipgloss.Color("#565F89"),
		ColorSuccess:   lipgloss.Color("#9ECE6A"),
		ColorError:     lipgloss.Color("#F7768E"),
		ColorText:      lipgloss.Color("#A9B1D6"),
		ColorSubtext:   lipgloss.Color("#787C99"),
		ColorHighlight: lipgloss.Color("#24283B"),
	}

	tm.themes["catppuccin"] = Theme{
		ColorPrimary:   lipgloss.Color("#89B4FA"),
		ColorSecondary: lipgloss.Color("#6C7086"),
		ColorSuccess:   lipgloss.Color("#A6E3A1"),
		ColorError:     lipgloss.Color("#F38BA8"),
		ColorText:      lipgloss.Color("#CDD6F4"),
		ColorSubtext:   lipgloss.Color("#A6ADC8"),
		ColorHighlight: lipgloss.Color("#45475A"),
	}

	return tm
}

// SetTheme sets the active theme
func (tm *ThemeManager) SetTheme(name string) bool {
	if _, exists := tm.themes[name]; exists {
		tm.activeTheme = name
		return true
	}
	return false
}

// GetTheme returns the active theme
func (tm *ThemeManager) GetTheme() Theme {
	return tm.themes[tm.activeTheme]
}

// GetThemeNames returns a slice of all available theme names
func (tm *ThemeManager) GetThemeNames() []string {
	var names []string
	for name := range tm.themes {
		names = append(names, name)
	}
	return names
}

var (
	themeManager = NewThemeManager()
	// Current theme colors
	ThemeColors = themeManager.GetTheme()

	// Base styles
	Base = lipgloss.NewStyle().Foreground(ThemeColors.ColorText)

	// Panes
	Pane = lipgloss.NewStyle().
		Border(lipgloss.RoundedBorder()).
		BorderForeground(ThemeColors.ColorSecondary).
		Padding(0, 1)

	ActivePane = Pane.Copy().
		BorderForeground(ThemeColors.ColorPrimary)

	// Watchlist
	ListItem = lipgloss.NewStyle().
		PaddingLeft(1).
		PaddingRight(1)

	SelectedItem = ListItem.Copy().
		Background(ThemeColors.ColorHighlight).
		Foreground(ThemeColors.ColorPrimary).
		Bold(true)

	PositiveChange = lipgloss.NewStyle().Foreground(ThemeColors.ColorSuccess)
	NegativeChange = lipgloss.NewStyle().Foreground(ThemeColors.ColorError)

	// Chart
	ChartLabel = lipgloss.NewStyle().
		Foreground(ThemeColors.ColorSubtext).
		Width(8).
		Align(lipgloss.Right)
)

// UpdateStyles updates all styles to use the current theme
func UpdateStyles() {
	ThemeColors = themeManager.GetTheme()
	Base = Base.Foreground(ThemeColors.ColorText)
	Pane = Pane.BorderForeground(ThemeColors.ColorSecondary)
	ActivePane = ActivePane.BorderForeground(ThemeColors.ColorPrimary)
	SelectedItem = SelectedItem.Background(ThemeColors.ColorHighlight).Foreground(ThemeColors.ColorPrimary)
	PositiveChange = PositiveChange.Foreground(ThemeColors.ColorSuccess)
	NegativeChange = NegativeChange.Foreground(ThemeColors.ColorError)
	ChartLabel = ChartLabel.Foreground(ThemeColors.ColorSubtext)
}

// SetThemeByName sets the theme by name
func SetThemeByName(name string) bool {
	result := themeManager.SetTheme(name)
	if result {
		UpdateStyles()
	}
	return result
}

// GetCurrentThemeName returns the name of the current theme
func GetCurrentThemeName() string {
	return themeManager.activeTheme
}

// GetAvailableThemes returns all available theme names
func GetAvailableThemes() []string {
	return themeManager.GetThemeNames()
}

// GetTheme returns the current theme
func GetTheme() Theme {
	return themeManager.GetTheme()
}

