# Four Function Contracts

Write examples before implementation. Do not paste function bodies here.

| Function | Accepted input | Returned result | Invariant / non-goal | Failure or boundary examples |
|---|---|---|---|---|
| `next_head` | | | Does not mutate input. | |
| `ate_food` | | | Exact cell equality. | |
| `hit_wall` | `head` 是 `(x, y)` 座標；`width`、`height`、`cell_size` 是正整數 | 如果蛇頭超出任一邊界回傳 `True`，否則回傳 `False` | 不修改任何輸入；合法座標須滿足 `0 <= x < width` 與 `0 <= y < height` | `(0, 0) -> False`；`(620, 460) -> False`；`(-20, 0) -> True`；`(640, 0) -> True`；`(0, -20) -> True`；`(0, 480) -> True` |
| `advance_body` | | | Returns a new list. | |

## Example-to-test bridge

For each function, convert at least one row above into a student-authored test. Write the expected observation before running it.
