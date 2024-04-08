import java.util.*
import kotlin.math.sqrt

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val scanner = Scanner(System.`in`)

        println("Enter values for coefficients a, b, and c:")
        print("a: ")
        val a = scanner.nextDouble()
        print("b: ")
        val b = scanner.nextDouble()
        print("c: ")
        val c = scanner.nextDouble()

        val solution = findSolution(a, b, c)

        System.out.printf("Solution to the inequality (x + %f)(x^2 - %f*x + %f) > 0:%n", a, b, c)
        println("Solution: $solution")

        scanner.close()
    }

    fun findSolution(a: Double, b: Double, c: Double): String {
        val discriminant = b * b - 4 * c
        if (discriminant < 0) {
            return "No solution"
        } else if (discriminant == 0.0) {
            val root = b / (2)
            return if (a < 0) if ((a >= root || 0 > root)) "(0; inf)" else "(0; $root)u($root; inf)"
            else if (-a > root) "(" + (-a) + "; inf)"
            else if (-a < root) "(" + (-a) + "; " + root + ")u(" + root + "; inf)"
            else "(-inf; $root)u($root; inf)"
        } else {
            val root1 = (b - sqrt(discriminant)) / (2)
            val root2 = (b + sqrt(discriminant)) / (2)
            if (a < 0) {
                if (a >= root2) return "(0; inf)"
                else if (a < root1) return "(0; $root1)u($root2; inf)"
                else if (a >= root1 && a < root2) return "($root2; inf)"
            } else {
                return if (-a > root2) "(" + (-a) + "; inf)"
                else if (-a < root1) "(" + (-a) + "; " + root1 + ")u(" + root2 + "; inf)"
                else "($root2; inf)"
            }
            return ""
        }
    }
}