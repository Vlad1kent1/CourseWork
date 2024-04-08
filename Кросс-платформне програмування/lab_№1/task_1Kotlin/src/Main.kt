import kotlin.math.abs

fun main() {
    print("Enter first number: ")
    val num1: Double = readln().toDouble()
    print("Enter second number: ")
    val num2: Double = readln().toDouble()

    val sum: Double = abs(num1) + abs(num2)
    val difference: Double = abs(num1) - abs(num2)
    val product: Double = abs(num1) * abs(num2)
    val quotient: Double = abs(num1) / abs(num2)

    print("Sum of modules: $sum")
    print("\nDifference of modules: $difference")
    print("\nProduct of modules: $product")
    print("\nShare of modules: $quotient")
}
