import turtle
import math
import csv
import json
from itertools import permutations

# ---------- Logger for Animation Export -----------
class KolamLogger:
    def __init__(self):
        self.movement_log = []
        self.current_time_ms = 0
        self.time_step_ms = 50

    def log_position(self, action, turtle_obj):
        x, y = turtle_obj.pos()
        self.movement_log.append({
            "time_ms": self.current_time_ms,
            "x": x,
            "y": y,
            "action": action
        })
        self.current_time_ms += self.time_step_ms

    def export_data(self):
        with open("kolam_coords.json", "w") as jf:
            json.dump(self.movement_log, jf, indent=4)
        with open("kolam_coords.csv", "w", newline='') as cf:
            writer = csv.DictWriter(cf, fieldnames=["time_ms", "x", "y", "action"])
            writer.writeheader()
            writer.writerows(self.movement_log)

# ---------- KolamRuleEngine: Generates L-System patterns based on chosen rule -----------
class KolamRuleEngine:
    def __init__(self, dot_count, iterations):
        self.dot_count = dot_count
        self.iterations = iterations

    def select_rule(self):
        # Display the available rules for the user:
        print("\nSelect a rule to apply (for generating the Kolam pattern):")
        print("1. Anthathi Loop (even dots, >= 4) - Loop drawing with a single continuous path")
        print("2. Step Kolam (odd dots) - Interlaced, triangular dot arrangements")
        print("3. 45° Grid Transform - Uses diagonal grid transforms (placeholder example)")
        print("4. Suli Arc Curve - Emphasizes smooth arcs drawn around points")
        print("5. Spiral Kolam - A free spiral pattern (smooth continuous curve)")
        print("6. Mirror Symmetry - Creates a symmetric pattern by reflection")
        choice = int(input("👉 Enter rule number (1-6): "))
        return self.apply_rule(choice, self.iterations)

    def apply_rule(self, choice, iterations):
        axiom = "F"
        rules = {}

        # Define rule-based L-system rewriting
        if choice == 1:  # Anthathi Loop
            axiom = "FBFBFBFB"
            rules = {"A": "AFBFA", "B": "AFBFBFBFA", "F": "F"}
        elif choice == 2:  # Step Kolam
            axiom = "A"
            rules = {"A": "FBF", "B": "AFBFA", "F": "F"}
        elif choice == 3:  # 45° Grid Transform (Placeholder implementation)
            return "AFBFBFAAF"
        elif choice == 4:  # Suli Arc Curve
            return "ABFABFAB"
        elif choice == 5:  # Spiral Kolam
            return "FFFFFFFFFF"
        elif choice == 6:  # Mirror Symmetry
            axiom = "FBF"
            rules = {"F": "F", "B": "BF", "A": "AB"}
        else:
            print("Invalid choice. Using default pattern.")
            return "FAFBFBFA"
        
        return self.generate_lsystem(axiom, iterations, rules)

    def generate_lsystem(self, axiom, iterations, rules):
        for _ in range(iterations):
            axiom = ''.join([rules.get(ch, ch) for ch in axiom])
        return axiom

# ---------- KolamMatrixGenerator: Generates dot matrices and a spiral path -----------
class KolamMatrixGenerator:
    def __init__(self, rows, cols=None):
        self.rows = rows
        self.cols = cols or rows

    def generate_square_matrix(self):
        return [[(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def generate_triangle_matrix(self):
        return [[(r, c) for c in range(r + 1)] for r in range(self.rows)]

    def generate_rectangle_matrix(self):
        return [[(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def get_spiral_path(self, matrix):
        """
        Returns the coordinates of the matrix in spiral (clockwise) order.
        """
        spiral = []
        while matrix:
            # Take the first row.
            spiral += matrix.pop(0)
            # Take the last element of each remaining row.
            if matrix and matrix[0]:
                for row in matrix:
                    spiral.append(row.pop())
            # Take the bottom row in reverse order.
            if matrix:
                spiral += matrix.pop()[::-1]
            # Take the first element of each remaining row (in reverse order).
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiral.append(row.pop(0))
        return spiral

# ---------- KolamVisualizer: Draws the L-System pattern via Turtle graphics -----------
class KolamVisualizer:
    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger
        self.turtle = turtle.Turtle()
        self.colors = ["red", "green", "blue", "purple"]
        self.color_index = 0
        self.turtle.speed(0)
        self.turtle.pensize(2)
        self.turtle.penup()
        self.turtle.setpos(0, 0)
        self.turtle.pendown()

    def next_color(self):
        col = self.colors[self.color_index]
        self.color_index = (self.color_index + 1) % len(self.colors)
        return col

    def draw_pattern(self):
        for cmd in self.pattern:
            if cmd == "F":
                self.turtle.pencolor(self.next_color())
                self.turtle.forward(10)
                self.logger.log_position("forward", self.turtle)
            elif cmd == "A":
                self._suli_arc(10, 90)
            elif cmd == "B":
                self._combo_arc()

    def _suli_arc(self, r, sweep):
        self.turtle.pencolor(self.next_color())
        steps = int(abs(sweep) / 5)
        for _ in range(steps):
            self.turtle.circle(r, sweep / steps)
            self.logger.log_position("arc", self.turtle)

    def _combo_arc(self):
        I = 5 / math.sqrt(2)
        self.turtle.forward(I)
        self.logger.log_position("forward-B-start", self.turtle)
        self.turtle.circle(I, 270)
        self.logger.log_position("arc-B", self.turtle)
        self.turtle.forward(I)
        self.logger.log_position("forward-B-end", self.turtle)

    def show(self):
        self.turtle.hideturtle()
        self.logger.export_data()
        turtle.done()

# ---------- MatrixVisualizer: Draws a closed path for a set of matrix coordinates -----------
class MatrixVisualizer:
    def __init__(self, coord_list, logger, scale=50):
        """
        coord_list: List of (row, col) coordinates.
        scale: Scaling factor to convert matrix units to pixels.
        """
        self.coord_list = coord_list
        self.logger = logger
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.pensize(2)
        self.turtle.penup()
        self.scale = scale

    def draw_path(self):
        # Convert first coordinate and move there.
        if not self.coord_list:
            return
        first = self.coord_list[0]
        x, y = first[1] * self.scale, -first[0] * self.scale  # Adjust coordinate mapping
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.logger.log_position("start", self.turtle)
        # Draw path through all coordinates
        for coord in self.coord_list[1:]:
            x, y = coord[1] * self.scale, -coord[0] * self.scale
            self.turtle.goto(x, y)
            self.logger.log_position("move", self.turtle)
        # Close the loop back to the first coordinate
        self.turtle.goto(first[1] * self.scale, -first[0] * self.scale)
        self.logger.log_position("close_loop", self.turtle)

    def show(self):
        self.turtle.hideturtle()
        self.logger.export_data()
        turtle.done()

# ---------- KolamApp: Main class to integrate input, rule selection, and drawing -----------
class KolamApp:
    def __init__(self):
        self.dot_count = int(input("Enter dot count for nxn matrix: "))
        self.iterations = int(input("Enter number of iterations (for L-System) [e.g., 2]: "))
        self.mode = input("Select drawing mode: 'l' for L-System, 'm' for Matrix path: ").lower()
        self.logger = KolamLogger()
        self.matrix_type = input("Enter matrix type (square/triangle/rectangle): ").lower()

    def run(self):
        if self.mode == 'l':
            # Use L-System mode (rule engine)
            rule_engine = KolamRuleEngine(self.dot_count, self.iterations)
            pattern = rule_engine.select_rule()
            visualizer = KolamVisualizer(pattern, self.logger)
            visualizer.draw_pattern()
            self.logger.export_data()
            visualizer.show()
        elif self.mode == 'm':
            # Use matrix mode: generate matrix and then a spiral closed path
            matrix_gen = KolamMatrixGenerator(self.dot_count)
            if self.matrix_type == "triangle":
                matrix = matrix_gen.generate_triangle_matrix()
            elif self.matrix_type == "rectangle":
                # For rectangle, ask for additional column count
                cols = int(input("Enter number of columns for the rectangle: "))
                matrix = matrix_gen.generate_rectangle_matrix()  # The generator uses dot_count as rows
                # Alternatively, reinitialize with rows and cols:
                matrix_gen = KolamMatrixGenerator(self.dot_count, cols)
                matrix = matrix_gen.generate_rectangle_matrix()
            else:
                # Default to square matrix
                matrix = matrix_gen.generate_square_matrix()
            
            # Get spiral (closed) path; clone the matrix to avoid altering it.
            import copy
            matrix_copy = copy.deepcopy(matrix)
            spiral_coords = matrix_gen.get_spiral_path(matrix_copy)
            # You could also use other traversal methods (or even iterate through all permutation paths)
            # if more variety is needed.
            visualizer = MatrixVisualizer(spiral_coords, self.logger)
            visualizer.draw_path()
            self.logger.export_data()
            visualizer.show()
        else:
            print("Invalid mode selected. Exiting.")

# ---------- Run the Application -----------
if __name__ == "__main__":
    turtle.setup(800, 800)
    turtle.bgcolor("white")
    turtle.title("Kolam Designer with L-System and Matrix Path")
    app = KolamApp()
    app.run()

