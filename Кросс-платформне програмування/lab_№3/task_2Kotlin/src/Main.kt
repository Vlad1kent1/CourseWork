import java.util.*

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val scanner = Scanner(System.`in`)
        var a: Double
        var b: Double
        var c: Double
        var d: Double
        var u: Double
        println("Введіть межі для x")
        a = scanner.nextDouble()
        b = scanner.nextDouble()
        if (a > b) {
            val temp = a
            a = b
            b = temp
        }
        var x = a
        val hx = (b - a) / 7

        println("Введіть межі для y")
        c = scanner.nextDouble()
        d = scanner.nextDouble()
        if (c > d) {
            val temp = c
            c = d
            d = temp
        }
        var y = c
        val hy = (d - c) / 7

        print("y\\x ")
        for (i in 0..7) System.out.printf("%8.2f", x + hx * i)
        println()
        for (i in 0..7) {
            System.out.printf("%5.2f", y)
            x = a
            for (j in 0..7) {
                u = x * y + 3 * y * y * y * x
                System.out.printf("%8.2f", u)
                x += hx
            }
            println()
            y += hy
        }
    }
}
