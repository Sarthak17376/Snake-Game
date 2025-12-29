# 🐍 Classic Snake Game (Python Turtle)

A modular, object-oriented implementation of the classic Arcade Snake game built using Python's `turtle` graphics library. This project demonstrates game loop logic, collision detection, inheritance, and file I/O for high-score persistence.

## 🎮 Gameplay Features

* **Classic Mechanics:** Navigate the snake to eat food, grow longer, and avoid hitting the walls or your own tail.
* **High Score Tracking:** The game automatically saves your highest score to a local file (`data.txt`).
* **Responsive Controls:** Smooth movement using keyboard arrow keys.
* **Game States:** Includes a "Start" screen and a "Game Over" state with a replay option.

## 🛠️ Project Structure & Logic

The project is structured using **Object-Oriented Programming (OOP)** to separate concerns. Each game element is its own class.

### Class Diagram
```mermaid
classDiagram
    class Snake {
        +list_of_segments
        +move_snake()
        +extend_snake()
        +up() down() left() right()
    }
    class Food {
        +food_move()
    }
    class Scoreboard {
        +score
        +highscore
        +increase_score()
        +reset_score()
    }
    class Turtle {
        <<Library>>
    }
    Snake --|> Turtle : uses
    Food --|> Turtle : inherits
    Scoreboard --|> Turtle : inherits

### File Breakdown

* **`main.py`**: The entry point. Sets up the screen, handles the main game loop, and manages key listeners.
* **`snake.py`**: Handles snake body segments, movement, and direction control.
* **`food.py`**: Inherits from Turtle to create food that respawns at random locations.
* **`scoreboard.py`**: Manages the score and reads/writes the high score to `data.txt`.
* **`data.txt`**: A simple text file used as a database to store the single integer high score.

## ⚠️ Configuration (Read Before Running)

**Please download the files to your local machine.** Do not rely on cloning tools if you are a beginner, as file paths need manual adjustment.

### 1. Download Instructions
1.  Download all project files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`, `data.txt`).
2.  Save them into a **single folder** on your computer.

### 2. Fix File Paths (Crucial Step)
The `scoreboard.py` file attempts to read `data.txt` to load the high score. Depending on your computer or code editor settings, the program might not find this file automatically if it looks for it relatively.

**You must update the file path:**
1.  Open `scoreboard.py`.
2.  Locate the line `with open("data.txt")` inside the `__init__` method and the `reset_score` method.
3.  Replace `"data.txt"` with the **absolute path** to the file on your computer.

**Example:**
```python
# In scoreboard.py, change this:
with open("data.txt") as file:

# To your specific location (Example):
with open("C:/Users/YourName/Desktop/SnakeGame/data.txt") as file:

## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the folder where you downloaded the files.
3.  Run the game:
```bash
python main.py

## 🕹️ Controls

| Key | Action |
| :--- | :--- |
| **Spacebar** | Start the game initially or Restart after a "Game Over" |
| **Arrow Keys** | Navigate the snake (Up, Down, Left, Right) |
