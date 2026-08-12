"""Four small, testable rules used by the supplied Pygame shell.

Your trio edits only this file for the core mission.  Keep every function pure:
do not import Pygame, open a window, read the keyboard, or change the supplied
``body`` list in place.
"""

from __future__ import annotations

Cell = tuple[int, int]
Direction = tuple[int, int]


def next_head(head: Cell, direction: Direction, cell_size: int) -> Cell:
    ef ate_food(head: Cell, food: Cell) -> bool:
   def create_snake(start_x, start_y, block_size):
       snake_tail = {
        "name": "snake_tail",
        "x": start_x,
        "y": start_y,
    }
    snake_body = {
        "name": "snake_body",
        "x": start_x + block_size,
        "y": start_y,
    }
    snake_head = {
        "name": "snake_head",
        "x": start_x + block_size * 2,
        "y": start_y,
    }
def is_wall_collision(
    next_x,
    next_y,
    wall_left,
    wall_right,
    wall_top,
    wall_bottom,
    block_size,
):
    if next_x < wall_left:
        return True
    if next_x + block_size > wall_right:
        return True
    if next_y < wall_top:
        return True
    if next_y + block_size > wall_bottom:
        return True
    return False
    return [snake_tail, snake_body, snake_head]
    def get_next_head_position(snake_head, direction, block_size):
        next_x = snake_head["x"]
        next_y = snake_head["y"]

        if direction == "LEFT":
            next_x -= block_size
        elif direction == "RIGHT":
            next_x += block_size
        elif direction == "UP":
            next_y -= block_size
        elif direction == "DOWN":
            next_y += block_size
        return next_x, next_y
def is_valid_move(next_x, next_y, snake_body):
    if (
        next_x == snake_body["x"]
        and next_y == snake_body["y"]
    ):
        return False
    return True
    def is_body_collision(next_x, next_y, snake_body):
        return (
            next_x == snake_body["x"]
            and next_y == snake_body["y"]
        )

    def grow_snake(body, grow):
        new_body = [new_head] + body
        return new_body
    def move_snake(snake, next_x, next_y):
        snake_tail = snake[0]
        snake_body = snake[1]
        snake_head = snake[2]
        old_body_x = snake_body["x"]
        old_body_y = snake_body["y"]
        old_head_x = snake_head["x"]
        old_head_y = snake_head["y"]
        snake_tail["x"] = old_body_x
        snake_tail["y"] = old_body_y
        snake_body["x"] = old_head_x
        snake_body["y"] = old_head_y
        snake_head["x"] = next_x
        snake_head["y"] = next_y
        return new_body
        
    def game_over(
        start_x,
        start_y,
        block_size,
        current_score,
    ):
        current_score = 0
        snake = create_snake(
            start_x,
            start_y,
            block_size,
        )
    def update_score(current_score, max_score):
        current_score += 1
        if current_score > max_score:
            max_score = current_score
            return current_score, max_score
    return snake, current_score
    def update_snake(snake, direction, block_size, wall_left, wall_right, wall_top, wall_bottom):
        snake_head = snake[2]
        snake_body = snake[1]
        next_x, next_y = get_next_head_position(
            snake_head,
            direction,
            block_size,
        )

        if is_wall_collision(
            next_x,
            next_y,
            wall_left,
            wall_right,
            wall_top,
            wall_bottom,
            block_size,
        ):
            return False

        if is_body_collision(
            next_x,
            next_y,
            snake_body,
        ):
            return False

        if not is_valid_move(
            next_x,
            next_y,
            snake_body,
        ):
            return False

        move_snake(
            snake,
            next_x,
            next_y,
        )
        return True
    def initialize_game():
        level = 1
        max_score = 0
        current_score = 0
        block_size = 20
        wall_left = 40
        wall_top = 40
        wall_right = 760
        wall_bottom = 560
        start_x = 300
        start_y = 300

        snake = create_snake(
            start_x,
            start_y,
            block_size,
        )
        direction = "RIGHT"
        return {
            "level": level,
            "max_score": max_score,
            "current_score": current_score,
            "block_size": block_size,
            "wall_left": wall_left,
            "wall_top": wall_top,
            "wall_right": wall_right,
            "wall_bottom": wall_bottom,
            "snake": snake,
            "direction": direction,
        }
    def initialize_game():
        level = 1
        max_score = 0
        current_score = 0

        block_size = 20

        wall_left = 40
        wall_top = 40
        wall_right = 760
        wall_bottom = 560
        start_x = 300
        start_y = 300

        snake = create_snake(
            start_x,
            start_y,
            block_size,
        )

        direction = "RIGHT"

        return {
        "level": level,
        "max_score": max_score,
        "current_score": current_score,
        "block_size": block_size,
        "wall_left": wall_left,
        "wall_top": wall_top,
        "wall_right": wall_right,
        "wall_bottom": wall_bottom,
        "snake": snake,
        "direction": direction,
    }
    def update_game(game):
        snake = game["snake"]

        moved = update_snake(
            snake=snake,
            direction=game["direction"],
            block_size=game["block_size"],
            wall_left=game["wall_left"],
            wall_right=game["wall_right"],
            wall_top=game["wall_top"],
            wall_bottom=game["wall_bottom"],
        )
        if not moved:
            game["snake"], game["current_score"] = game_over(
                start_x=300,
                start_y=300,
                block_size=game["block_size"],
                current_score=game["current_score"],
            )
            game["direction"] = "RIGHT"
            return False
        game["current_score"] += 1
        if game["current_score"] > game["max_score"]:
            game["max_score"] = game["current_score"]
        return True
    # TODO 1: replace this line with one return statement.
    raise NotImplementedError("TODO 1: compute the next head")
    # TODO 2: replace this line with one boolean return statement.
    raise NotImplementedError("TODO 2: compare head and food")


def hit_wall(head: Cell, width: int, height: int, cell_size: int) -> bool:
    """Return True when any part of the head is outside the board.

    Legal x values begin at 0 and stop before ``width``.
    Legal y values begin at 0 and stop before ``height``.
    The head is aligned to the grid, so its top-left coordinate is enough.
    """
    # TODO 3: check left, right, top, and bottom boundaries.
    raise NotImplementedError("TODO 3: check four wall boundaries")


def advance_body(body: list[Cell], new_head: Cell, grow: bool) -> list[Cell]:
    """Return the next snake body without changing ``body``.

    The returned list always begins with ``new_head``.  When ``grow`` is True,
    keep every old segment.  Otherwise remove only the old tail.
    """
    # TODO 4: build and return a new list.  Never call body.insert/pop/remove.
    raise NotImplementedError("TODO 4: create the next body")
