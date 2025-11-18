# Day 6 – Reeborg’s World Challenges

Welcome to Day 6 of my Python learning journey! Today, we focused on **functions, loops, conditionals, and problem-solving** using the Reeborg’s World coding environment. The challenges included Hurdle Races of varying difficulty and a Maze Escape. This README explains each challenge and the Python concepts practiced.

---

## **1. Python Concepts Practiced**
- **Defining and calling functions**  
  - Example: `turn_right()`, `jump()`
- **While loops**
  - Repeat actions until a condition is met (`while not at_goal():`)
- **If / elif / else statements**
  - Decision-making based on conditions (e.g., `wall_in_front()`, `right_is_clear()`)
- **Indentation**
  - Correct code blocks under loops and conditionals
- **Problem-solving**
  - Breaking down complex movements into reusable functions

---

## **2. Hurdle Race Challenges**

### **Overview**
Reeborg must run a course with hurdles. The position and height of hurdles vary depending on the world. The goal is to reach the end without hitting walls.

### **Challenge Progression**
1. **Hurdles 1**
   - Fixed-height hurdles
   - Simple `jump()` function
   ```python
   def jump():
       turn_left()
       move()
       turn_right()
       move()
       turn_right()
       move()
       turn_left()
