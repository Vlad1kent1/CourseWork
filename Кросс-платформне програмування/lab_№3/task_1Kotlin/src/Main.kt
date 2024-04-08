import java.lang.Math.pow
import java.util.*
import kotlin.math.abs

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val scanner = Scanner(System.`in`)
        var u: Double
        var sum = 1.0
        val eps = 0.00001
        print("Enter value x: ")
        val x = scanner.nextDouble()
        u = -x / 3
        var n = 2

        while (abs(u) > eps) {
            sum += u
            u *= -x * (3 * n - 2) / (3 * n)
            n++
        }

        println("Sum value: $sum")
        println("Library function value: %.6f".format(pow((1 + x),(-1.0 / 3.0))))
        println("Number of terms: " + (n - 1))
    }
}
