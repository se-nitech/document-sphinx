"""算術演算の振る舞いを選択する統合レイヤー。"""


class AddOrMult():
    """演算キーに基づいて加算または乗算を適用する。

    Attributes:
        add (Callable[[int, int], int]): 加算に使用する関数。
        mult (Callable[[int, int], int]): 乗算に使用する関数。
    """

    def __init__(self, add_func, mult_func):
        """演算ディスパッチャを初期化する。

        Args:
            add_func (Callable[[int, int], int]): 加算関数。
            mult_func (Callable[[int, int], int]): 乗算関数。
        """
        super().__init__()
        self.add = add_func
        self.mult = mult_func

    def do(self, a, b, c):
        """選択された演算を実行する。

        Args:
            a (int): 1つ目のオペランド。
            b (int): 2つ目のオペランド。
            c (str): "add" または "mult" の演算キー。

        Returns:
            int | None: 有効な演算キーの場合は計算結果、無効な場合はNone。
        """
        if c == 'add':
            return self.add(a, b)
        if c == 'mult':
            return self.mult(a, b)
        return None
