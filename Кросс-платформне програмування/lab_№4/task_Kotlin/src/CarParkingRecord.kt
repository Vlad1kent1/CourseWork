class CarParkingRecord(
    var brandModel: String = "",
    var licensePlate: String = "",
    var ownerPhone: String = "",
    var parkingHour: Int = 0,
    var prepaidHours: Int = 0
) {
    override fun toString(): String {
        return "Car: $brandModel, License Plate: $licensePlate, Owner's Phone: $ownerPhone, Parking Hour: $parkingHour, Prepaid Hours: $prepaidHours"
    }

    fun toText(): String {
        return "$brandModel,$licensePlate,$ownerPhone,$parkingHour,$prepaidHours"
    }

    companion object {
        fun fromText(line: String): CarParkingRecord? {
            val parts = line.split(",")
            return if (parts.size == 5) {
                CarParkingRecord(parts[0], parts[1], parts[2], parts[3].toInt(), parts[4].toInt())
            } else {
                null
            }
        }
    }
}
