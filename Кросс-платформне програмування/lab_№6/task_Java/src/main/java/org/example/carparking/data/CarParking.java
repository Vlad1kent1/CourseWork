package org.example.carparking.data;

import jakarta.persistence.*;

@Entity
@Table(name = "parking_records")
public class CarParking {
    private String brand_model;
    private String license_plate;
    private String owner_phone;
    private int parking_hour;
    private int prepaid_hours;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    public CarParking() {
        this.brand_model = "";
        this.license_plate = "";
        this.owner_phone = "";
        this.parking_hour = 0;
        this.prepaid_hours = 0;
    }

    public CarParking(String brandModel, String licensePlate, String ownerPhone, int parkingHour, int prepaidHours) {
        this.brand_model = brandModel;
        this.license_plate = licensePlate;
        this.owner_phone = ownerPhone;
        this.parking_hour = parkingHour;
        this.prepaid_hours = prepaidHours;
    }

    public String getBrand_model() {
        return brand_model;
    }

    public void setBrand_model(String brandModel) {
        this.brand_model = brandModel;
    }

    public String getLicense_plate() {
        return license_plate;
    }

    public void setLicense_plate(String licensePlate) {
        this.license_plate = licensePlate;
    }

    public String getOwner_phone() {
        return owner_phone;
    }

    public void setOwner_phone(String ownerPhone) {
        this.owner_phone = ownerPhone;
    }

    public int getParking_hour() {
        return parking_hour;
    }

    public void setParking_hour(int parkingHour) {
        this.parking_hour = parkingHour;
    }

    public int getPrepaid_hours() {
        return prepaid_hours;
    }

    public void setPrepaid_hours(int prepaidHours) {
        this.prepaid_hours = prepaidHours;
    }

    @Override
    public String toString() {
        return "Car: " + brand_model + ", License Plate: " + license_plate + ", Owner's Phone: " + owner_phone +
                ", Parking Hour: " + parking_hour + ", Prepaid Hours: " + prepaid_hours;
    }

    public String toText() {
        return brand_model + "," + license_plate + "," + owner_phone + "," + parking_hour + "," + prepaid_hours;
    }

    public static CarParking fromText(String line) {
        String[] parts = line.split(",");
        if (parts.length == 5) {
            return new CarParking(parts[0], parts[1], parts[2], Integer.parseInt(parts[3]), Integer.parseInt(parts[4]));
        } else {
            return null;
        }
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }
}

