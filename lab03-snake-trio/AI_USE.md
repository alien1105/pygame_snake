# | When | Person asking | Question or prompt | Hint received | Human decision and verification |
|---|---|---|---|---|
| 2026-08-12 | 你的名字 | 詢問 Step 3 邊界碰撞應該如何完成 | AI 說明合法與非法座標範圍、四面牆判斷概念和測試方法；未提供完整函式內容 | 我根據提示自行實作；測試完成後記錄實際結果 |
我根據提示自行修改 hit_wall，並執行公開的四邊界測試，通過
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
|2026/08/12/16:11|林承緯|def ate_food(head: Cell, food: Cell) -> bool:
    """Return True exactly when the snake head occupies the food cell.

    Hint: both values use the same ``(x, y)`` tuple format.
    """
    # TODO 2: replace this line with one boolean return statement.
    raise NotImplementedError("TODO 2: compare head and food")
可以幫我把這個函式新增吃東西的程式碼，我的需求是food會生成在地圖的隨機位置，但不可生成在地圖外和head及body的位置，一次只生成一個food，head碰到food後，food會消失並繼續隨機生成|你的邏輯非常清晰，把貪吃蛇吃食物的完整流程（包含判斷、消失、避免生成在蛇身上、再生成）想得很周到！不過，在這個專案的架構中，你不需要把食物生成的邏輯寫在這個函式裡。這是一個分工合作的設計：你的任務 (logic.py)： ate_food 函式的職責非常單純，它只需要做一件事——判斷蛇頭的座標是否剛好等於食物的座標。如果是，就回傳 True，否則回傳 False。  系統的任務 (game.py)： 當你的 ate_food 回傳 True 給系統時，game.py 裡面的 step 函式就會自動幫你加分，並且呼叫 choose_food 函式來負責尋找下一個不在蛇身上的空位，生成新的食物。  因此，你只需要用一行程式碼，將 head 與 food 進行比較即可。程式碼實作請將 logic.py 中的 TODO 2 替換成以下程式碼：Pythondef ate_food(head: Cell, food: Cell) -> bool:
    """Return True exactly when the snake head occupies the food cell.

    Hint: both values use the same ``(x, y)`` tuple format.
    """
    return head == food
這樣寫就足夠了！Python 中的 == 可以直接比較兩個 Tuple（即 (x, y) 座標）是否完全相同。剩下的生成工作，系統會完美地幫你接手。|在ate_food()的函式裡新增return head == food|
|2026/08/12/16:18|林承緯|那game.py有要新增甚麼程式碼啊|完全不需要新增任何程式碼！根據系統提供的檔案說明，在這次的核心任務中，你不需要編輯 game.py 這個檔案。  game.py 的定位是這個貪吃蛇遊戲的「外殼（Presentation Shell）」。它已經幫你把所有基礎建設都寫好了，包含：  處理鍵盤輸入（上下左右控制方向）。  繪製遊戲畫面與格子。  管理遊戲狀態（分數、遊戲結束、重新開始）。  隨機生成食物（choose_food 函式已經處理了避免食物生成在蛇身上的邏輯）。  它唯一依賴的，就是呼叫你在 logic.py 裡面寫好的四個核心函式（next_head、ate_food、hit_wall、advance_body）來決定遊戲下一步該長什麼樣子。  所以，你只要專心把 logic.py 裡面的 4 個 TODO 完成，直接執行 game.py，你的貪吃蛇遊戲就能順利運作了！|理解具體要做什麼了|
|2026/08/12/16:22|林承緯|def advance_body(body: list[Cell], new_head: Cell, grow: bool) -> list[Cell]:
    """Return the next snake body without changing ``body``.

    The returned list always begins with ``new_head``.  When ``grow`` is True,
    keep every old segment.  Otherwise remove only the old tail.
    """
    # TODO 4: build and return a new list.  Never call body.insert/pop/remove.
    raise NotImplementedError("TODO 4: create the next body")
幫我新增程式碼，我的需求是頭碰到食物身體長度會+1|這個 advance_body 函式的設計非常巧妙。系統傳入的 grow 參數，其實就已經代表了「頭是否碰到食物」的結果（因為 game.py 會把剛才 ate_food 的結果傳遞給這個 grow 參數）。  根據你的需求與檔案中的規定，這段程式碼必須滿足以下條件：回傳的新列表必須以 new_head 為開頭。  如果 grow 為 True（代表吃到食物），我們要保留所有舊的身體段落（這樣加上新蛇頭，總長度就會 +1）。  如果 grow 為 False（代表只是單純移動），我們要移除舊的蛇尾。  絕對不能使用 body.insert、body.pop 或 body.remove 來修改原本的列表。  為了達成「不修改原列表」的要求，我們可以使用 Python 的列表相加與切片（Slicing）技巧。請將 logic.py 中的 TODO 4 替換成以下程式碼：Pythondef advance_body(body: list[Cell], new_head: Cell, grow: bool) -> list[Cell]:
    """Return the next snake body without changing ``body``.

    The returned list always begins with ``new_head``.  When ``grow`` is True,
    keep every old segment.  Otherwise remove only the old tail.
    """
    if grow:
        # 吃到食物：新蛇頭 + 完整的舊身體（長度 +1）
        return [new_head] + body
    else:
        # 單純移動：新蛇頭 + 除了最後一節以外的舊身體（長度不變）
        return [new_head] + body[:-1]
程式碼原理解釋：[new_head]：我們將新蛇頭變成一個單一元素的列表，這樣才能與後面的 body 列表相加。這滿足了「回傳的列表總是以 new_head 開頭」的規定。  body[:-1]：這是 Python 的切片語法，代表「從開頭取到倒數第二個元素」，這完美達成了「只移除舊蛇尾」的要求，而且不會像 .pop() 那樣去修改到原本的 body 內容。  |在advance_body()函式裡新增if grow:
        # 吃到食物：新蛇頭 + 完整的舊身體（長度 +1）
        return [new_head] + body
    else:
        # 單純移動：新蛇頭 + 除了最後一節以外的舊身體（長度不變）
        return [new_head] + body[:-1]|

If no AI was used, write: `No AI used.`
