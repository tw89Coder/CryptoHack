# Modular Arithmetic 學習筆記

本文件整理自 CryptoHack Modular Arithmetic 課程，涵蓋基礎模運算、GCD、費馬小定理、二次剩餘、勒讓德符號、Tonelli-Shanks 演算法與中國剩餘定理 (CRT)。

## 目錄

1. [基礎運算 (GCD & Extended GCD)](#1-基礎運算-gcd--extended-gcd)
2. [模運算基礎 (Modular Arithmetic & Inverses)](#2-模運算基礎-modular-arithmetic--inverses)
3. [二次剩餘 (Quadratic Residues)](#3-二次剩餘-quadratic-residues)
4. [大數開根號 (Modular Square Root)](#4-大數開根號-modular-square-root)
5. [中國剩餘定理 (Chinese Remainder Theorem)](#5-中國剩餘定理-chinese-remainder-theorem)
6. [代數技巧與二項式 (Modular Binomials)](#6-代數技巧與二項式-modular-binomials)
7. [Python 函數速查](#7-python-函數速查)

---

## 1. 基礎運算 (GCD & Extended GCD)

### 最大公因數 (GCD)
Euclid's Algorithm (歐幾里得演算法) 用於快速計算兩個數的最大公因數。
原理：
```math
\gcd(a, b) = \gcd(b, a \pmod b)
```
> 費曼解釋：**長方形鋪磚**
> 想像一個 $a \times b$ 的長方形，你想用「最大的正方形」鋪滿它。如果你先鋪滿一個 $b \times b$ 的區域，剩下的部分就是 $(a-b) \times b$。重複這個「取餘數」的過程，直到兩邊相等，那個最終的正方形就是 GCD。

### 擴展歐幾里得演算法 (Extended Euclidean Algorithm)
除了計算 GCD，還能找出整數係數 $u, v$ 使得：
```math
a \cdot u + b \cdot v = \gcd(a, b)
```

* **應用直覺：** 這代表任何兩個數的公因數，都可以由這兩個數透過「加減組合」出來。
* **模反元素：** 當 $\gcd(a, n) = 1$ 時，組合式變為 $a \cdot u + n \cdot v = 1$，這意味著在模 $n$ 下， $a \cdot u \equiv 1$ ，因此 $u$ 就是 $a$ 的倒數。
---

## 2. 模運算基礎 (Modular Arithmetic & Inverses)

### 定義
```math
a \equiv b \pmod m
```
表示 $a$ 除以 $m$ 的餘數等於 $b$ 。

### 費馬小定理 (Fermat's Little Theorem)
若 $p$ 為質數，且 $a$ 不是 $p$ 的倍數，則：
```math
a^{p-1} \equiv 1 \pmod p
```
> 費曼解釋：**模世界的週期性**
> 想像一個有 $p$ 個刻度的圓形時鐘。如果你以步長 $a$ 不斷旋轉，因為 $p$ 是質數，你必須繞完 $p-1$ 圈後才會剛好回到起點 1。

**重要推論：**
```math
a^{p-2} \equiv a^{-1} \pmod p
```
這提供了一種計算模反元素的方法（僅限模數為質數時）。

### 模反元素 (Modular Inverse)
尋找 $d$ 使得 $a \cdot d \equiv 1 \pmod n$ 。
若 $\gcd(a, n) \neq 1$，則模反元素不存在。

---

## 3. 二次剩餘 (Quadratic Residues)

### 定義
若存在整數 $x$ 使得 $x^2 \equiv a \pmod p$，則稱 $a$ 為模 $p$ 的二次剩餘 (Quadratic Residue, QR)。否則稱為二次非剩餘 (Quadratic Non-Residue, QNR)。

* **直覺理解：** 這是在問「在模世界中， $a$ 是否為一個完全平方數？」

### 性質
- $QR \times QR = QR$
- $QNR \times QNR = QR$
- $QR \times QNR = QNR$

### 勒讓德符號 (Legendre Symbol)
用於快速判斷 $a$ 是否為模 $p$ 的二次剩餘。
公式：
```math
\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p
```

**結果判讀：**
- **1**: $a$ 是二次剩餘 (QR)。
- **-1** (即 $p-1$): $a$ 是二次非剩餘 (QNR)。
- **0**: $a$ 是 $p$ 的倍數。

> **費曼解釋：平方數過濾器** 根據費馬小定理， $a^{p-1} \equiv 1$ 。我們可以將其拆解為 $(a^{(p-1)/2})^2 \equiv 1$ 。在模質數下，只有 $1$ 與 $-1$ 的平方是 $1$。因此 $a^{(p-1)/2}$ 就像一個過濾器，結果為 $1$ 代表它是平方數（QR）， $-1$ 則不是。

---

## 4. 大數開根號 (Modular Square Root)

解方程式 $x^2 \equiv a \pmod p$ 。

### 情況一： $p \equiv 3 \pmod 4$
若質數 $p$ 除以 4 餘 3，有簡單公式可直接求根：
```math
x \equiv \pm a^{(p+1)/4} \pmod p
```
> **推導邏輯：** 我們已知 $a^{(p-1)/2} \equiv 1$。兩邊同乘 $a$ 得到 $a^{(p+1)/2} \equiv a$ 。 寫成平方形式： $(a^{(p+1)/4})^2 \equiv a$ 。因此直接開根號即可得到結果。

### 情況二： $p \equiv 1 \pmod 4$ (Tonelli-Shanks)
若質數 $p$ 除以 4 餘 1，必須使用 **Tonelli-Shanks Algorithm**。
這是一個迭代演算法，將 $p-1$ 分解為 $Q \cdot 2^S$，透過不斷逼近來求根。

> **費曼解釋：** 當我們不能直接計算時，我們找一個「非平方數」作為基準，不斷修正我們的猜測值，直到誤差消除為止。

---

## 5. 中國剩餘定理 (Chinese Remainder Theorem)

### 定義
若已知 $x$ 對一組兩兩互質的模數 $n_i$ 的餘數 $a_i$：
```math
\begin{cases}
x \equiv a_1 \pmod {n_1} \\
x \equiv a_2 \pmod {n_2} \\
\dots
\end{cases}
```
則 $x$ 在模 $N = n_1 \times n_2 \times \dots$ 下有唯一解。

> **費曼解釋：多維度時鐘對齊** 你有多個不同週期的時鐘（例如 3 小時一圈、5 小時一圈）。只要知道每個時鐘現在的指針位置，且週期之間互質，你就能推算出總共過了幾小時。


### 解法 (Gauss Algorithm)
```math
x \equiv \sum (a_i \cdot N_i \cdot y_i) \pmod N
```
其中：
- $N_i = N / n_i$
- $y_i \equiv N_i^{-1} \pmod {n_i}$ (模反元素)

---

## 6. 代數技巧與二項式 (Modular Binomials)

### 問題特徵
當遇到多項式型態的加密，例如：
```math
c_1 \equiv (Ap + Bq)^{e_1} \pmod N
```
```math
c_2 \equiv (Cp + Dq)^{e_2} \pmod N
```

### 解決策略
1. 利用模運算性質分別對模 $p$ 和模 $q$ 進行簡化。
2. 尋找 $c_1, c_2$ 之間的代數關係，構造出一個差值 $K$ 。
3. 若推導出 $K \equiv 0 \pmod p$ 但 $K \neq 0$，則可利用 GCD 進行因數分解：
```math
p = \gcd(K, N)
```

這是一種不需要 RSA 私鑰也能分解 $N$ 的數學攻擊方式。

> **核心思維：** $K$ 裡面包含了 $p$ 的成分，但沒有 $q$。透過 $\gcd(K, N)$，我們能直接把躲在 $N$ 裡面的 $p$ 抓出來。這是不需要私鑰就能分解大數的強大武器。

---

## 7. Python 函數速查

以下列出常用的 Python 內建函數：

* **`math.gcd(a, b)`**
    計算最大公因數。

* **`pow(base, exp, mod)`**
    快速模冪運算 ($base^{exp} \pmod {mod}$)。

* **`pow(a, -1, n)`**
    計算模反元素 (求 $a$ 在模 $n$ 下的倒數)。

* **`pow(a, (p-1)//2, p)`**
    勒讓德符號 (檢查是否為二次剩餘)。

* **`pow(a, (p+1)//4, p)`**
    當 $p \equiv 3 \pmod 4$ 時的開根號公式。