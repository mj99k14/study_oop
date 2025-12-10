#기말고사  magic method역할
from typing import List

class Tensor:
    def __init__(self, data: List[List[float]]):
        """
        생성자: 1~2차원 실수 데이터를 받아 초기화
        """
        self.data = data

    def __repr__(self) -> str:
 
        return f"Tensor({self.data})"

    def __matmul__(self, other: 'Tensor') -> 'Tensor':
        """
        Magic Method: @ 연산자 정의
        W @ T 수행 시 자동으로 호출됨
        """
        A = self.data
        B = other.data

        row_A = len(A)
        col_A = len(A[0])
        col_B = len(B[0])

        # 결과 행렬 (row_A × col_B) 초기화
        result_data = [[0.0 for _ in range(col_B)] for _ in range(row_A)]

        # 행렬 곱셈 수행
        for i in range(row_A):
            for j in range(col_B):
                for k in range(col_A):
                    result_data[i][j] += A[i][k] * B[k][j]

        return Tensor(result_data)

# --- 실행 예시 ---
W = Tensor([[1.0, 2.0],
            [3.0, 4.0]])   # 2×2

T = Tensor([[5.0],
            [6.0]])        # 2×1

R = W @ T                  # W.__matmul__(T) 자동 호출
print(R)
