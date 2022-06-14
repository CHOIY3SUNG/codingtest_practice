// x만큼 간격이 있는 n개의 숫자
import UIKit

func solution(_ x:Int, _ n:Int) -> [Int64] {
    var answer: [Int64] = []
    for i in 1...n{
        answer.append(Int64(x*i))
    }
    return answer
}

solution(10, 5)
