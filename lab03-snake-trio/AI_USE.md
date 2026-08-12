# AI Use Record - L1

L1 permits explanations, hints, counterexamples, test ideas, and traceback help. It does not permit AI to write or replace the four final function bodies.

| When | Person asking | Question or prompt | Hint received | Human decision and verification |
|2026/08/12|林承緯|def next_head(head: Cell, direction: Direction, cell_size: int) -> Cell:
    """Return the next head cell.

    Interface:
        head: current ``(x, y)`` grid position.
        direction: one of ``(-1, 0)``, ``(1, 0)``, ``(0, -1)``, ``(0, 1)``.
        cell_size: positive number of pixels moved in one step.
        return: a new ``(x, y)`` tuple.

    Hint: calculate x and y separately.  Do not mutate any input.
    """
    # TODO 1: replace this line with one return statement.
    raise NotImplementedError("TODO 1: compute the next head")
幫我按照要求完成這段程式碼|這是一段計算貪食蛇（或類似網格遊戲）蛇頭下一步位置的程式碼。你可以使用以下寫法來完成：

Python
def next_head(head: Cell, direction: Direction, cell_size: int) -> Cell:
    """Return the next head cell.

    Interface:
        head: current ``(x, y)`` grid position.
        direction: one of ``(-1, 0)``, ``(1, 0)``, ``(0, -1)``, ``(0, 1)``.
        cell_size: positive number of pixels moved in one step.
        return: a new ``(x, y)`` tuple.

    Hint: calculate x and y separately.  Do not mutate any input.
    """
    return (head[0] + direction[0] * cell_size, head[1] + direction[1] * cell_size)
程式碼邏輯說明：
head[0] 與 head[1] 分別代表當前蛇頭的 X 與 Y 座標。

direction[0] 與 direction[1] 代表 X 與 Y 軸的移動方向（例如 (-1, 0) 表示向左移動，X 軸減 1）。

乘上 cell_size 是因為每次移動的距離是依照網格大小決定，而不是只移動 1 像素。

最後將計算好的新 X 與新 Y 座標打包成一個新的 tuple (new_x, new_y) 回傳，這樣就不會修改到原本的 head 變數。|在next_head()函式新增return (head[0] + direction[0] * cell_size, head[1] + direction[1] * cell_size)|
| | | | | |

If no AI was used, write: `No AI used.`
