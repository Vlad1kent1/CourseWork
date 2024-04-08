import java.util.*

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val x = IntArray(4)
        val y = IntArray(4)
        var flag = false // змінена на var, щоб можна було змінювати
        data_entry(x, y)
        flag = checks(x, flag)
        flag = checks(y, flag)

        while (flag) {
            flag = false
            println("\nIncorrect values were entered!!!")
            data_entry(x, y)
            flag = checks(x, flag)
            flag = checks(y, flag)
        }
        println("Coordinates of the fourth vertex of the rectangle: (${x[3]}, ${y[3]})")
    }

    private fun data_entry(x: IntArray, y: IntArray) {
        val scanner = Scanner(System.`in`)

        val str = arrayOf("A", "B", "C")
        println("Enter the coordinates of the rectangle vertices")
        for (i in 0..2) {
            System.out.printf("Vertex %s (x%d, y%d):%n", str[i], i + 1, i + 1)
            x[i] = scanner.nextInt()
            y[i] = scanner.nextInt()
        }
    }

    private fun checks(a: IntArray, flag: Boolean): Boolean {
        var newFlag = flag
        if (a[0] == a[1]) a[3] = a[2]
        else if (a[0] == a[2]) a[3] = a[1]
        else if (a[1] == a[2]) a[3] = a[0]
        else newFlag = true
        return newFlag
    }
}
