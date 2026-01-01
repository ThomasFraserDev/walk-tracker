# Walk Tracker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Rich](https://img.shields.io/badge/Rich-00AA00?style=for-the-badge&logoColor=white)](https://rich.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)

A Python CLI tool for tracking, analysing, and visualising your data from walks/runs. The tool allows you to log your data via the CLI, then use various commands to view roundups or graphs of your stats.

## Features

- **Walk Tracking**: Log walks with steps, distance, elevation, heart rate, temperature, time of day and weather conditions. Average pace and step distance are then calculated
- **Heart Rate Prediction**: If unknown, estimate heart rate based on walk characteristics using linear regression
- **Rich Analytics**: View totals, averages, maximums, and compare stats across timeframes
- **Data Visualization**: Plot trends, weekly/monthly charts, and performance over time
- **Data Management**: Add, edit, delete, and export walk data to CSV
- **Interactive CLI**: User-friendly command interface with searchable command list

## Available Commands

| Category | Commands |
|----------|----------|
| **Data** | `add`, `delete`, `edit`, `show`, `list`, `export csv` |
| **Stats** | `total stats`, `average stats`, `max stats`, `date stats`, `compare stats` |
| **Visualisation** | `plot trend`, `weekly steps`, `monthly steps`, `weekly distance`, `monthly distance` |
| **Misc** | `cmds`, `category cmds`, `quit` |

Type `cmds` when running to see all available commands and their descriptions.

## How To Run

### Prerequisites

- **Python** 3.10+
- **pip** (Python package manager)

### Run The Tracker

```bash
git clone https://github.com/ThomasFraserDev/walk-tracker.git
cd walk-tracker
pip install -r requirements.txt
python src/main.py
```

## Dependencies

- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualisation
- **scikit-learn**: Machine learning models
- **rich**: Beautiful terminal output

## Contributing

Contributions are welcome! :]

If you’d like to help improve this walk tracker, please follow these steps:
1. Fork the repository and create a new branch from main.
2. For UI changes, screenshots or short clips are encouraged.
3. Make sure the project runs locally:
```bash
npm install
npm run dev
```
4. Open a Pull Request with:
- A clear description of what you changed or added 
- The reasoning behind it

If you’re unsure about an idea or want feedback before starting, feel free to open an issue to discuss it first.

Thanks for helping make this project better! 💜

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
