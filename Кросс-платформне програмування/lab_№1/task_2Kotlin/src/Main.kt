object Main {
    @JvmStatic
    fun main(args: Array<String>) {

        print("Enter your number: ")
        val num: Int = readln().toInt()

        val size: Int = num / 1024
        println("File size in kilobytes: $size")
    }
}
